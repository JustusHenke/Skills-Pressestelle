# Skills für die Hochschulkommunikation

14 modulare Agent Skills für wiederkehrende Aufgaben in Hochschulpressestellen. Jeder Skill ist ein eigenständiger Ordner mit `SKILL.md` und – wo nötig – ergänzenden Referenzen oder Skripten.

## Wofür die Sammlung gedacht ist

Pressestellen können die Skills als klar abgegrenzte Arbeitshilfen für wiederkehrende redaktionelle Aufgaben einsetzen. Ein möglicher Ablauf: Themen und eingehende Anfragen vorsortieren, prüfpflichtige Aussagen markieren, aus freigegebenem Material einen PM- oder Webnews-Entwurf erstellen und diesen anschließend für angefragte Kanäle aufbereiten. Weitere Skills unterstützen einzelne Schritte wie Briefings, Titel, Zitatkürzungen, Social Posts, Bildkonzepte, barriereärmere Texte und die Auswertung bereitgestellter Clipping-Daten. Die Krisenampel ordnet eine Lage ein; sie verfasst ausdrücklich keine Krisenstatements.

Die Sammlung ist kein automatischer Veröffentlichungsprozess. Die Skills erstellen Entwürfe, Prüflisten und Vorschläge auf Grundlage der bereitgestellten Inhalte. Sie recherchieren nicht selbstständig, kennen lokale Regeln nur, wenn passende Referenzen hinterlegt sind, und ersetzen weder fachliche Prüfung noch redaktionelle Freigabe. Die Pressestelle entscheidet, welche Schritte passen und was nach Prüfung verwendet wird.

Die Skills liegen im offenen Agent-Skills-Format. Der gemeinsame Quellbestand befindet sich unter `.agents/skills/`; anbieterspezifische Anleitungen und Prompts sind davon getrennt.

Wer keine Skills installieren und keinen Agenten einrichten kann, nutzt die Vorlagen unter [`prompt_templates/`](prompt_templates/README.md): 14 Copy-Paste-Prompts für einen normalen Chat, eins zu eins zu den Skills. Sie brauchen keine Admin-Rechte und keine Vorschaufunktion. Dafür tragen sie ihre Regeln selbst im Prompt — Referenzdateien wie Stil-Guide, Eigennamenliste oder Krisenplan müssen als Material beigelegt werden. Die Vorlagen sind ein Entwurf und noch nicht an echten Pressestellentexten getestet.

## Skills

| Skill | Aufgabe |
|---|---|
| `barrierefrei-text` | Verständlichkeit prüfen, barriereärmere Fassungen und Alternativtexte vorschlagen |
| `bild-prompt` | Bildkonzepte, Generator-Prompts und Alt-Texte erstellen |
| `briefing` | Veranstaltungs- und Interviewbriefings aus freigegebenen Informationen erstellen |
| `clip-report` | bereitgestellte Medienresonanz- oder Clipping-Daten auswerten |
| `faktencheck` | prüfpflichtige Aussagen und Belegstellen systematisch erfassen |
| `kanaladaption` | freigegebene Inhalte für unterschiedliche Kanäle aufbereiten |
| `krisen-ampel` | potenzielle Krisen einordnen und auf Zuständigkeiten verweisen; keine Statements formulieren |
| `nachrichtenwert-vorsortierung` | Themen anhand eines Kriterienkatalogs vergleichen und priorisieren |
| `pm-entwurf` | Rohmaterial in einen Pressemitteilungs- oder Webnews-Entwurf überführen |
| `presseanfrage-triage` | Presseanfragen klassifizieren und Klärungsbedarf ausweisen |
| `social-posts` | freigegebene Inhalte für Social-Media-Kanäle adaptieren |
| `stil-guard` | Texte gegen bereitgestellte Stil- und Terminologieregeln prüfen |
| `titelvorschlag` | Titel-, Teaser- und Hook-Varianten entwickeln |
| `zitat-kuerzung` | Zitate transparent kürzen und mögliche Bedeutungsverschiebungen markieren |

## Plattformen

Die Skills sind **plattformneutral beschrieben**, aber nicht jede Plattform erkennt denselben Repository-Pfad oder bietet dieselben Funktionen. Insbesondere Bildgenerierung und Skriptausführung hängen von den verfügbaren Werkzeugen ab.

| Plattform | Nutzung |
|---|---|
| GitHub Copilot | Skills im Projektpfad `.agents/skills/` ablegen. Unterstützte Erkennungspfade können je nach Copilot-Oberfläche variieren. |
| Gemini CLI | `.agents/skills/` wird als gemeinsamer Skills-Pfad unterstützt. Alternativ ist der Gemini-spezifische Pfad `.gemini/skills/` verfügbar. |
| Claude | Claude Code erkennt Projekt-Skills unter `.claude/skills/<skill-name>/`; Claude-Webprodukte haben eigene Verfügbarkeits- und Importwege. Die gemeinsame Quelle hier bleibt `.agents/skills/`; eine lokale Spiegelung für Claude Code wird unten beschrieben. |
| ChatGPT | Die ChatGPT-Skills-Funktion nutzen, sofern sie für Konto und Workspace verfügbar ist; den produktspezifischen Erstellungs- und Freigabeweg beachten. Dieses Repository wird nicht automatisch als Live-Skill geladen. |
| OpenAI API | Unterstützte Skills als Ordner oder Paket über die Skills-API bereitstellen. API-Nutzung ist von der ChatGPT-Oberfläche zu unterscheiden. |
| Microsoft 365 Copilot Agent Builder | Jeden Skill als ZIP-Paket mit `SKILL.md` im ZIP-Stamm hochladen. Details und Prompts stehen unter [`integrations/microsoft-365-agent-builder/`](integrations/microsoft-365-agent-builder/anleitung_agent_builder.md). |
| Jeder Chat, ohne Installation | Kein Skill und kein Agent nötig: eine Vorlage aus [`prompt_templates/`](prompt_templates/README.md) kopieren, Platzhalter füllen, freigegebenes Material einfügen. Regeln und Referenzen stehen dann nur im Prompt oder im beigelegten Material. |

Die Plattformen entwickeln ihre Skills-Unterstützung weiter. Vor der Einrichtung die aktuelle Dokumentation und die Funktionen des eigenen Kontos oder Tenants prüfen. Claude Code erkennt `.agents/skills/` nicht automatisch. Wenn du die Skills dort nutzen willst, musst du sie nach `.claude/skills/` spiegeln:

```powershell
New-Item -ItemType Directory -Force -Path ".claude/skills" | Out-Null
Get-ChildItem ".agents/skills" -Directory | ForEach-Object {
    Copy-Item $_.FullName -Destination ".claude/skills" -Recurse -Force
}
```

Die Kopien sind eine zweite Fassung und müssen nach Änderungen erneut synchronisiert werden. `.claude/skills/` ist standardmäßig in `.gitignore` ausgeschlossen. Wenn die Projektgruppe die Spiegelung versionieren und pflegen will, den Ignore-Eintrag entfernen und einen Synchronisationsprozess festlegen; andernfalls den lokalen Spiegel nicht einchecken. Für Microsoft 365 Agent Builder und unterstützte OpenAI-Workflows pro Skill ein Paket aus derselben Quelle erstellen.

## Institutionsspezifische Anpassung

Viele Referenzdateien enthalten den Platzhalter `[HOCHSCHULNAME]` oder markierte Vorlagen. Vor produktivem Einsatz:

1. Platzhalter durch geprüfte Institutionsangaben ersetzen.
2. Vorlagen wie Stilregeln, freigegebene Positionen, Zuständigkeiten und Krisenpläne fachlich ausfüllen.
3. Sicherstellen, dass der verwendete Agent die jeweiligen Referenzdateien tatsächlich laden kann.
4. Datenschutz, Rechte, Barrierefreiheit, Freigabewege und lokale Kommunikationsregeln prüfen.

Leere oder nicht freigegebene Referenzen dürfen nicht als verbindliche Hausregeln behandelt werden. Kein Skill veröffentlicht, versendet oder gibt Inhalte frei; die redaktionelle Verantwortung bleibt bei Menschen.

## Lizenz und Wiederverwendung

Dieses Repository steht unter **CC0 1.0 Universal**. Die enthaltenen Materialien dürfen – soweit die Rechte bei den jeweiligen Rechteinhabern liegen – ohne Namensnennung genutzt, bearbeitet, weitergegeben und auch kommerziell verwendet werden. Der vollständige Lizenztext steht in [`LICENSE`](LICENSE) und [online](https://creativecommons.org/publicdomain/zero/1.0/).

CC0 gilt nur für Rechte, die die jeweiligen Rechteinhaber an den Materialien einräumen können. Marken, Patente, Persönlichkeits- und Datenschutzrechte sowie Rechte Dritter werden dadurch nicht automatisch freigegeben. Die Inhalte werden ohne Gewähr bereitgestellt.

## Dokumentation

- [`integrations/microsoft-365-agent-builder/anleitung_agent_builder.md`](integrations/microsoft-365-agent-builder/anleitung_agent_builder.md) – Microsoft-365-spezifische Einrichtung
- [`integrations/microsoft-365-agent-builder/systemprompts/`](integrations/microsoft-365-agent-builder/systemprompts/) – Agent-Anweisungen für diese Integration
- [`prompt_templates/`](prompt_templates/README.md) – 14 Chat-Prompt-Vorlagen ohne Installation, mit README zu Nutzung und Grenzen

## Weiterführende Dokumentation

- [Agent Skills – Spezifikation](https://agentskills.io/specification)
- [GitHub Copilot: Agent Skills](https://docs.github.com/en/copilot/concepts/customizations/agent-skills)
- [Gemini CLI: Agent Skills](https://geminicli.com/docs/cli/skills/)
- [OpenAI: Skills in der API](https://developers.openai.com/api/docs/guides/tools-skills)
- [OpenAI Help Center: Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [Microsoft Learn: Skills in Agent Builder](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-skills)
- [Claude Code: Skills](https://code.claude.com/docs/en/skills)
