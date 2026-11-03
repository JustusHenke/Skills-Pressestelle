---
name: clip-report
description: Wertet einen vorhandenen Medienresonanz- oder Clipping-Export aus — Tonalität, Thema, Erwähnung, zitierte Personen — und erstellt eine Übersicht mit Auffälligkeiten und Handlungsbedarf. Bewertet nur bereitgestellte Daten, betreibt keine Recherche und keine Scraping-Aktivität.
---

# Skill: Medienresonanz auswerten

## 1. Zweck

Medienresonanz wird oft gesammelt, aber selten ausgewertet. Dieser Skill nimmt einen vorhandenen Export (CSV, Text, Tabelle) und macht daraus eine Übersicht: wie oft, in welcher Tonalität, zu welchem Thema, mit welchen Aussagen. Er erfindet keine Daten und holt keine selbst.

## 2. Einsatzgrenzen

**Nicht geeignet für:** Krisenbeobachtung in Echtzeit — dafür braucht es einen Monitoringservice. Nicht als Ersatz für manuelle Prüfung einzelner Artikel, wenn Tonalität strittig ist.

**Grenze:** Der Skill wertet nur die bereitgestellten Daten aus. Fehlt der Volltext, kann er Tonalität, Kontext, korrekte Wiedergabe und mögliche Fehler nicht zuverlässig prüfen; Titel, Metadaten oder Kurzbeschreibungen reichen dafür nicht. CSV-Zählungen beschreiben nur den Export und belegen weder vollständige Medienabdeckung noch tatsächliche Reichweite oder Wirkung. Diese Grenzen je Ergebnis ausweisen; fehlende Felder nicht schätzen.

## 3. Eingaben

Erforderlich:

- Export oder Liste von Medienartikeln: Medium, Datum, Titel, ggf. Autor:in, Link, Text oder Zusammenfassung
- Fragestellung (z. B. „Wie wurde unsere Förderung aufgenommen?", „Welche Tonalität zur Studienreform?")
- Optional: Vergleichszeitraum, Zielmedienliste, definierte Kategorien

## 4. Verbindliche Schritte

1. **Daten prüfen.** Fehlende Felder, Dubletten, Datumsfehler, doppelte Medien benennen.
2. **Kategorisieren.** Nach Thema, Medium, Zeitraum, Tonalität (positiv/neutral/kritisch/gemischt) — letzteres nur, wenn es aus dem Text begründbar ist. Sonst „nicht bewertet".
3. **Erwähnungen und Wiedergabe prüfen.** Nur bei vorliegendem ausreichendem Artikeltext beurteilen, ob Institution, Personen, Projekte oder Kernbotschaften korrekt wiedergegeben sind. Bei fehlendem oder auszugsweisem Text den Status „nicht prüfbar“ ausweisen und Umfang der verfügbaren Textgrundlage nennen.
4. **Auffälligkeiten finden.** Wiederkehrende Themen und Kritik nur innerhalb des vorliegenden Exports beschreiben. Tonalität, sachliche Richtigkeit, Platzierung/Reichweite und tatsächliche Reputationswirkung getrennt behandeln. Eine Wirkung nicht aus Tonalität, Artikelzahl oder Platzierung ableiten; nur direkt beobachtbare Merkmale berichten.
5. **Handlungsbedarf vorschlagen.** Eine Richtigstellung nur dann als Kandidat nennen, wenn eine konkrete falsche Wiedergabe anhand ausreichenden Artikeltexts und einer verlässlichen Vergleichsquelle belegt ist. Bei fehlendem Volltext oder unklarer Faktenlage nur „manuell prüfen“ vorschlagen. Kein Nachfassen oder Kontakt ohne redaktionelle Freigabe.
6. **Bericht ausgeben** (Abschnitt 5).

## 5. Ausgabeformat

```
Zeitraum:        (von–bis) | Artikel im bereitgestellten Export: N | Medien im Export: N
Datenbasis:      (Datei/Stand; Volltext, Auszüge oder Metadaten; erkennbare Abdeckungslücken)
Nicht ableitbar: tatsächliche Gesamtreichweite oder Reputationswirkung, sofern dafür keine geeigneten Daten vorliegen

Übersicht:
| Medium | Datum | Titel | Thema | Tonalität | Erwähnungsprüfung (geprüft / nicht prüfbar) | Textgrundlage | Auffälligkeit |

Verdichtung:
- Häufigste Themen: …
- Medien mit wiederkehrender Kritik: …
- Falsch wiedergegebene Angaben: …

Handlungsbedarf (Vorschlag):
| Anlass | Empfohlene Maßnahme | Zuständigkeit |
```

## 6. Verbote

- Keine erfundenen Artikel, Medien, Zahlen.
- Keine Tonalitätsbewertung ohne Textgrundlage. Stattdessen „nicht bewertet".
- Keine automatische Kontaktaufnahme oder Richtigstellung.
- Keine Bewertung der politischen Ausrichtung von Medien.
- Keine Speicherung personenbezogener Daten ohne Rechtsgrundlage.

## 7. Prüf- und Freigabeschritte

Der Bericht dient der internen Lageübersicht. Maßnahmen gehen in die übliche Freigabe. Bei personenbezogenen Daten Datenschutzregeln beachten.

## 8. Referenzdateien

- `referenzen/tonalitaets-kriterien.md` — Definition von positiv/neutral/kritisch
- `referenzen/zielmedien-hochschule.md`
- `referenzen/clip-report-vorlage.md`
- `skripte/medienresonanz_auswerten.py` — optionale Auswertung bereitgestellter CSV-Exporte

## 9. Beispiel und Gegenbeispiel

**Beispiel (richtig):**

> CSV mit 40 Artikeln → Übersichtstabelle; drei Artikel mit falscher Bezeichnung der Hochschule markiert; Vorschlag: Richtigstellungshinweis an zwei Redaktionen.

**Gegenbeispiel (falsch):**

> Artikel fehlt im Export → Skill ergänzt „vermutlich auch im Handelsblatt erschienen". → Erfindung, verboten.

---

**Verwandte Skills:** `nachrichtenwert-vorsortierung`, `presseanfrage-triage`
