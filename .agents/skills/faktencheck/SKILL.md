---
name: faktencheck
description: Prüft einen Textentwurf auf prüfpflichtige Aussagen — Namen, Zahlen, Daten, Zitate, Fristen, Zuständigkeiten — und verlangt für jede davon eine Belegstelle. Einsetzen, bevor ein Entwurf in die Freigabe geht. Erstellt selbst keine Inhalte und korrigiert nichts stillschweigend.
---

# Skill: Faktencheck

## 1. Zweck

Dieser Skill ist die Bremse vor der Freigabe. Er prüft **nicht**, ob ein Text gut ist. Er prüft, ob jede überprüfbare Aussage eine Quelle hat. Er produziert keine neue Formulierung und ändert den Text nicht.

Der Skill macht Faktentreue zu einem festen Arbeitsschritt: Jede prüfbare Aussage wird einer Belegstelle zugeordnet oder ausdrücklich als ungeprüft markiert.

## 2. Einsatzgrenzen

**Nicht geeignet für:** Krisen- und Rechtsfragen, vertrauliche, nicht öffentliche oder sensible personenbezogene Inhalte sowie die Prüfung von Bildinhalten. Namen und Funktionen in zur Veröffentlichung vorgesehenen Texten können geprüft werden, wenn eine einschlägige, institutionell freigegebene Quelle vorliegt und die Verarbeitung nach den geltenden institutionellen Vorgaben zulässig ist. In anderen Fällen greift die Freigabekette der [HOCHSCHULNAME], nicht dieser Skill.

**Kein Ersatz für:** fachliche Prüfung durch Verantwortliche. Der Skill liefert eine Prüfliste, keine Freigabe.

## 3. Eingaben

Erforderlich:

- Textentwurf (Pressemitteilung, Webnews, Post, FAQ, Briefing)
- Belegquellen: Originaldokumente, Datenblätter, Freigabenotizen, Kontaktangaben — soweit vorhanden
- Geltende Versionen (Datum/Stand), falls mehrere Fassungen existieren

Falls keine Quellen vorliegen: Der Skill arbeitet dann als **Prüflisten-Generator** und markiert alles als ungeprüft. Er erfindet keine Belege.

## 4. Verbindliche Schritte

1. **Aussagen isolieren.** Jeden Satz in einzeln prüfbare Aussagen zerlegen. Mehrere Fakten in einem Satz werden getrennt geführt.
2. **Kategorisieren.** Jede Aussage einer Kategorie zuordnen: Eigenname, Zahl/Menge, Datum/Frist, Zitat, Zuständigkeit/Rolle, Ortsangabe, Förderangabe, Ranglistenplatz, Rechtsbezug, Sonstiges.
3. **Beleg suchen.** Für jede Aussage die Belegstelle suchen. Nur zulässig: Primärquelle, freigegebenes Dokument, ausdrückliche Auskunft. Nicht zulässig: Plausibilität, Ähnlichkeit zu anderen Fällen, Modellwissen.
4. **Status vergeben.** Pro Aussage genau einen Status aus dem Referenzkatalog `referenzen/pruefpflichtige-kategorien.md` verwenden:
   - `belegt` — Quelle und Fundstelle vorhanden, deckt die Aussage vollständig
   - `teilbelegt` — Quelle vorhanden, deckt nur einen Teil oder ist ungenau
   - `ungeprüft` — keine geeignete Quelle gefunden oder keine Fundstelle ermittelbar
   - `zurückgewiesen` — eine geeignete Quelle widerspricht der Aussage. Widerspruch und Fundstelle nennen; nicht eigenständig korrigieren oder entscheiden.
5. **Abweichungen prüfen.** Zahl im Text gegen Zahl in der Quelle, Name gegen Schreibweise, Datum gegen Kalender, Zitat gegen Originalwortlaut (auch Kürzungen: markieren, wo gekürzt wurde).
6. **Widersprüche melden.** Wenn zwei Quellen abweichen, beide Werte mit Fundstelle nennen. Nicht selbst entscheiden.
7. **Tabelle ausgeben** (siehe Abschnitt 5) und mit der Prüfliste für die Redaktion abschließen.

## 5. Ausgabeformat

Immer genau diese Tabelle, danach der Block „Prüfliste":

| Nr. | Aussage (wörtlich) | Kategorie | Status | Beleg / Fundstelle | Handlungsbedarf |
|---|---|---|---|---|---|
| 1 | … | Zahl | belegt | Datenblatt 2026-03, S. 4 | — |
| 2 | … | Zitat | ungeprüft | — | Originalzitat anfordern |

Anschließend:

```
Prüfliste Redaktion:
[ ] Alle „ungeprüft" und „teilbelegt" an der Quelle geklärt
[ ] Alle „zurückgewiesen" mit Fachstelle/Redaktion geklärt; keine stille Korrektur erfolgt
[ ] Zitat-Wortlaut mit der aussagenden Person abgeglichen
[ ] Fristen und Zuständigkeiten bestätigt
[ ] Kennzeichnung nach geltenden gesetzlichen, Plattform- und Institutionsvorgaben geprüft (falls nach außen)
[ ] Freigabe durch verantwortliche Person eingeholt
```

## 6. Verbote

- Keine erfundenen oder „wahrscheinlich richtigen" Belege.
- Keine stillen Korrekturen. Änderungen am Wortlaut werden immer vorgeschlagen, nie eingebaut.
- Keine Bewertung, ob ein Zitat politisch opportun ist.
- Keine Prüfung von Personen-, Personal- oder Rechtsfragen.
- Keine Zusage „geprüft" für etwas, das nur plausibel klingt.

## 7. Übergabe an Menschen

Der Skill liefert eine prüfpflichtige Liste. Die Entscheidung, was veröffentlicht wird, trifft die verantwortliche Person in der Pressestelle.

## 8. Referenzdateien

- `referenzen/pruefpflichtige-kategorien.md` — Kategorienkatalog mit Beispielen
- `referenzen/beleg-quellen-hochschule.md` — welche Quellen zulässig sind (von der [HOCHSCHULNAME] zu füllen)

## 9. Beispiel und Gegenbeispiel

**Beispiel (richtig):**

> Eingabe: „Die [HOCHSCHULNAME] erhält 2,4 Mio. Euro vom BMBF für das Projekt X."
> Ausgabe: Aussage 1 „2,4 Mio. Euro" → Zahl → `belegt` (Zuwendungsbescheid vom …); Aussage 2 „BMBF" → Fördergeber → `belegt`; Aussage 3 „Projekt X" → Eigenname → `belegt`. Hinweis: Betragsweise auf zwei Stellen gerundet, Original 2.391.000 Euro — Freigabe klären, ob gerundet kommuniziert wird.

**Gegenbeispiel (falsch):**

> Eingabe ohne Quellen, Ausgabe behauptet „belegt" mit erfundener Fundstelle „Pressemitteilung Nr. 42". → Verstoß gegen Abschnitt 6.

---

**Verwandte Skills:** `pm-entwurf`, `stil-guard`, `zitat-kuerzung`
