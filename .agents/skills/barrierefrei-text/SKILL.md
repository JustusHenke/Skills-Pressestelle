---
name: barrierefrei-text
description: Prüft Texte auf Verständlichkeit und Barrierefreiheit, erstellt eine Variante in einfacher Sprache und schlägt Alternativtexte für Bilder vor. Prüft Lesbarkeit, Satzlänge, Fachbegriffe und Struktur. Ändert keine Fakten und markiert jede inhaltliche Kürzung.
---

# Skill: Barrierearme Textprüfung

## 1. Zweck

Barrierefreiheit ist Pflicht, nicht Kür. Dieser Skill prüft Texte auf Verständlichkeit, erstellt bei Bedarf eine einfache Fassung und liefert Alternativtexte für Bilder. Er arbeitet an der Form und markiert jede Kürzung.

## 2. Einsatzgrenzen

**Nicht geeignet für:** juristische Texte, in denen jede Formulierung bindend ist. Nicht als Ersatz für eine Prüfung durch Menschen mit Behinderung oder Fachexpertise.

**Grenze:** „Einfache Sprache" ist keine „Leichte Sprache". Die Regeln sind unterschiedlich streng. Der Skill liefert einfache Sprache, nicht Leichte Sprache — Letztere braucht Übersetzer:innen nach anerkanntem Regelwerk. Eine Textprüfung ist keine umfassende Barrierefreiheitsprüfung: Sie bestätigt weder WCAG-/EN-Konformität noch Kontrast, Tastaturbedienbarkeit, Screenreader-Ausgabe oder technische Umsetzung.

## 3. Eingaben

Erforderlich:

- zu prüfender Text
- Zielformat (Web, PDF, Social, Print)
- Zielgruppe
- Optional: Bild(er) für Alt-Text, gewünschtes Niveau (Standard/einfach)
- Optional: Regelsatz aus `referenzen/barrierefrei-regeln.md`

## 4. Verbindliche Schritte

1. **Textmerkmale prüfen.** Satzlänge, Passivgebrauch, Fachbegriffe und Verschachtelung beurteilen. Zahlen nur ausgeben, wenn sie zuverlässig aus dem vorliegenden Text gezählt oder berechnet wurden; andernfalls als Schätzung kennzeichnen oder einen qualitativen Befund geben. Keine scheinpräzisen Prozentangaben. Die Richtwerte in der Referenz sind redaktionelle Orientierung, keine Bestehensgrenzen.
2. **Struktur prüfen.** Zwischenüberschriften vorhanden? Listen statt Fließtextblöcke? Aussagekräftige Linktexte statt „hier klicken"?
3. **Begriffe prüfen.** Fachbegriffe und Abkürzungen auflisten, mit Erklärungsbedarf.
4. **Einfache Variante erstellen.** Kurze Sätze, Aktiv, gängige Wörter, ein Gedanke pro Satz. Keine Inhaltskürzung ohne Markierung.
5. **Alt-Texte vorschlagen.** Für jedes Bild eine knappe Beschreibung dessen, was für die Aussage wichtig ist. Nicht das Aussehen beschreiben, sondern die Funktion.
6. **Bericht ausgeben** (Abschnitt 5).

## 5. Ausgabeformat

```
Textmerkmale:  Satzlänge / Passiv / Fachbegriffe / Verschachtelung; Kennzeichnung jeder Zahl als „gezählt/berechnet“ oder „geschätzt“, sonst qualitativer Befund. Keine Konformitätsaussage.
Struktur:    (Befund, z. B. keine Zwischenüberschriften in Abs. 3)
Begriffe:    (Liste mit Erklärungsvorschlag)

Einfache Variante: (Text)

Alt-Texte:
| Bild | Vorschlag | Begründung |

Nicht gekürzt: (was aus inhaltlichen Gründen bleiben muss)
```

## 6. Verbote

- Keine inhaltliche Vereinfachung, die Aussagen verfälscht oder Einschränkungen entfernt.
- Keine Behauptung, der Text erfülle Leichte-Sprache-Normen.
- Keine Veröffentlichung.
- Keine automatische Übernahme in bestehende Seiten ohne Freigabe.

## 7. Prüf- und Freigabeschritte

Die einfache Fassung wird von der Fachabteilung freigegeben. Alt-Texte prüft die Redaktion am Originalbild.

## 8. Referenzdateien

- `referenzen/barrierefrei-regeln.md` — Regelsatz, angelehnt an WCAG/EN 301 549
- `referenzen/alt-text-leitfaden.md`
- `referenzen/stil-guide-hochschule.md`

## 9. Beispiel und Gegenbeispiel

**Beispiel (richtig):**

> Text mr:innen unzulässig.

---

**Verwandte Skills:** `stil-guard`, `kanaladaption`, `bild-prompt`
 Diagramm, dr:innen unzulässig.

---

**Verwandte Skills:** `stil-guard`, `kanaladaption`, `bild-prompt`
auptet „entspricht Leichter Sprache nach DIN" — ohne Prüfung durch zertifizierte Übersetzer:innen unzulässig.

---

**Verwandte Skills:** `stil-guard`, `kanaladaption`, `bild-prompt`
