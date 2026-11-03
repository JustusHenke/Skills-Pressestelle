---
name: social-posts
description: Erzeugt aus einer freigegebenen Pressemitteilung oder Webnews einen oder mehrere Social-Media-Posts je angefragter Plattform, mit optionalen Hook-Alternativen, Zeichenangaben, Hashtag-Vorschlägen und Bild-/Alternativtext-Bedarf. Verändert keine Zahlen und weist auf offene Kennzeichnungsprüfungen hin.
---

# Skill: Social-Media-Posts

## 1. Zweck

Pressemitteilungen sind nicht automatisch plattformfähig. Dieser Skill erstellt für die angefragten Plattformen jeweils einen oder mehrere Posts, ohne die Faktenbasis zu verlassen.

## 2. Einsatzgrenzen

**Nicht geeignet für:** Krisenposts, Kommentare zu laufenden Debatten, Antworten auf Nutzerkommentare (das gehört in die Community-Betreuung). Keine Posts zu Personalangelegenheiten.

**Wichtig:** Ein Post darf den Inhalt zuspitzen, aber nicht verfälschen. Der Skill weist aus, wo zugespitzt wird.

## 3. Eingaben

Erforderlich:

- freigegebene PM/Webnews (Quelle, Stand)
- angefragte Plattformen
- Zielgruppe je Plattform
- Optional: Bildmaterial, Link, Sperrfrist
- Optional: Plattformregeln aus `referenzen/kanal-rahmen.md`

## 4. Verbindliche Schritte

1. **Kernbotschaft bestimmen.** Was ist die eine Aussage, die hängen bleiben soll?
2. **Hook bauen.** Erste Zeile je Plattform — sie entscheidet über die Anzeige „weiterlesen".
3. **Post formulieren.** Ton je Plattform, Länge je Zeichenrahmen, Link setzen.
4. **Hashtags.** Nur naheliegende, keine aufgeblähten Sets. Vorschlag mit Begründung.
5. **Bild und Alternativtext.** Bildidee als Vorschlag kennzeichnen. Einen Alternativtext nur für ein vorliegendes/final ausgewähltes informatives Bild entwerfen und an dessen tatsächlichem Inhalt und Funktion ausrichten; für ein nicht vorhandenes Bild keinen fertigen Alt-Text behaupten. Bei synthetischen Bildern Kennzeichnungsstatus samt konkreter Grundlage und Stand prüfen oder als offen markieren.
6. **Optionale Varianten.** Hook-Varianten nur in der angefragten Zahl erstellen; ohne Mengenwunsch genügt eine passende Fassung, bei erkennbarem redaktionellem Nutzen können wenige Alternativen vorgeschlagen werden. Sie sind Textvorschläge, kein durchgeführter A/B-Test und kein Nachweis, dass die Plattform einen Test unterstützt. Einen tatsächlichen Test darf nur die Redaktion nach Prüfung von Plattformfunktion, Testaufbau und institutioneller Freigabe planen und durchführen.
7. **Prüfung.** Keine erfundenen Zahlen oder unbelegten Aussagen. Kennzeichnung je Plattform nur anhand konkret bereitgestellter oder nachweislich aktuell geprüfter Rechts-, Plattform- und Institutionsvorgaben beurteilen. Grundlage und Stand nennen. Status als „nicht relevant“ (begründen), „geprüft“ (Ergebnis, Quelle und Stand), „erforderlich“ (Fundstelle und Vorgabe) oder „offen“ (Grundlage fehlt/unklar) ausweisen. Ohne belastbare Grundlage keine Pflicht behaupten.

## 5. Ausgabeformat

| Plattform | Hook / optionale Alternativen (Textvorschläge) | Posttext | Zeichen Posttext (Istwert) | Zeichenrahmen (falls vorgegeben: Quelle/Stand) | Hashtags | Bildfunktion / Alternativtext zum finalen Bild |
|---|---|---|---:|---|---|---|
|---|---|---|---|---|---|---|

Danach:

```
Nicht verwendet: (relevante Fakten oder Nuancen, die im Post fehlen; einen anderen Zielkanal nur nennen, wenn angefragt)

Kennzeichnungsstatus je Plattform: nicht relevant / geprüft / erforderlich / offen
Grundlage und Stand je Plattform: konkrete Vorgabe/Fundstelle oder Grund für „offen“ bzw. „nicht relevant“
Sperrfristen: (falls zutreffend)
```

## 6. Verbote

- Keine erfundenen Zahlen, Namen, Zitate.
- Keine Übertreibung, die der Basistext nicht deckt („Sensation", „Durchbruch").
- Keine Nutzung fremder Bildrechte.
- Keine Veröffentlichung, kein Scheduling.
- Keine Antworten auf Kommentare.

## 7. Prüf- und Freigabeschritte

Posts gehen in die redaktionelle Freigabe. Bei synthetischen Bildern den Kennzeichnungsstatus anhand konkret bereitgestellter oder nachweislich aktuell geprüfter Vorgaben belegen; Grundlage und Stand dokumentieren. Fehlt die Grundlage, Status „offen“ ausweisen und keine Kennzeichnungspflicht behaupten. Der Skill plant nichts und veröffentlicht nichts.

## 8. Referenzdateien

- `referenzen/kanal-rahmen.md` — Zeichenlimits, Plattform-Tonalitäten
- `referenzen/stil-guide-hochschule.md`
- `referenzen/verbotsliste.md`

## 9. Beispiel und Gegenbeispiel

**Beispiel (richtig):**

> PM zu Studienstart → LinkedIn: fachlicher Einstieg mit Zahl; Instagram: kurzer Hook, motivnah, Link in Bio; Newsletter: Teaser mit Verweis. Jeweils ein Hook-Vorschlag; Alternativen nur auf Wunsch oder bei erkennbarem Mehrwert. Hashtags mit Begründung; keine tatsächlichen Tests.

**Gegenbeispiel (falsch):**

> „Jetzt bewerben, sonst ist es zu spät!" — künstlicher Zeitdruck ohne belegte Frist. → verworfen.

---

**Verwandte Skills:** `kanaladaption`, `titelvorschlag`, `zitat-kuerzung`, `bild-prompt`
