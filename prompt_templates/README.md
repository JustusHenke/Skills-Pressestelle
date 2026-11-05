---
typ: README
titel: Prompt-Vorlagen ohne Installation
projekt: Skills Pressestelle
stand: 2026-11-04
---

# Prompt-Vorlagen für den normalen Chat

Für Pressestellen, die keine Skills installieren und keine Agenten einrichten können. Das kommt in der Praxis oft vor: kein Admin-Recht im Tenant, keine Freigabe für Vorschaufunktionen, nur ein Browser-Chat, oder schlicht ein Workshop-Raum, in dem niemand etwas einrichten soll. Die Custom-Skills-Funktion in Microsoft 365 Agent Builder ist laut Microsoft-Dokumentation Preview und an das Frontier Program gebunden; die eigene README des Repositorys weist außerdem darauf hin, dass ChatGPT ein solches Repository nicht automatisch als Live-Skill lädt. Wer in dieser Lage trotzdem strukturiert arbeiten will, kopiert einen Prompt.

`prompt_vorlagen_pressestelle.md` enthält 14 Vorlagen, eins zu eins zu den 14 Skills unter `../.agents/skills/`. Sie bilden denselben Arbeitsablauf ab: Themen sichten, Anfragen sortieren, Briefing, Entwurf, Titel, Fakten, Zitate, Stil, Verständlichkeit, Kanäle, Social, Bild, Clipping, Krisenampel.

Jede Vorlage trägt eine Golden Rule: einen Merksatz, der in einem Satz festlegt, was die KI tut und was die Redaktion behält. Die Regeln stehen zwischen Beschreibung und Prompt-Block und dienen als Rahmen für die Arbeitsteilung — nicht als Teil des kopierten Prompts.

## So geht es

1. Passende Vorlage aus `prompt_vorlagen_pressestelle.md` kopieren.
2. Platzhalter in eckigen Klammern ersetzen, insbesondere `[HOCHSCHULNAME]`, Kanal, Zielgruppe und Format.
3. Das freigegebene Material direkt unter `-- MATERIAL --` einfügen. Ohne Material liefern die meisten Vorlagen nur eine Struktur mit offenen Punkten — so sind sie gebaut.
4. Antwort lesen, Belege gegen die Originale prüfen, in die redaktionelle Freigabe geben.

Ein Prompt gilt für einen Durchgang. Bei einem neuen Text den Prompt neu kopieren, nicht im alten Verlauf weiterschreiben: sonst vermischen sich Material und Prüflisten aus zwei Aufgaben.

## Die drei Wege im Vergleich

| Weg | Was nötig ist | Was die KI an Regeln hat |
|---|---|---|
| Skill (`../.agents/skills/`) | Erkennungspfad im Agenten, z. B. `.agents/skills/` | `SKILL.md` plus Referenzdateien und Skripte |
| Agent Builder (`../integrations/microsoft-365-agent-builder/`) | Lizenz, Tenant-Freigabe, ZIP-Paket je Skill, Agenten-Anweisung | Systemprompt plus geladene Skills und angebundene Quellen |
| Chat-Vorlage (dieser Ordner) | ein freigegebener Chat | genau das, was im kopierten Prompt steht |

Der dritte Weg ist der einzige, der ohne Einrichtung funktioniert. Er ist auch der anfälligste: Ein Skill kann `referenzen/stil-guide-hochschule.md` oder `referenzen/pruefpflichtige-kategorien.md` laden; ein Chat kennt diese Dateien nicht. Alles, was die Antwort können soll, muss im Prompt stehen oder als Material beiliegen. Wer die Hausregeln braucht, fügt sie selbst unter `-- MATERIAL --` ein. Das ist der Preis für die Einfachheit, keine Kleinigkeit.

Lizenz wie das Repository: CC0 1.0 Universal, siehe `../LICENSE`. Dateinamen folgen der Workbench-Konvention mit Unterstrichen; die Skill-Ordner unter `../.agents/skills/` verwenden Bindestriche. Das ist eine bewusste Uneinheitlichkeit zugunsten der übergeordneten Ablagekonvention.
