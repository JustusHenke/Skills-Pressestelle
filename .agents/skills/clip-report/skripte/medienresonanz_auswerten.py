#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erstellt eine Rohfassung aus einem bereitgestellten Clipping-CSV-Export.

Zählungen beziehen sich nur auf den Export. Tonalität, Prüfstatus,
Textgrundlage und Auffälligkeiten werden übernommen, nicht unabhängig
verifiziert. Ohne expliziten Status lautet die Erwähnungsprüfung
„nicht prüfbar". Die frühere Spalte „Erwähnung korrekt?" gilt nicht als
Prüfung und wird nur als unbestätigte Exportangabe kenntlich gemacht.

Erkannte Spalten (Reihenfolge beliebig): medium, datum, titel, thema,
tonalitaet, erwaehnung_pruefung, textgrundlage, auffaelligkeit, link.

Aufruf:
    PYTHONIOENCODING=utf-8 python medienresonanz_auswerten.py export.csv
    PYTHONIOENCODING=utf-8 python medienresonanz_auswerten.py export.csv --csv-trenner ";"
"""

import argparse
import csv
import re
import sys
import unicodedata
from collections import Counter
from datetime import datetime
from pathlib import Path

FELDER = [
    "medium", "datum", "titel", "thema", "tonalitaet",
    "erwaehnung_pruefung", "textgrundlage", "auffaelligkeit", "link",
]
ALIASE = {
    "medium": {"medium", "medien", "outlet", "publikation"},
    "datum": {"datum", "date", "veroeffentlichungsdatum"},
    "titel": {"titel", "headline", "ueberschrift"},
    "thema": {"thema", "themenfeld", "topic"},
    "tonalitaet": {"tonalitaet", "sentiment"},
    "erwaehnung_pruefung": {
        "erwaehnung_pruefung", "erwaehnungspruefung", "pruefstatus",
        "pruefstatus_erwaehnung", "erwaehnung_status", "erwaehnung_geprueft",
        "mention_check",
    },
    "textgrundlage": {"textgrundlage", "textumfang", "textabdeckung", "textbasis"},
    "auffaelligkeit": {"auffaelligkeit", "anmerkung", "notiz", "hinweis"},
    "link": {"link", "url", "artikel_link"},
    "erwaehnung_export": {
        "erwaehnung_ok", "erwaehnung_korrekt", "korrektheit_erwaehnung",
    },
}
TONALITAETEN = {"positiv", "neutral", "kritisch", "gemischt", "nicht bewertet"}
STATUS_ALIASE = {
    "geprueft": "geprüft",
    "nicht_pruefbar": "nicht prüfbar",
}


def normalisiere_name(name):
    """Vereinheitlicht Spaltennamen und Statuswerte."""
    name = name.strip().lower().translate(str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}))
    name = unicodedata.normalize("NFKD", name)
    name = "".join(c for c in name if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "_", name).strip("_")


def normalisiere(kopf):
    """Ordnet bekannte Spaltennamen exakt zu; vermeidet Teilstring-Treffer."""
    alias_index = {
        normalisiere_name(alias): feld
        for feld, alias_set in ALIASE.items()
        for alias in alias_set
    }
    mapping = {}
    for i, name in enumerate(kopf):
        feld = alias_index.get(normalisiere_name(name))
        if feld is not None:
            mapping.setdefault(feld, i)
    return mapping


def lies(datei, trenner):
    with open(datei, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f, delimiter=trenner))
    if not rows:
        return [], {}

    mapping = normalisiere(rows[0])
    artikel = []
    for row in rows[1:]:
        if not any(cell.strip() for cell in row):
            continue
        item = {}
        for feld in FELDER:
            idx = mapping.get(feld)
            item[feld] = row[idx].strip() if idx is not None and idx < len(row) else ""

        tone = item["tonalitaet"].strip().lower()
        item["tonalitaet"] = tone if tone in TONALITAETEN else "nicht bewertet"

        raw_status = normalisiere_name(item["erwaehnung_pruefung"])
        item["status_roh"] = item["erwaehnung_pruefung"]
        item["status_standardisiert"] = raw_status in STATUS_ALIASE
        item["erwaehnung_pruefung"] = STATUS_ALIASE.get(raw_status, "nicht prüfbar")
        item["status_aus_export"] = mapping.get("erwaehnung_pruefung") is not None and bool(raw_status)
        if not item["textgrundlage"]:
            item["textgrundlage"] = "nicht angegeben"

        legacy_idx = mapping.get("erwaehnung_export")
        if legacy_idx is not None and legacy_idx < len(row) and row[legacy_idx].strip():
            raw = row[legacy_idx].strip()
            note = f'Exportangabe „Erwähnung korrekt?": {raw} (nicht unabhängig geprüft)'
            item["auffaelligkeit"] = "; ".join(filter(None, [item["auffaelligkeit"], note]))
        artikel.append(item)

    # Kernfelder aus der Berichtsvorlage je Datensatz sichtbar machen.
    for item in artikel:
        item["fehlende_kerndaten"] = [
            feld for feld in ("medium", "datum", "titel", "thema") if not item[feld]
        ]

    # Exakte Übereinstimmungen sind nur Dubletten-Kandidaten; nichts entfernen.
    gruppen = {}
    for nummer, item in enumerate(artikel, start=1):
        datum = parse_datum(item["datum"])
        key = (
            normalisiere_name(item["medium"]),
            datum.isoformat() if datum else normalisiere_name(item["datum"]),
            normalisiere_name(item["titel"]),
        )
        if all(key):
            gruppen.setdefault(key, []).append(nummer)
    for nummern in gruppen.values():
        if len(nummern) > 1:
            for nummer in nummern:
                artikel[nummer - 1]["dubletten_ids"] = nummern

    return artikel, mapping


def parse_datum(wert):
    """Liest nur eindeutig unterstützte Datumsformate, ohne Werte zu erraten."""
    wert = wert.strip()
    if not wert:
        return None
    try:
        return datetime.fromisoformat(wert.replace("Z", "+00:00")).date()
    except ValueError:
        pass
    for fmt in ("%d.%m.%Y", "%d.%m.%y", "%Y/%m/%d"):
        try:
            return datetime.strptime(wert, fmt).date()
        except ValueError:
            continue
    return None


def esc(value):
    """Bereitet Feldwerte als Markdown-Tabellenzellen auf."""
    return str(value).replace("|", "\\|").replace("\r", " ").replace("\n", " ").strip()


def bericht(artikel, mapping, datei):
    daten = [(a["datum"], parse_datum(a["datum"])) for a in artikel]
    parsebar = [wert for _, wert in daten if wert is not None]
    nicht_parsebar = sum(1 for _, parsed in daten if parsed is None)
    zeitraum = f"{min(parsebar).isoformat()} bis {max(parsebar).isoformat()}" if parsebar else "nicht zuverlässig bestimmbar"
    if parsebar and nicht_parsebar:
        zeitraum += f" (unvollständig; {nicht_parsebar} Datumsangaben fehlen oder sind nicht interpretierbar)"

    out = ["# Medienresonanz [HOCHSCHULNAME] (Rohfassung)", "", "```"]
    out.append(f"Zeitraum (aus eindeutig interpretierbaren Exportdaten): {zeitraum}")
    if nicht_parsebar:
        out.append(f"Datumsangaben ohne zuverlässig interpretierbares Datum: {nicht_parsebar}")
    out.append(f"Quelle (Dateiname): {Path(datei).name}")
    out.append(f"Artikel im bereitgestellten Export: {len(artikel)}")
    medien = {a["medium"] for a in artikel if a["medium"]}
    out.append(f"Medien im bereitgestellten Export: {len(medien)}")
    fehlend = [feld for feld in FELDER if feld not in mapping]
    if fehlend:
        out.append("Fehlende Spalten: " + ", ".join(fehlend))
    out.append("Datenbasis: Nur der bereitgestellte CSV-Export; Vollständigkeit nicht geprüft.")
    out.extend(["```"])
    out.extend([
        "", "## Übersicht", "",
        "| Medium | Datum | Titel | Thema | Tonalität (Exportangabe) | Erwähnungsprüfung | Textgrundlage | Auffälligkeit | Link |",
        "|---|---|---|---|---|---|---|---|---|",
    ])
    for a in artikel:
        if a["status_aus_export"] and a["status_standardisiert"]:
            status = f'{a["erwaehnung_pruefung"]} (laut Export; nicht unabhängig geprüft)'
        elif a["status_aus_export"]:
            status = f'nicht prüfbar (Statusangabe „{a["status_roh"]}" nicht standardisiert)'
        else:
            status = "nicht prüfbar (Prüfstatus im Export fehlt)"
        notiz = a["auffaelligkeit"]
        if a.get("fehlende_kerndaten"):
            notiz = "; ".join(filter(None, [notiz, "Fehlend: " + ", ".join(a["fehlende_kerndaten"])]))
        if a.get("dubletten_ids"):
            notiz = "; ".join(filter(None, [notiz, "Dubletten-Kandidat zu Datensatz(en): " + ", ".join(map(str, a["dubletten_ids"]))]))
        values = [
            a["medium"], a["datum"], a["titel"], a["thema"], a["tonalitaet"],
            status, a["textgrundlage"], notiz, a["link"],
        ]
        out.append("| " + " | ".join(esc(v) for v in values) + " |")

    out.extend(["", "## Verdichtung", "", "Häufigste Themen (nur im Export):"])
    themen = Counter(a["thema"] for a in artikel if a["thema"])
    out.extend(
        (f"- {esc(thema)} ({anzahl})" for thema, anzahl in themen.most_common(5))
        if themen else ["- (kein Themenfeld im Export gefüllt)"]
    )
    out.extend(["", "Exportierte Tonalitätsangaben (nicht unabhängig geprüft):"])
    ton = Counter(a["tonalitaet"] for a in artikel)
    out.extend(f"- {esc(label)}: {anzahl}" for label, anzahl in ton.most_common())

    auffaellig = [a for a in artikel if a["auffaelligkeit"]]
    out.extend(["", "Im Export eingetragene Auffälligkeiten (nicht unabhängig verifiziert):"])
    if auffaellig:
        for a in auffaellig[:20]:
            out.append(
                f'- {esc(a["medium"])} ({esc(a["datum"])}): '
                f'{esc(a["titel"])} — {esc(a["auffaelligkeit"])}'
            )
    else:
        out.append("- keine eingetragen")

    dubletten_gruppen = sorted({tuple(a["dubletten_ids"]) for a in artikel if a.get("dubletten_ids")})
    out.extend(["", "Dubletten-Kandidaten (automatisch erkannt, manuell prüfen):"])
    if dubletten_gruppen:
        for ids in dubletten_gruppen:
            out.append("- Datensätze " + ", ".join(map(str, ids)))
    else:
        out.append("- keine exakten Kandidaten erkannt; inhaltliche Dubletten sind damit nicht ausgeschlossen")

    out.extend(["", "## Handlungsbedarf (Vorschlag)", "",
                "| Anlass | Empfohlene Maßnahme | Zuständigkeit | Frist |",
                "|---|---|---|---|"])
    auffaelligkeitswerte = {a["auffaelligkeit"].strip().lower() for a in artikel if a["auffaelligkeit"].strip()}
    export_hinweise = []
    if any(feld not in mapping for feld in ("titel", "datum", "medium")):
        export_hinweise.append("Fehlende Kerndaten-Spalten im Export; Datengrundlage ergänzen.")
    if any(a.get("fehlende_kerndaten") for a in artikel):
        export_hinweise.append("Einzelne Datensätze haben leere Kerndaten; Einträge prüfen und ergänzen.")
    if any(a.get("dubletten_ids") for a in artikel):
        export_hinweise.append("Exakte Dubletten-Kandidaten gefunden; Datensätze manuell vergleichen, nicht automatisch entfernen.")
    if nicht_parsebar:
        export_hinweise.append("Datumsfelder konnten nicht vollständig interpretiert werden; Zeitraum manuell verifizieren.")
    if any(a["erwaehnung_pruefung"] == "nicht prüfbar" for a in artikel):
        export_hinweise.append("Erwähnungsprüfung ist nicht belegt oder im Export nicht angegeben; Artikeltext und Vergleichsquelle manuell prüfen.")
    if auffaelligkeitswerte:
        export_hinweise.append("Im Export vermerkte Auffälligkeiten redaktionell gegen Artikeltext und Quelle prüfen.")
    if export_hinweise:
        for hinweis in export_hinweise:
            out.append(f"| Exportfeld / Prüfbedarf | {esc(hinweis)} | Redaktion (Vorschlag) | offen |")
    else:
        out.append("| — | Keine Handlung aus den Exportfeldern ableitbar; redaktionelle Prüfung entscheidet | Redaktion | — |")

    out.extend([
        "", "## Grenzen und nächste Prüfung", "",
        "- Artikel- und Medienzahlen beschreiben nur den bereitgestellten Export, nicht dessen Vollständigkeit oder tatsächliche Reichweite.",
        "- Tonalität, Prüfstatus, Textgrundlage und Auffälligkeiten werden aus dem Export übernommen; dieses Skript bewertet sie nicht unabhängig. Ausgegebene Links werden nicht geöffnet oder auf Aktualität geprüft.",
        "- Ohne expliziten Prüfstatus ist die Erwähnung als „nicht prüfbar“ markiert. Eine Richtigkeitsbewertung erfordert ausreichenden Artikeltext und eine verlässliche Vergleichsquelle.",
        "- Tatsächliche Reichweite oder Reputationswirkung sind ohne geeignete Daten und Methode nicht ableitbar.",
        "- Rohfassung; redaktionelle Prüfung und Freigabe bleiben erforderlich.",
    ])
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description="Erstellt eine Rohfassung aus einem Clipping-Export.")
    parser.add_argument("datei", help="Bereitgestellte CSV-Datei")
    parser.add_argument("--csv-trenner", default=",", help="Trennzeichen, Standard ,")
    args = parser.parse_args()
    try:
        artikel, mapping = lies(args.datei, args.csv_trenner)
    except OSError as exc:
        print(f"Fehler beim Lesen: {exc}", file=sys.stderr)
        return 1
    except csv.Error as exc:
        print(f"CSV-Fehler: {exc}", file=sys.stderr)
        return 1
    if not artikel:
        print("Keine Artikel gefunden. Spaltennamen oder CSV-Inhalt prüfen.", file=sys.stderr)
        return 1
    print(bericht(artikel, mapping, args.datei))
    return 0


if __name__ == "__main__":
    sys.exit(main())
