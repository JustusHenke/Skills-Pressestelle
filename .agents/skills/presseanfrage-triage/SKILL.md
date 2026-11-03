---
name: presseanfrage-triage
description: Klassifiziert eingehende Presseanfragen nach Thema, Deadline, Risikograd und Zuständigkeit und schlägt Antwortbausteine aus freigegebenen Positionen vor. Beantwortet nichts selbst und leitet nichts weiter.
---

# Skill: Presseanfrage-Triage

## 1. Zweck

Presseanfragen kommen schnell und zu allem. Dieser Skill sortiert sie: Was ist die Frage, wie dringend, wie heikel, wer ist zuständig, was darf geantwortet werden. Er bereitet vor, er antwortet nicht.

## 2. Einsatzgrenzen

**Nicht geeignet für:** Krisenanfragen, Interviewzusagen oder Terminabsprachen. Bei Krisenhinweisen die inhaltliche Triage beenden und nach dem institutionell bestätigten Krisenprozess handeln; der Skill leitet nichts weiter und kontaktiert niemanden.

**Datenschutz:** Nur erforderliche Angaben verarbeiten. Vor Eingabe prüfen, ob die verwendete KI-Umgebung nach den institutionellen Vorgaben für Anfrageinhalte zugelassen ist. Nicht benötigte Namen, E-Mail-Adressen, Telefonnummern, Signaturen und vertrauliche oder sensible Details vorab entfernen oder anonymisieren. Ist die Zulässigkeit unklar, Anfrage nicht eingeben und manuell nach lokalem Verfahren bearbeiten. Keine eigenständige Ablage oder Weitergabe; Aufbewahrung und Löschung richten sich nach den institutionellen Regeln.

**Grenze:** Der Skill arbeitet nur mit dem bereitgestellten, für die Verarbeitung freigegebenen Anfrageauszug. Er kennt keine internen Vorgänge, die nicht mitgeliefert sind.

## 3. Eingaben

Erforderlich:

- Erforderlicher Auszug der Anfrage (Mail, Nachricht, Anrufnotiz); nicht benötigte personenbezogene oder vertrauliche Angaben vorher entfernen
- Medium/Redaktion; Name oder Kontakt der anfragenden Person nur, wenn für Einordnung, Frist oder einen späteren Kontakt erforderlich
- Deadline
- Optional: freigegebene Positionen, frühere Antworten, Zuständigkeitsliste
- Optional: Zuständigkeitsliste Fachbereiche

## 4. Verbindliche Schritte

1. **Kernfrage isolieren.** Was will die anfragende Person wirklich wissen? Oft mehrere Fragen — trennen.
2. **Klassifizieren.** Kategorien: Faktenabfrage, Stellungnahme, Interviewwunsch, Recherche mit Vorwurf, Bildmaterial, Expertenvermittlung, Krisenthema.
3. **Risikograd.** Vorläufig einschätzen: niedrig / mittel / hoch / kritisch; Begründung nennen. Bei „hoch" oder „kritisch" keine inhaltliche Bearbeitung und keine Antwortbausteine erstellen. Nur den in einer aktuellen, freigegebenen Zuständigkeitsliste festgelegten internen Eskalationsweg als Vorschlag nennen. Fehlt er, „Eskalationsweg ungeklärt" ausgeben. Das ist keine tatsächliche Weiterleitung.
4. **Zuständigkeit.** Eine fachlich zuständige Stelle nur nennen, wenn sie in der bereitgestellten, aktuellen Zuständigkeitsliste steht; sonst „Zuständigkeit unklar — Klärung nötig" ausgeben.
5. **Interne Antwortvorschläge.** Nur einschlägige Auszüge aus freigegebenen Positionen verwenden und Quelle, Stand und Freigabestatus nennen. Nichts ergänzen. Als interne Arbeitsgrundlage kennzeichnen, nicht als versandfertige Antwort. Fehlt eine freigegebene Position: „nicht freigegeben — Rücksprache".
6. **Deadline prüfen.** Realistisch? Wenn nicht, allenfalls eine interne Option für eine Zwischennachricht vorschlagen. Keine Nachricht versenden oder als freigegeben darstellen; keine nicht autorisierte Sachauskunft oder Zusage formulieren.
7. **Bericht ausgeben** (Abschnitt 5).

## 5. Ausgabeformat

```
Eingang:        (Zeitpunkt, falls erforderlich) | Medium/Redaktion: … | Ansprechperson: (nur falls erforderlich, sonst anonymisiert) | Deadline: …

Kernfragen:
| Nr. | Frage | Kategorie | Freigabestatus |

Einschätzung:
| Risikograd | Begründung | Zuständigkeit |

Antwortbausteine (nur bei niedrigem oder mittlerem Risiko; bei hohem/kritischem Risiko keine inhaltlichen Bausteine erstellen):
| Frage | interner Vorschlag aus freigegebener Position | Quelle, Stand und Freigabestatus | Fehlt / offen |

Empfohlene interne nächste Schritte (nur Vorschläge; keine Ausführung oder Weiterleitung):
[ ] … (Zuständige Stelle laut Referenz, Frist)
```

## 6. Verbote

- Keine Antwort an Journalist:innen. Kein Versand.
- Keine erfundenen Zuständigkeiten oder Positionen.
- Keine eigene Einschätzung von Rechtsfragen.
- Keine Weiterleitung an Dritte ohne Freigabe.
- Keine Weitergabe von Informationen über laufende Verfahren.

## 7. Prüf- und Freigabeschritte

Der Skill erzeugt eine Vorlage. Die Antwort verantwortet die Pressestelle. Krisen- und Rechtsthemen gehen an die Freigabekette.

## 8. Referenzdateien

- `referenzen/zustaendigkeiten.md` — wer antwortet wozu
- `referenzen/freigegebene-positionen.md`
- `referenzen/risikokriterien.md`

## 9. Beispiel und Gegenbeispiel

**Beispiel (richtig):**

> Anfrage zur Studienplatzvergabe mit Deadline in 3 Stunden → Kategorie „Faktenabfrage", Risikograd „mittel", Zuständigkeit „Studierendenservice"; Baustein aus freigegebener FAQ, offener Punkt markiert.

**Gegenbeispiel (falsch):**

> Skill formuliert eine Antwort und sendet sie. → verboten. Keine Kommunikation nach außen.

---

**Verwandte Skills:** `nachrichtenwert-vorsortierung`, `briefing`, `krisen-ampel`
