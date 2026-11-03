#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kategorien_markieren.py

Findet in einem Text prüfpflichtige Aussagen und ordnet sie den Kategorien
aus referenzen/pruefpflichtige-kategorien.md zu. Erzeugt eine Markdown-Tabelle
im Format, das der Skill `faktencheck` erwartet (Rohfassung, Status = ungeprüft).

Der Belegstatus wird NICHT erfunden. Das Skript markiert nur, WAS zu prüfen ist.
Die Belege trägt die Redaktion ein.

Aufruf:
    PYTHONIOENCODING=utf-8 python kategorien_markieren.py eingabe.txt
    PYTHONIOENCODING=utf-8 python kategorien_markieren.py eingabe.txt --json

Ausgabe: Markdown-Tabelle auf stdout (oder JSON mit --json).
"""

import argparse
import json
import re
import sys

# Reihenfolge wichtig: spezifischere Muster zuerst. Begriffe folgen dem Kategorienkatalog;
# einfache reguläre Ausdrücke liefern Hinweise, keine vollständige Erkennung.
MUSTER = [
    ("Zitat", re.compile(r'[„"»]\s*[^"“”«]{10,}\s*[“"«]')),
    ("Zahl / Betrag", re.compile(r'\b\d[\d.,]*(?:\s*(?:Mio\.?|Millionen|Mrd\.?|Milliarden|Euro|EUR|€|%|Prozent(?:punkte)?|Studierende|Studierenden|Personen|Forschende|Jahre|km|Quadratmeter))?(?=\b|[^A-Za-zÄÖÜäöüß0-9_])', re.I)),
    ("Datum / Frist", re.compile(r'\b\d{1,2}\.\s*(Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\s*\d{2,4}\b|\b\d{1,2}\.\d{1,2}\.\d{2,4}\b|\b(20\d{2})\s*[–-]\s*(20\d{2})\b', re.I)),
    ("Fördergeber", re.compile(r'\b(BMBF|BMEL|DFG|EU|Bund|Land|Stiftung|Ministerium|Horizon|Erasmus)\b')),
    ("Rang / Vergleich", re.compile(r'\b(Platz|Rang|Rangliste|Ranking|Top\s?\d+|Auszeichnung|Preis)\b', re.I)),
    ("Rechtsbezug", re.compile(r'\b(Satzung|Verordnung|Ordnung|§\s?\d+|Art\.\s?\d+)\b', re.I)),
    ("Statistik / Studie", re.compile(r'\b(Studie|Erhebung|Umfrage|Prozent|Proband|Stichprobe|n\s?=\s?\d+)\b', re.I)),
    ("Eigenname (Institution)", re.compile(r'\b(Hochschule|Universität|Fakultät|Institut|Zentrum)\b')),
    ("Eigenname (Person)", re.compile(r'\b(Prof\.?|Dr\.?|Professor\w*|Präsident\w*|Dekan\w*)\s+[A-ZÄÖÜ][a-zäöüß]+')),
    ("Ortsangabe", re.compile(r'\b(Campus|Standort|Gebäude)\b')),
    ("Hyperlink", re.compile(r'https?://\S+')),
]


ABKUERZUNGEN = ("Mio.", "Mrd.", "Dr.", "Prof.", "Nr.", "Abs.", "S.", "bzw.", "z. B.", "ca.", "vgl.", "u. a.", "etc.")


def saetze(text):
    """Zerlegt Text grob in Sätze. Schützt gängige Abkürzungen vor Falschtrennung."""
    text = re.sub(r'\s+', ' ', text).strip()
    geschuetzt = text
    for abk in ABKUERZUNGEN:
        geschuetzt = geschuetzt.replace(abk, abk.replace(".", "\u0001"))
    teile = re.split(r'(?<=[.!?])\s+', geschuetzt)
    return [t.replace("\u0001", ".").strip() for t in teile if t.strip()]


def analysiere(text):
    """Erkennt nur bekannte Muster; unerkannte Aussagen müssen manuell ergänzt werden."""
    rows = []
    nr = 0
    for satz in saetze(text):
        treffer = []
        for kategorie, muster in MUSTER:
            if muster.search(satz):
                treffer.append(kategorie)
        if treffer:
            nr += 1
            rows.append({
                "nr": nr,
                "aussage": satz,
                "kategorien": sorted(set(treffer)),
                "status": "ungeprüft",
                "beleg": "",
                "bedarf": "Beleg erforderlich",
            })
    return rows


def als_markdown(rows):
    out = ["Automatische Mustererkennung ist unvollständig; alle prüfpflichtigen Aussagen manuell ergänzen. Treffer können mehrere Aussagen umfassen und müssen ggf. aufgeteilt werden.",
           "",
           "| Nr. | Aussage (wörtlich) | Kategorie | Status | Beleg / Fundstelle | Handlungsbedarf |",
           "|---:|---|---|---|---|---|"]
    for r in rows:
        aussage = r["aussage"].replace("|", "\\|")
        out.append(f'| {r["nr"]} | {aussage} | {", ".join(r["kategorien"])} | {r["status"]} |  | {r["bedarf"]} |')
    out.append("")
    out.append("Prüfliste Redaktion:")
    out.append("[ ] Alle 'ungeprüft' und 'teilbelegt' an der Quelle geklärt")
    out.append("[ ] Alle 'zurückgewiesen' mit Fachstelle/Redaktion geklärt; keine stille Korrektur erfolgt")
    out.append("[ ] Zitat-Wortlaut mit der aussagenden Person abgeglichen")
    out.append("[ ] Fristen und Zuständigkeiten bestätigt")
    out.append("[ ] Kennzeichnung nach geltenden gesetzlichen, Plattform- und Institutionsvorgaben geprüft (falls nach außen)")
    out.append("[ ] Freigabe durch verantwortliche Person eingeholt")
    return "\n".join(out)


def main():
    p = argparse.ArgumentParser(description="Markiert prüfpflichtige Aussagen.")
    p.add_argument("datei", help="Textdatei (UTF-8)")
    p.add_argument("--json", action="store_true", help="JSON statt Markdown")
    args = p.parse_args()

    try:
        with open(args.datei, encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        print(f"Fehler beim Lesen: {e}", file=sys.stderr)
        return 1

    rows = analysiere(text)
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    else:
        print(als_markdown(rows))
        print(f"\n{len(rows)} prüfpflichtige Aussagen gefunden.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
