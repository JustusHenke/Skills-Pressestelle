---
name: krisen-ampel
description: Ordnet ein potenzielles Krisenthema ein — Lage, Betroffenheit, Öffentlichkeitsdruck, Zeitdruck — und benennt die zuständigen Rollen und die einzuhaltende Freigabekette. Formuliert ausdrücklich keine Statements und keine Antworten. Reines Prozesswerkzeug.
---

# Skill: Krisenampel

## 1. Zweck

Dieser Skill ist bewusst kein Textgenerator. Er hilft, eine Lage früh einzuordnen und die richtigen Leute einzuschalten. In Krisen ist die gefährlichste Wirkung von KI ein schnell formulierter, ungeprüfter Satz. Deshalb liefert dieser Skill ausschließlich Einschätzung, Zuständigkeiten und Schritte — keine Formulierungen.

## 2. Einsatzgrenzen

**Nicht geeignet für:** Erstellung von Statements, Posts, Antworten oder Sprachregelungen. Ausdrücklich ausgeschlossen. Ebenso nicht für Rechtsberatung, Personalthemen im Einzelfall, laufende Verfahren.

**Voraussetzung:** Es muss einen aktuellen, institutionell bestätigten Notfall-/Krisenplan der [HOCHSCHULNAME] geben. Ohne ihn darf der Skill keine konkreten Zuständigkeiten oder Kontaktwege vorschlagen; der institutionelle Krisenprozess ist manuell zu nutzen.

**Datenschutz:** Nur erforderliche, möglichst aggregierte und nicht identifizierende Angaben verarbeiten. Namen, Kontaktdaten, Gesundheitsdaten oder andere vertrauliche Details Betroffener nicht in die KI-Umgebung eingeben, sofern dies nicht zwingend erforderlich und durch institutionelle Vorgaben für genau diese Umgebung freigegeben ist. Bei unklarer Zulässigkeit keine Eingabe; manuell nach Krisenplan handeln. Aufbewahrung und Löschung richten sich nach den institutionellen Regeln.

## 3. Eingaben

Erforderlich:

- Sachverhalt in Stichpunkten (was ist bekannt, was nicht)
- Quelle der Information und Zeitpunkt
- Betroffene Gruppen und Umfang, soweit belegt und erforderlich; möglichst aggregiert und ohne Namen oder andere identifizierende Details
- Bekannter Öffentlichkeitsdruck (Anfragen, Social Media, Presse)
- Geltender Krisenplan / Zuständigkeitsliste

## 4. Verbindliche Schritte

1. **Faktenlage trennen.** Bekannt / unbekannt / strittig. Nichts ergänzen.
2. **Ampel setzen.** Grün (Routine), Gelb (Beobachtung), Rot (Krise), mit Begründung aus Kriterien.
3. **Betroffenheit beschreiben.** Nur belegte, erforderliche Angaben verwenden, möglichst aggregiert. Keine Einzelfall- oder Rechtsbewertung und keine Ableitung individueller Rechte oder Pflichten; offene Schutz- oder Rechtsfragen als Prüfauftrag an die zuständige menschliche Stelle markieren.
4. **Öffentlichkeitsdruck einschätzen.** Presseanfragen, Social-Media-Reaktionen, drohende Berichterstattung.
5. **Zeitdruck.** Wie schnell ist eine Reaktion erwartet — und ist sie überhaupt nötig?
6. **Rollen benennen.** Zuständigkeiten und Kontaktwege ausschließlich aus dem aktuellen, institutionell bestätigten Krisenplan übernehmen. Keine Personen, Kontaktdaten oder Zuständigkeiten ergänzen oder erraten. Fehlen Angaben, als ungeklärt markieren und auf den manuellen Krisenprozess verweisen.
7. **Schritte auflisten.** Reihenfolge, Zuständigkeit, Fristen.
8. **Ausdrücklich festhalten:** keine Statements durch diesen Skill.

## 5. Ausgabeformat

```
Sachverhalt (bekannt):      …
Unbekannt / strittig:       …
Ampel:                      Grün / Gelb / Rot
Begründung:                 (aus Kriterien)

Betroffenheit:              (belegter, möglichst aggregierter Umfang; keine Einzelfall- oder Rechtsbewertung)
Öffentlichkeitsdruck:       (Anfragen, Social, Presse)
Zeitdruck:                  (Einschätzung)

Rollen:
| Rolle | zuständige Stelle laut Krisenplan | Aufgabe | bestätigter institutioneller Kontaktweg laut Krisenplan |

Nächste Schritte:
[ ] … (Zuständig, Frist)

Hinweis: Dieser Skill formuliert keine Aussagen. Statements nur über die Krisenfreigabe.
```

## 6. Verbote

- Keine Formulierung von Statements, Antworten, Posts, Sprachregelungen.
- Keine Rechtsbewertung, keine Schuldzuweisung.
- Keine Weitergabe, kein Versand.
- Keine Einschätzung zu Personen im Einzelfall.
- Keine Aussage „die Lage ist entspannt", wenn Fakten fehlen.

## 7. Prüf- und Freigabeschritte

Der Skill ist ein Frühwarnwerkzeug. Ab Ampel „Gelb" übernimmt der menschliche Krisenprozess. Ab „Rot" ist der Skill beendet.

## 8. Referenzdateien

- `referenzen/krisenplan-hochschule.md` — Rollen, Kette, Erreichbarkeit
- `referenzen/risikokriterien.md`
- `referenzen/ampel-kriterien.md`

## 9. Beispiel und Gegenbeispiel

**Beispiel (richtig):**

> Vorwurf in einem Blogbeitrag, noch keine Presseanfrage. Ausgabe: Ampel Gelb, Betroffenheit mittel, Rollen: Leitung, Pressestelle, Justiziariat; Schritt: Lage prüfen, keine Reaktion vorab; ausdrücklich kein Statement durch den Skill.

**Gegenbeispiel (falsch):**

> Skill schreibt „Wir bedauern die Vorfälle und prüfen den Sachverhalt" als Statement. → genau das, was dieser Skill verhindern soll. Verboten.

---

**Verwandte Skills:** `presseanfrage-triage`, `briefing`, `faktencheck`
