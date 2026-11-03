# Referenz: Bild-Prompt-Beispiele

> Beispiele für `bild-prompt`. Alle Motive sind fiktiv. Zweck: zeigen, wie ein Prompt aufgebaut ist und wann ein Negativ-Prompt nötig ist.

## Bildgenerierung als optionale Funktion

Wenn die verwendete Umgebung Bildgenerierung unterstützt und die Rechtefrage geklärt ist, kann der Prompt für bis zu drei Varianten genutzt werden. Andernfalls wird nur der kopierfertige Prompt ausgegeben. Der Mensch prüft und wählt aus.

- Der kopierfertige Prompt wird zusätzlich ausgegeben, damit das Bild auch in anderen Werkzeugen entstehen kann.
- Vor externer Nutzung geltende gesetzliche, plattform- und institutionsspezifische Kennzeichnungsvorgaben prüfen.
- Kein Logo in das generierte Bild montieren — Logo separat nach Markenrichtlinie.
- Bei echten Fotos (freigegebenes Material) wird nicht generiert, sondern das Foto verwendet.

## Aufbau eines Prompts

```
Motiv:        (was zu sehen ist)
Stil:         (Fotografie, Illustration)
Perspektive:  (Kamerawinkel, Bildausschnitt)
Licht:        (Tageslicht, weich, gerichtet)
Farben:       (Stimmung, Markenbezug)
Format:       (Seitenverhältnis, Pixel)
Negativ:      (was nicht vorkommen darf)
```

## Beispiel 1 — Forschungsmeldung

```
Motiv:        Junger Obstbaum in einer Versuchsanlage, Sortenschild unscharf
              im Hintergrund
Stil:         dokumentarische Fotografie
Perspektive:  Augenhöhe, mittlere Totale
Licht:        weiches Morgenlicht, leichte Schatten
Farben:       natürliche Grün- und Brauntöne, warme Stimmung
Format:       16:9, 1920×1080
Negativ:      keine erkennbaren Gesichter, keine Logos, keine Schrift,
              keine Stockpose-Idealtypen
```

## Beispiel 2 — Studienstart

```
Motiv:        Gruppe von Studierenden mit Büchern auf einer Campuswiese, im
              Hintergrund ein Hochschulgebäude unscharf
Stil:         dokumentarische Fotografie
Perspektive:  leichte Aufsicht, natürliches Weitwinkel ohne Verzerrung
Licht:        Nachmittagslicht, warm
Farben:       natürliche Töne
Format:       4:5, 1080×1350
Negativ:      keine erkennbaren Gesichter, keine Logos, keine Schrift
```

## Beispiel 3 — Datenmeldung (Grafik statt Foto)

```
Motiv:        Schlichtes, reduziertes Diagramm zur Entwicklung der Fördersumme
Stil:         flache Infografik, ruhig
Perspektive:  frontal
Licht:        entfällt
Farben:       zwei Serienfarben aus der Markenpalette, kontrastreich
Format:       16:9, 1200×675
Negativ:      keine Verläufe, keine Schatten, kein 3D, keine Bild-Icons
```

Bei Daten ist ein echtes Diagramm (Skript oder geeignetes Visualisierungswerkzeug) besser als ein generiertes Bild. Generierte Diagramme können inhaltlich falsch sein. Für Datenlayouts wird deshalb keine Bildgenerierung empfohlen — stattdessen der Hinweis auf ein überprüfbares Diagramm.

## Wann Negativ-Prompt Pflicht ist

- Immer, sobald Personen im Bild sind (Gesichter)
- Immer, sobald Marken oder Logos im Umfeld vorkommen könnten
- Immer, wenn Schrift im Bild zu erwarten ist
- Bei Datenlayouts (keine dekorativen Elemente)

## Fehlerquellen

- „professionelles Foto einer Professorin" → reale Person, unzulässig
- „mit [HOCHSCHULNAME]-Logo" → Logo wird nicht generiert, separat montieren
- „Balkendiagramm mit Zahl X" → generierte Zahlen sind erfunden
