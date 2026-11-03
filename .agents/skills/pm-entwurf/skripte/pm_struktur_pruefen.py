#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mechanische Orientierung zu einem PM- oder Webnews-Entwurf.

Die Ausgabe ist kein Freigabe- oder Faktencheck. Optionale Elemente wie Zitat,
Untertitel, Faktenkasten und Boilerplate werden nicht als Pflichtbausteine
behandelt. Der Lead wird nur gezählt, wenn er ausdrücklich mit „Lead:"
markiert ist; andernfalls ist er nicht zuverlässig automatisiert erkennbar.

Aufruf:
    PYTHONIOENCODING=utf-8 python pm_struktur_pruefen.py entwurf.txt --format pm
    PYTHONIOENCODING=utf-8 python pm_struktur_pruefen.py entwurf.txt --format webnews
    PYTHONIOENCODING=utf-8 python pm_struktur_pruefen.py entwurf.txt --json
"""

import argparse
import json
import re
import sys

TITEL_MIN, TITEL_MAX = 50, 70
LEAD_WOERTER_MIN, LEAD_WOERTER_MAX = 40, 70

VERBOTSFLOSKELN = [
    "bahnbrechend", "revolutionär", "einzigartig", "weltweit erstmals",
    "Meilenstein", "am Puls der Zeit", "nicht nur", "im Rahmen von",
    "hinsichtlich", "Aufbruch in eine neue Ära",
]
SUPERLATIVE = ["beste", "größte", "führend", "einmalig", "erstmals", "höchste"]


def absaetze(text):
    return [a.strip() for a in re.split(r"\n\s*\n", text) if a.strip()]


def woerter(text):
    return len(re.findall(r"\w+", text))


def titel_auslesen(text):
    """Erkennt einen expliziten Titel oder nimmt die erste nichtleere Zeile als Heuristik."""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    for line in lines:
        labeled = re.match(r"(?i)^(?:titel(?:vorschlag)?)\s*:\s*(.+)$", line)
        if labeled:
            return labeled.group(1).strip()
        if re.match(r"(?i)^(?:format|untertitel|ort|datum|lead)\s*:", line):
            continue
        return re.sub(r"^#{1,6}\s*", "", line).strip()
    return ""


def lead_auslesen(text):
    """Erkennt nur ausdrücklich markierte Lead-Abschnitte."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        match = re.match(r"(?i)^\s*(?:#{1,6}\s*)?lead\s*:\s*(.*)$", line)
        if not match:
            continue
        parts = [match.group(1).strip()] if match.group(1).strip() else []
        for following in lines[i + 1:]:
            if not following.strip() or re.match(r"^\s*#{1,6}\s+", following):
                break
            parts.append(following.strip())
        return " ".join(parts).strip()
    return None


def pruefe(text, format_="pm"):
    befunde = []

    def hinweis(baustein, status, text_hinweis):
        befunde.append({"baustein": baustein, "status": status, "hinweis": text_hinweis})

    zeichen = len(text)
    paras = absaetze(text)
    fmt = format_.lower()

    if fmt == "pm":
        if 1800 <= zeichen < 2500:
            label = "im Richtwertbereich Kurz-PM"
        elif 2500 <= zeichen <= 4000:
            label = "im Richtwertbereich Standard-PM"
        elif 4000 < zeichen <= 6000:
            label = "im Richtwertbereich lange PM/Hintergrund"
        else:
            label = "außerhalb der angegebenen PM-Richtwerte; Format und Material redaktionell prüfen"
    else:
        label = "im Richtwertbereich Webnews (3.000–6.000 Zeichen)" if 3000 <= zeichen <= 6000 else "außerhalb des Webnews-Richtwerts (3.000–6.000 Zeichen); redaktionell prüfen"
    hinweis("Gesamtlänge", "Orientierung", f"{zeichen} Zeichen; {label}. Richtwerte sind keine Bestehensgrenzen.")

    titel = titel_auslesen(text)
    if titel:
        status = "im Richtwert" if TITEL_MIN <= len(titel) <= TITEL_MAX else "redaktionell prüfen"
        hinweis("Titel", status, f"{len(titel)} Zeichen; Referenz-Richtwert {TITEL_MIN}–{TITEL_MAX}. Erkannter Titel: {titel}")
    else:
        hinweis("Titel", "nicht erkannt", "Kein Titel zur automatischen Orientierung erkannt.")

    lead = lead_auslesen(text)
    if lead is None:
        hinweis("Lead", "nicht automatisch geprüft", "Lead nicht eindeutig markiert. Eine Wortzählung wäre ohne verlässliche Abgrenzung irreführend.")
    else:
        n = woerter(lead)
        status = "im Richtwert" if LEAD_WOERTER_MIN <= n <= LEAD_WOERTER_MAX else "redaktionell prüfen"
        hinweis("Lead", status, f"{n} Wörter; Referenz-Richtwert {LEAD_WOERTER_MIN}–{LEAD_WOERTER_MAX}. Richtwert, keine Bestehensgrenze.")

    zitat_vorhanden = bool(re.search(r"[„“»«\"]", text))
    if zitat_vorhanden:
        hinweis("Zitat", "erkannt", "Zitatzeichen gefunden; Eignung, Originalwortlaut, Beleg und Freigabe redaktionell prüfen.")
    else:
        hinweis("Zitat", "nicht erkannt", "Ein Zitat ist nicht automatisch erforderlich; nur bei Bedarf und mit belegtem, freigegebenem Original verwenden.")

    kontakt_erkannt = bool(re.search(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", text) or re.search(r"(?i)(?:telefon|tel\.?|mobil|fax)\s*:?\s*(?:\+\d{1,3}[\s/-]?)?\(?\d{2,5}\)?[\s/-]+\d{3,}", text))
    if fmt == "pm":
        note = "Kontaktangabe erkannt; Aktualität und Freigabe nicht automatisch geprüft." if kontakt_erkannt else "Keine Kontaktangabe erkannt; laut Strukturreferenz ist bei PMs eine Ansprechperson vorgesehen. Aktuelle, freigegebene Kontaktangabe redaktionell ergänzen oder Fehlen als offenen Punkt markieren."
        hinweis("Kontaktangabe (PM)", "Hinweis", note)
        hinweis("Weitere PM-Bausteine", "manuell prüfen", "Ort/Datum, Faktenkasten (falls passend und belegt) sowie aktuelle Boilerplate (falls verwendet) sind aus dem Material und der Freigabereferenz zu prüfen; kein Baustein wird hier pauschal erzwungen.")
    else:
        note = "Kontaktangabe erkannt; Inhalt und Freigabe nicht automatisch geprüft." if kontakt_erkannt else "Kontaktangabe nicht erkannt; für Webnews optional und formatabhängig."
        hinweis("Kontaktangabe (Webnews)", "Hinweis", note)
        hinweis("Zwischenüberschriften", "manuell prüfen", "Bei Webnews nennt die Referenz Zwischenüberschriften etwa alle zwei bis drei Absätze als Orientierung, nicht als starre Pflicht.")

    treffer = [phrase for phrase in VERBOTSFLOSKELN if phrase.lower() in text.lower()]
    superlative = [word for word in SUPERLATIVE if re.search(rf"\b{re.escape(word)}\b", text, re.I)]
    stil_treffer = treffer + superlative
    if stil_treffer:
        hinweis("Formulierungen", "Beleg prüfen", "Mögliche Floskeln/Superlative: " + ", ".join(stil_treffer) + ". Kein automatisches Urteil; Beleg und lokale Stilregeln prüfen.")
    else:
        hinweis("Formulierungen", "keine Treffer", "Keine Treffer in der heuristischen Liste; dies ersetzt keine Stil- oder Faktenprüfung.")

    return {"format": fmt, "zeichen": zeichen, "absaetze": len(paras), "befunde": befunde}


def als_markdown(res):
    out = [f"Format: {res['format']} | Zeichen: {res['zeichen']} | Absätze: {res['absaetze']}", "",
           "Automatische Orientierung, keine Freigabe oder inhaltliche Prüfung.", "",
           "| Baustein | Status | Hinweis |", "|---|---|---|"]
    for item in res["befunde"]:
        note = item["hinweis"].replace("|", "\\|")
        out.append(f"| {item['baustein']} | {item['status']} | {note} |")
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description="Gibt mechanische Orientierung zu einem PM- oder Webnews-Entwurf.")
    parser.add_argument("datei")
    parser.add_argument("--format", choices=("pm", "webnews"), default="pm", help="Format für die passenden Richtwerte (Standard: pm)")
    parser.add_argument("--json", action="store_true", help="JSON statt Markdown")
    args = parser.parse_args()
    try:
        with open(args.datei, encoding="utf-8") as f:
            text = f.read()
    except OSError as exc:
        print(f"Fehler beim Lesen: {exc}", file=sys.stderr)
        return 1
    result = pruefe(text, args.format)
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else als_markdown(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
