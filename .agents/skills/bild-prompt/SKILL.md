---
name: bild-prompt
description: Entwickelt aus einem Textinhalt ein Bildkonzept für Banner-, Presse- oder Social-Bilder und formuliert einen kopierfertigen Generator-Prompt. Nutzt Bildgenerierung nur, wenn die jeweilige Umgebung sie unterstützt. Kennzeichnet KI-Bilder nach den geltenden redaktionellen Vorgaben.
---

# Skill: Bildkonzept, Bildgenerierung und Bild-Prompt

## 1. Zweck

Bilder entscheiden über die Wahrnehmung einer Meldung. Dieser Skill übersetzt einen Inhalt in ein Bildkonzept und formuliert einen kopierfertigen Prompt. Wenn die verwendete Umgebung eine Bildgenerierung unterstützt und die Rechtefrage geklärt ist, kann sie zusätzlich zur Erzeugung von Varianten genutzt werden. Die Entscheidung über die Verwendung bleibt beim Menschen.

## 2. Einsatzgrenzen

**Nicht geeignet für:** Pressebilder mit identifizierbaren realen Personen (Rechte, Persönlichkeitsschutz). Für Fotos von Veranstaltungen gilt Fotodokumentation, nicht Generierung.

**Wichtig:** Für KI-generierte Bilder geltende gesetzliche, Plattform- und Institutionsvorgaben anhand aktueller, konkreter Quellen prüfen. Wenn die Quelle oder Auslegung fehlt, als offen markieren. Ein generiertes Bild ist kein Beleg für tatsächliche Personen, Ereignisse, Orte, Forschungsergebnisse oder Daten. Fotorealismus darf keine dokumentarische Echtheit vortäuschen; bei inszenierten oder synthetischen Motiven Symbol-/Illustrationscharakter deutlich machen.

**Herkunft und Rechte:** Vor einer Nutzung Herkunft und Nutzungsrechte von Ausgangsbildern, Referenzen, Logos, Schriften und anderen bereitgestellten Materialien klären. Keine Rechte oder Modellherkunft behaupten, die nicht belegt sind. Die Pressestelle dokumentiert mindestens generatives Werkzeug/Anbieter (soweit bekannt), Erstellungs- oder Bearbeitungsdatum, verwendete Eingaben/Referenzen sowie die erfolgte Rechte- und Freigabeprüfung. Keine vertraulichen oder personenbezogenen Referenzmaterialien in nicht freigegebene KI-Umgebungen eingeben.

**Direkte Generierung wird nicht angeboten**, wenn:

- reale Personen erkennbar dargestellt werden sollen,
- das Bild als Dokumentarfoto ausgegeben werden soll,
- Marken, Logos oder geschützte Werke nachgebildet werden sollen,
- ein freigegebenes echtes Foto vorliegt (dann Foto verwenden),
- die Umgebung keine Bildgenerierung zulässt (dann nur Prompt liefern).

## 3. Eingaben

Erforderlich:

- Inhalt (PM, Meldung, Veranstaltung)
- Verwendungszweck (Banner, Website-Header, Social, Print)
- Format und Ausrichtung (z. B. 1200×630, 1:1, 9:16)
- Optional: verfügbares Fotomaterial
- Optional: Corporate-Farbwelt/Schriftvorgaben
- Optional: Anzahl gewünschter Bildvarianten (Standard: 3)

## 4. Verbindliche Schritte

1. **Bildidee bestimmen.** Was muss das Bild zeigen, damit die Aussage trägt? Motiv, Situation, Emotion.
2. **Kompositionsskizze.** Vordergrund/Mittelgrund/Hintergrund, Bildachse, Textfreiraum für Titel/Logo.
3. **Format und Ausrichtung.** Für jeden Kanal passend, mit Begründung.
4. **Farb- und Stilwelt.** An die Institution angelehnt; keine fremden Markenfarben.
5. **Generator-Prompt formulieren.** Beschreibung für den Generator: Motiv, Stil, Perspektive, Licht, Farben, Format, Negativ-Prompt (was nicht vorkommen soll, z. B. keine Logos, keine realen Gesichter).
6. **Optional Bild generieren.** Wenn die verwendete Umgebung Bildgenerierung unterstützt, mit dem formulierten Prompt bis zu drei Varianten erzeugen und dem Menschen zur Auswahl vorlegen. Wenn keine Bildgenerierung verfügbar ist, dies melden und nur den Prompt liefern.
7. **Auswahl und Prüfung.** Variante auf unerwünschte Elemente, sachliche Richtigkeit, implizite Behauptungen, falsche Beschriftungen und irreführende Dokumentarwirkung prüfen. Keine Bildaussage als Fakt übernehmen, die nicht unabhängig belegt ist.
8. **Herkunft und Rechte dokumentieren.** Werkzeug/Anbieter und Datum soweit bekannt, verwendete Referenzmaterialien sowie Ergebnis der Rechte-, Datenschutz- und redaktionellen Freigabeprüfung festhalten. Unbekanntes als unbekannt markieren.
9. **Alternativtext bzw. Dekoration bestimmen.** Bildfunktion im Kontext prüfen. Bei informativem Bild relevante sichtbare Inhalte und Funktion beschreiben, ohne eine synthetische Szene als real auszugeben. Bei rein dekorativem Bild nach dem Zielsystem einen leeren Alternativtext vorsehen. Alternativtext am finalen Bild prüfen.
10. **Kennzeichnungshinweis.** Geltende konkrete Vorgaben und Quelle/Stand nennen oder fehlende Grundlage als offen markieren. Kennzeichnung nicht aus dem bloßen Einsatz eines Bildgenerators ableiten.
11. **Risikohinweis.** Rechte, Herkunft, Persönlichkeitsrechte, Marken, Datenschutz, irreführende Bildwirkung und Freigaben.

## 5. Ausgabeformat

```
Bildidee:            (2–3 Sätze)
Komposition:         (Skizze in Worten)
Format:              (px / Seitenverhältnis je Kanal)
Farb-/Stilwelt:      (Beschreibung)
Textfreiraum:        (wo Titel/Logo Platz haben)

Generator-Prompt:
  Motiv:       …
  Stil:        …
  Perspektive: …
  Licht:       …
  Format:      …
  Negativ:     …

Bildvarianten:       (optional, falls in der verwendeten Umgebung verfügbar;
                      andernfalls: "Bildgenerierung in dieser Umgebung nicht verfügbar")
Alternativ-Prompt für andere Werkzeuge:  (derselbe Prompt, kopierfertig)

Bildfunktion:        informativ / dekorativ (mit kurzer Begründung)
Alternativtext:      (für finales informatives Bild; dekorativ: leerer Alt-Text nach Zielsystem)
Herkunft:            (Werkzeug/Anbieter und Datum, soweit bekannt; Referenzmaterialien)
Kennzeichnung:       Ergebnis, konkrete Grundlage und Stand oder „offen“
Freigabe:            (Rechte, Datenschutz, Redaktion — erteilt/offen)
Risiken:             (Rechte, Herkunft, Persönlichkeit, Marken, Datenschutz, irreführende Wirkung)
```

## 6. Verbote

- Kein Prompt, der reale Personen, Marken oder geschützte Werke nachbildet.
- Keine Generierung erkennbarer Gesichter für offizielle Kommunikation.
- Keine Behauptung, ein generiertes Bild sei ein Dokumentarfoto.
- Keine Veröffentlichung ohne Rechteklärung und Prüfung geltender Kennzeichnungsvorgaben.
- Keine Nutzung eines generierten Bildes, solange die jeweils geltenden Kennzeichnungsvorgaben ungeklärt sind.

## 7. Prüf- und Freigabeschritte

Bildkonzept, Prompt und erzeugte Varianten gehen an die Redaktion. Die Auswahl trifft ein Mensch. Die jeweils geltenden Kennzeichnungsregeln und Rechte sind vor Verwendung zu prüfen. Der Skill veröffentlicht nichts, montiert kein Logo und setzt kein Bild in eine Seite ein.

## 8. Referenzdateien

- `referenzen/bildformate-hochschule.md` — Standardformate je Kanal
- `referenzen/corporate-design.md` — Farben, Schriften, Logoschutz
- `referenzen/bild-prompt-beispiele.md`

## 9. Beispiel und Gegenbeispiel

**Beispiel (richtig):**

> Meldung über Gewächshausforschung → Bildidee „modernes Gewächshaus von innen, Morgenlicht, Forschende im Hintergrund unscharf", Format 1200×630, Prompt mit Negativ „keine Logos, keine erkennbaren Gesichter". Der Skill liefert einen kopierfertigen Prompt, den Alt-Text und einen Hinweis zur Kennzeichnung nach den geltenden redaktionellen Vorgaben. Falls die Umgebung Bildgenerierung unterstützt, können Varianten zur Auswahl erstellt werden.

**Gegenbeispiel (falsch):**

> Prompt: „Foto der Professorin X im Labor" → unzulässig, reale Person ohne Einwilligung. Hier wird keine direkte Generierung angeboten.

---

**Verwandte Skills:** `social-posts`, `kanaladaption`, `barrierefrei-text` (Alt-Texte)
