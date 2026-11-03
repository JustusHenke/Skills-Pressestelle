---
name: pm-entwurf
description: Erzeugt aus Rohmaterial (Faktenblatt, Interviewnotizen, Förderbescheid, Terminangaben) einen strukturierten Entwurf für eine Pressemitteilung oder Webnews nach Hochschulkonvention. Liefert Entwurf, offene Punkte und Faktencheckliste. Veröffentlicht nichts, erfindet keine Angaben.
---

# Skill: Pressemitteilungsentwurf

## 1. Zweck

Rohmaterial in einen vorzeigbaren Entwurf überführen — schneller als ein leerer Bildschirm, ohne den Faktencheck zu umgehen. Der Skill unterstützt eine Hochschulpressestelle beim Übersetzen, Glätten und strukturierten Prüfen von Ausgangsmaterial.

## 2. Einsatzgrenzen

**Nicht geeignet für:** Krisenkommunikation, Rechtsstreitigkeiten, Personalangelegenheiten, Drittmittel-Akquise-Texte mit Zusagen. Ebenso nicht für Fälle, in denen noch kein freigegebenes Faktenmaterial vorliegt — dann liefert der Skill nur eine Struktur, keinen Text.

**Grenze:** Der Entwurf ist ein Arbeitsprodukt. Namen, Zahlen, Zitate, Fristen und Zuständigkeiten stammen ausschließlich aus dem bereitgestellten Material.

## 3. Eingaben

Erforderlich:

- Rohmaterial: Faktenblatt, Notizen, Förderbescheid, Presseinfo Dritter, Terminangaben
- Anlass und Ziel der Mitteilung
- Zielgruppe(n) und Kanal (PM, Webnews, Newsletter)
- Optional: verfügbare Zitate der Beteiligten, Bildmaterial, Freigabestatus
- Optional: [HOCHSCHULNAME]-Stilreferenz (siehe `referenzen/stil-guide-hochschule.md`)

## 4. Verbindliche Schritte

1. **Material sichten.** Alles, was nicht im Material steht, wird nicht erfunden. Fehlende Angaben kommen in die Liste „Offene Punkte".
2. **Nachrichtenkern bestimmen.** Einen Satz formulieren, der die Nachricht trägt. Kein Themenüberblick, sondern das Ereignis.
3. **Struktur anlegen** (Abschnitt 5).
4. **Lead schreiben.** Erster Absatz: Wer, was, wann, wo, warum, mit welcher Bedeutung. Nachrichtlich vorne.
5. **Körper.** Hintergrund, Einordnung, Förderung, Anwendungsbezug. Regionalen Bezug nur, wenn er belegt ist.
6. **Zitat einsetzen, falls geeignet und vorhanden.** Nur ein bereitgestelltes, belegtes und freigegebenes Originalzitat verwenden; nie erfinden, zusammensetzen oder umformulieren. Fehlt ein Zitat, nicht automatisch als Mangel behandeln: nur dann als offenen Punkt ausweisen, wenn die Redaktion für das konkrete Format eines benötigt.
7. **Formatbausteine bedingt verwenden.** Bei einer Pressemitteilung Faktenkasten, Boilerplate, Ort/Datum und Ansprechperson nur aus bereitgestellten, aktuellen und freigegebenen Angaben übernehmen. Bei Webnews keinen PM-Faktenkasten oder Boilerplate erzwingen; die passende Struktur aus `referenzen/pm-struktur.md` nutzen. Fehlende Pflichtangaben nur für das angefragte Format als offene Punkte markieren.
8. **Redaktionshinweise.** Bei externen Inhalten auf die Prüfung geltender gesetzlicher, Plattform- und Institutionsvorgaben zur Kennzeichnung hinweisen.
9. **Selbstprüfung** anhand Abschnitt 7 und Übergabe.

## 5. Ausgabeformat

```
Format:              Pressemitteilung / Webnews
Titelvorschlag:      (1 Vorschlag)
Untertitel:          (nur falls für das Format vorgesehen oder angefragt)
Lead:                (1 Absatz, passend zu Format und Quellenlage)
Textkörper:          (Absätze passend zu Format und Umfang; Zwischenüberschriften gemäß `referenzen/pm-struktur.md`.)
Zitat:               (nur falls geeignet, belegt und freigegeben; andernfalls weglassen)
PM-spezifische Bausteine (nur bei Pressemitteilung):
  Faktenkasten:      (nur mit belegten, passenden Angaben; sonst weglassen)
  Boilerplate:       (nur aus aktueller Referenz, unverändert; fehlt sie, offen ausweisen)
  Ansprechperson:    (aus aktuellem freigegebenem Material; fehlende formatrelevante Angaben als offen markieren)
Webnews:             (keinen PM-Faktenkasten oder Boilerplate erzwingen; ggf. passende Kontakt-/Linkangabe nur aus dem Material)
---

Offene Punkte:       (was fehlt, um veröffentlichungsreif zu sein)
Faktencheckliste:    (alle prüfpflichtigen Aussagen)
Redaktionshinweise:  (Kennzeichnung, Bildbedarf, Sperrfristen)
```

## 6. Verbote

- Keine erfundenen Zitate, Personen, Funktionen, Zahlen, Fristen.
- Keine Wertung als „bahnbrechend", „einzigartig", „weltweit erstmals" ohne Beleg.
- Keine Zusagen zu Förderung, Zulassung oder Rechtsfolgen.
- Keine direkte Veröffentlichung, kein Versand.
- Keine Übernahme von Formulierungen aus fremden Pressemitteilungen (Urheberrecht).

## 7. Prüf- und Freigabeschritte

Der Skill schließt mit `faktencheck`-Logik ab. Der Text geht danach in die übliche Freigabekette (Fachbereich, ggf. Leitung, Presse). Der Skill darf keine Freigabe simulieren.

## 8. Referenzdateien

- `referenzen/stil-guide-hochschule.md` — Anrede, Tonalität, Terminologie, Gendern
- `referenzen/pm-struktur.md` — Aufbau, Zeichenrahmen, Boilerplate
- `referenzen/beispiel-pm-1.md` — Vorlage für ein freigegebenes Referenzbeispiel

## 9. Beispiel und Gegenbeispiel

**Beispiel (richtig):**

> Eingabe: Faktenblatt zu einem Verbundprojekt (Förderbetrag, Laufzeit, zwei Partner, ein Zitat der Projektleitung).
> Ausgabe: PM-Entwurf mit Lead, zwei Absätzen, Originalzitat, Faktenkasten; offene Punkte: Ansprechperson im Fachbereich, Freigabe des Partners, Bildmaterial.

**Gegenbeispiel (falsch):**

> Ein fehlendes Zitat wird erfunden und eingefügt. → Verstoß gegen Abschnitt 6. Korrekt: Zitat weglassen; nur dann als offenen Punkt ausweisen, wenn die Redaktion für das konkrete Format ausdrücklich eines benötigt.

---

**Verwandte Skills:** `faktencheck`, `titelvorschlag`, `kanaladaption`, `stil-guard`
