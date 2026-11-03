---
name: stil-guard
description: Prüft einen Text gegen die Stil-, Terminologie- und Anrederegeln einer Hochschule und liefert eine Änderungsliste mit Begründung je Fundstelle. Setzt Hausstandards durch, ohne Inhalte umzuschreiben oder Fakten zu verändern.
---

# Skill: Stil- und Terminologieprüfung

## 1. Zweck

Ein Hausstil, der überall gilt, wirkt über alle anderen Skills. Dieser Skill prüft Texte gegen eine hinterlegte Stilreferenz: Anrede, Tonalität, Terminologie, Gendern, Zahlenformate, Abkürzungen, Produktnamen, institutionelle Bezeichnungen. Er produziert eine Änderungsliste, keine Neufassung.

## 2. Einsatzgrenzen

**Nicht geeignet für:** inhaltliche, fachliche oder rechtliche Prüfung. Der Skill prüft Form, nicht Substanz. Für Fakten greift `faktencheck`.

**Voraussetzung:** Es muss eine gepflegte Stilreferenz geben. Ohne sie ist der Skill wirkungslos — dann zuerst `referenzen/stil-guide-hochschule.md` füllen.

## 3. Eingaben

Erforderlich:

- zu prüfender Text
- Stilreferenz (Hausstandard)
- Optional: Kanal (Web, Social, Print), Zielgruppe

## 4. Verbindliche Schritte

1. **Regelkatalog laden** aus der Stilreferenz. Kategorie und Schweregrad nur übernehmen, wenn die lokale Regel sie ausdrücklich festlegt. Fehlt ein Schweregrad, „nicht festgelegt“ ausweisen; keinen Muss-/Sollte-/Kann-Status ableiten.
2. **Text durchlaufen.** Satzweise gegen den Katalog prüfen.
3. **Fundstellen sammeln.** Jede Abweichung mit Zitat, Position und Regelverweis.
4. **Änderungsvorschlag** je Fundstelle — als Vorschlag, nicht als Änderung am Text.
5. **Konsistenzprüfung.** Schreibweisen, Abkürzungen und Bezeichnungen über den Text hinweg vergleichen. Widersprüchliche Schreibweisen benennen.
6. **Bericht ausgeben** (Abschnitt 5).

## 5. Ausgabeformat

| Nr. | Fundstelle (Zitat) | Kategorie | Regel | Schweregrad | Vorschlag | Begründung |
|---:|---|---|---|---|---|---|
| 1 | … | … | … | nicht festgelegt | … | lokale Stilreferenz, Abschnitt … |

Danach:

```
Konsistenzhinweise: (uneinheitliche Schreibweisen, widersprüchliche Bezeichnungen)
Nicht bewertet: (Passagen, für die keine Regel vorliegt — zur Freigabe markieren)
```

## 6. Verbote

- Keine Inhaltsänderung. Nur Form.
- Keine Regeln erfinden, die nicht in der Stilreferenz stehen. Wünsche als „Vorschlag zur Ergänzung" kennzeichnen.
- Keine Faktenkorrektur, keine Bewertung politischer Aussagen.
- Keine automatische Übernahme in den Text.

## 7. Prüf- und Freigabeschritte

Die Redaktion entscheidet, welche Vorschläge übernommen werden. Einen Verstoß als Freigabehindernis kennzeichnen, wenn die lokale Regel dies ausdrücklich vorsieht. Die Bezeichnungen Muss/Sollte/Kann allein begründen keine automatische Blockierung, sofern der Hausstandard das nicht festlegt. Keine stillschweigende Korrektur.

## 8. Referenzdateien

- `referenzen/stil-guide-hochschule.md` — Anrede, Terminologie, Gendern, Formate
- `referenzen/verbotsliste.md` — nicht zu verwendende Begriffe (KI-Marker, Floskeln, Marketing-Sprache)
- `referenzen/eigennamen.md` — korrekte Bezeichnungen von Einrichtungen und Projekten

## 9. Beispiel und Gegenbeispiel

**Beispiel (richtig):**

> Text enthält einen Namen oder eine Hochschulbezeichnung, die von der hinterlegten Namensliste abweicht. Ausgabe nennt Fundstelle und zugehörige lokale Regel; einen Schweregrad weist sie nur aus, wenn der Regelkatalog ihn ausdrücklich festlegt.

**Gegenbeispiel (falsch):**

> Skill schreibt den Text komplett neu, um den Stil zu treffen. → Überschreitung: der Skill prüft, er schreibt nicht um.

---

**Verwandte Skills:** `faktencheck`, `barrierefrei-text`, `kanaladaption`
