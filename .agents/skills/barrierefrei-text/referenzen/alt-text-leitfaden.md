# Referenz: Alt-Text-Leitfaden

> Leitfaden für `barrierefrei-text`. Ein Alternativtext beschreibt, was für die Aussage wichtig ist — nicht, wie das Bild aussieht.

## Grundregel

Ein Alt-Text ersetzt das Bild für Menschen, die es nicht sehen können. Er soll die Information tragen, die das Bild trägt, im Kontext des Textes.

## Aufbau

1. **Was** ist zu sehen (Gegenstand, Person, Situation)
2. **Wo/Wie** nur wenn aussagekräftig (Kontext)
3. **Warum relevant** — im Verhältnis zum Text

## Längenrichtwerte

| Kontext | Länge |
|---|---|
| Dekoratives Bild | leer (leeres alt-Attribut) |
| Informatives Bild | 80 bis 120 Zeichen |
| Diagramm oder Grafik | bis 200 Zeichen, ggf. zusätzliche Textbeschreibung |
| Porträt | Name und Funktion, wenn im Kontext nötig |

## Beispiele

**Gut:**
„Klimahalle der [HOCHSCHULNAME] von innen, in der junge Obstbäume unter kontrollierten Bedingungen wachsen."

**Schlecht:**
„Bild1" oder „Foto" oder „Grafik" — ohne Information.

**Gut (Diagramm):**
„Balkendiagramm: Fördersumme der [HOCHSCHULNAME] je Jahr 2023 bis 2026, Anstieg von 8 auf 14 Millionen Euro."

**Schlecht (Diagramm):**
„Balkendiagramm."

## Regeln

- Keine Wiederholung des Titels oder der Bildunterschrift
- Keine Einleitung mit „Bild von" oder „Foto zeigt"
- Keine Wertung (etwa „schönes Foto")
- Keine Farbe allein beschreiben, wenn sie Information trägt
- Keine Personen nennen, deren Einwilligung fehlt

## Sonderfälle

**Dekoratives Bild:** leeres Alt-Attribut (`alt=""`), nicht weglassen. So überspringen Screenreader das Bild.

**Bild mit Text:** den Text im Alt-Text wiedergeben, nicht nur beschreiben, dass Text vorhanden ist.

**Komplexe Grafik:** kurzer Alt-Text plus ausführliche Beschreibung im Fließtext daneben.
