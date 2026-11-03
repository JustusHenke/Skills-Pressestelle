---
name: nachrichtenwert-vorsortierung
description: Bewertet eine Sammlung eingehender Meldungen, Rohmaterialien oder Themenvorschläge nach einem Nachrichtenfaktor-Katalog und schlägt eine Rangfolge vor. Reine Bewertung, keine Feed-Anbindung. Trifft keine Themenentscheidung und erfindet keine Fakten.
---

# Skill: Nachrichtenwert vorsortieren

## 1. Zweck

Nicht jede Meldung ist eine Nachricht. Dieser Skill bewertet Stapel von Rohmaterial — eingehende PM von außen, Forschungsmeldungen, Terminhinweise, Themenvorschläge — nach einem Kriterienkatalog und schlägt eine Rangfolge vor. Die Redaktion entscheidet.

Der Skill bewertet vorhandenes Material. Er zieht nichts aus einem Feed oder Postfach. Für eine laufende Anbindung an Mailsystem oder Feeds ist ein eigener technischer Schritt nötig (siehe Abschnitt 7).

## 2. Einsatzgrenzen

**Nicht geeignet für:** Krisenmeldungen — diese gehen direkt in die Freigabekette. Ebenso nicht für Rechts-, Personal- und Vertragsthemen.

**Grenze:** Nachrichtenwert ist keine Eigenschaft, die ein Text „hat". Er entsteht aus Kriterien und Zielgruppe. Der Skill macht die Kriterien offen, statt ein Urteil zu setzen.

## 3. Eingaben

Erforderlich:

- Liste oder Sammlung von Rohmaterialien (Titel, Text, Quelle, Datum)
- Zielgruppe(n) der Pressestelle
- Kriterienkatalog (Abschnitt 4) oder eigene Gewichtung
- Optional: verfügbare Bildmaterialien
- Optional: geplanter Kanal und Zeitraum

## 4. Kriterienkatalog für eine Hochschule

Der Katalog ist eine redaktionelle Prüfliste, keine allgemeingültige Messung. Eine Einzelbewertung je Kriterium (z. B. 0–3) ist optional und von einem lokal vereinbarten Gewicht zu unterscheiden. Die konkrete Skala und Gewichtung müssen vorab institutionell festgelegt sein; ohne diese Grundlage keine Gesamtpunktzahl berechnen. Krisen- oder Rechtsrisiken dienen als Ausschluss-/Eskalationssignal, nicht als gewichteter Rankingfaktor.

| Kriterium | Prüffrage | optionale redaktionelle Bewertung (nicht objektiv) |
|---|---|---|
| Neuheit | Ist es neu, oder wird Bekanntes wiederholt? | z. B. 0–3 oder qualitativ |
| Anlass | Gibt es einen konkreten Anlass (Berufung, Abschluss, Förderung, Meilenstein)? | z. B. 0–3 oder qualitativ |
| Drittmittel / Förderung | Geht es um eingeworbene Mittel oder Förderzusagen? | z. B. 0–3 oder qualitativ |
| Anwendungsnähe | Ist ein belegter Praxisbezug oder ein Bezug zum lokal definierten Hochschulprofil erkennbar? | z. B. 0–3, qualitativ oder nicht beurteilbar |
| Anschlussfähigkeit | Berührt es Politik, Gesellschaft, Gesundheit, Klima? | z. B. 0–3 oder qualitativ |
| Personenbezug | Geht es um Personen (Auszeichnung, Amt, Berufung)? | z. B. 0–3 oder qualitativ |
| Zahl / Größe | Enthält es belastbare Zahlen (Mittel, Reichweite, Studierendenzahl)? | z. B. 0–3 oder qualitativ |
| Überraschung | Weicht es von den Erwartungen ab? | z. B. 0–3 oder qualitativ |
| Bildverfügbarkeit | Gibt es brauchbares Bildmaterial? | z. B. 0–3 oder qualitativ |
| Erhebliches Risiko / Krisenpotenzial | Liegt nach dem lokal bestätigten Kriterienkatalog ein erhebliches Krisen-, Rechts- oder Reputationsrisiko vor? | ja / nein / unklar; bei ja oder unklar nicht ranken, bestätigten Eskalationsweg nutzen |

Die Kriterien und Gewichte sind lokal festzulegen; kein Kriterienkatalog gilt für alle Hochschulen. Bei vereinbarter Gewichtung die aktuelle Referenz `referenzen/kriterien-gewichtung-hochschule.md` verwenden. Jeden Wert mit einem Beleg aus dem bereitgestellten Material begründen. Ist die Grundlage zu dünn, „nicht beurteilbar“ statt 0 vergeben. Ohne lokal abgestimmte Gewichtung keine scheinpräzise Gesamtpunktzahl als objektiven Nachrichtenwert ausgeben; Ergebnisse sind nur eine transparente, redaktionelle Orientierung innerhalb dieses Stapels und nicht zwischen unterschiedlich konfigurierten Stapeln vergleichbar.

## 5. Ausgabeformat

| Vorschlagsrang innerhalb dieses Stapels | Rohmaterial | Quelle | Anlass | Kriterienwerte und Belege (Gewichte nennen, falls lokal festgelegt) | Risiko | Redaktioneller Vorschlag |
|---:|---|---|---|---|---|---|

Danach:

```
Beobachtungen:      (Themen, die gehäuft auftreten; Lücken im Stapel)
Nicht bewertet:     (Material ohne ausreichende Informationen)
Nicht priorisiert / ausgeschlossen: (Material, das im vorliegenden Stapel nicht priorisiert wird, mit Begründung; keine definitive Aussage über Nachrichtenwert)
Hinweis an Redaktion: Die Rangfolge ist ein Vorschlag, keine Entscheidung.
```

## 6. Verbote

- Keine erfundenen Fakten, Zahlen oder Anlässe.
- Keine Themenentscheidung. Nur Bewertung und Vorschlag.
- Keine Priorisierung von Krisenmaterial — das geht an die Freigabekette.
- Keine politische Bewertung, keine Positionierung.
- Keine Veröffentlichung, keine Weiterleitung.

## 7. Ausbaustufe (Feed-Anbindung)

Eine laufende Vorsortierung eingehender Mails oder Feeds erfordert Technik außerhalb dieses Skills: Mailregel, Power-Automate-Flow, Skript. Das ist ein eigenes Vorhaben mit IT, Datenschutz und Zuständigkeitsklärung. Der Skill liefert dann nur die Bewertungslogik.

## 8. Referenzdateien

- `referenzen/nachrichtenfaktoren.md` — Katalog mit Beispielen
- `referenzen/kriterien-gewichtung-hochschule.md` — von der [HOCHSCHULNAME] abzustimmen
- `referenzen/stil-guide-hochschule.md`

## 9. Beispiel und Gegenbeispiel

**Beispiel (richtig):**

> Stapel mit 12 eingehenden Meldungen und lokal freigegebener Kriteriengewichtung → begründete Rangfolge innerhalb dieses Stapels. Eine Meldung mit Krisen- oder Rechtsrisiko wird nicht bewertet, sondern als „an Freigabekette — nicht priorisieren“ markiert. Ohne abgestimmte Gewichtung keine Gesamtpunktzahl ausgeben.

**Gegenbeispiel (falsch):**

> Skill entscheidet „Diese Meldung wird heute veröffentlicht" → Überschreitung. Der Skill priorisiert nur.

---

**Verwandte Skills:** `presseanfrage-triage`, `clip-report`, `pm-entwurf`, `briefing`
