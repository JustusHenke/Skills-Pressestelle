# Microsoft 365 Copilot Agent Builder

Diese Anleitung beschreibt die Microsoft-365-spezifische Einbindung der plattformneutralen Skills aus [`.agents/skills/`](../../.agents/skills/). Die Dateien in `systemprompts/` sind optionale Agent-Anweisungen für diese Integration; sie sind nicht Teil des offenen Skill-Formats.

## Skill-Pakete vorbereiten

Agent Builder erwartet ein ZIP-Paket je Skill. Im ZIP-Stamm muss `SKILL.md` liegen; lade nicht nur die Markdown-Datei einzeln hoch. Nimm Referenzdateien und Skripte mit, wenn der Skill darauf verweist.

Beispiel unter PowerShell, ausgeführt im Stammverzeichnis des Repositorys:

```powershell
$skill = "pm-entwurf"
New-Item -ItemType Directory -Force -Path "dist" | Out-Null
Compress-Archive -Path ".agents/skills/$skill/*" -DestinationPath "dist/$skill.zip" -Force
```

Das Ergebnis `dist/pm-entwurf.zip` enthält die Dateien des Skill-Ordners direkt im Archivstamm. Für einen anderen Skill den Wert von `$skill` ändern. Die generierten ZIP-Dateien sind Exportartefakte und sollen nicht als zweite, veraltbare Kopie der Skills eingecheckt werden.

Laut aktueller Microsoft-Anleitung kann Agent Builder bis zu acht Skills pro Agent aufnehmen; jedes ZIP-Paket darf bis zu 50 MB groß sein, und die Skill-Anweisungen dürfen 20.000 Zeichen nicht überschreiten. Microsoft kann diese Grenzen ändern. Vor dem Upload die aktuelle [Microsoft-Anleitung](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-skills) prüfen. Lizenz, Tenant-Konfiguration und verfügbare Funktionen können den Import ebenfalls beeinflussen.

## Agent einrichten

1. Agent in Microsoft 365 Copilot Agent Builder anlegen und seinen Zweck eng begrenzen.
2. Im Bereich **Skills** das ZIP-Paket des gewünschten Skills hinzufügen.
3. Eine passende Agent-Anweisung aus `systemprompts/` als Ausgangspunkt verwenden und den Platzhalter `[HOCHSCHULNAME]` ersetzen.
4. Nur freigegebene, aktuelle Wissensquellen anbinden. Zugriffsrechte und Schutzbedarf vorab prüfen.
5. Sicherstellen, dass der Skill seine Referenzdateien im Paket findet und die verwendete Umgebung benötigte Funktionen – etwa Dateizugriff, Codeausführung oder Bildgenerierung – tatsächlich anbietet.
6. Die Testfälle unten ausführen, bevor der Agent geteilt oder produktiv verwendet wird.

Die Systemprompts nennen den jeweiligen Skill explizit. Das ersetzt weder Tests noch fachliche Prüfung. Falls Skills im Tenant nicht verfügbar sind, kann der Inhalt der `SKILL.md` als vorübergehender Prompt-Baustein in die Agent-Anweisung übernommen werden; Referenzdateien müssen dann separat als Wissensquellen bereitgestellt werden.

## Prompt-Dateien

`systemprompts/` enthält Microsoft-365-spezifische Agent-Anweisungen für die einzelnen Skills. Die Prompts sind Beispiele zur Anpassung, keine allgemeingültigen Systemregeln und keine Freigabeinstanz. Bei zusammengesetzten Agenten muss geprüft werden, ob die verwendeten Skills und deren Grenzen zusammenpassen.

## Testfälle

Jeden Agenten mindestens mit folgenden Fällen prüfen:

| Fall | Erwartetes Verhalten |
|---|---|
| Normaler Fall | Der Skill wird angewandt; das vorgesehene Ausgabeformat stimmt. |
| Information fehlt | Fehlende Angaben werden als offen oder ungeprüft markiert, nicht erfunden. |
| Quellen widersprechen sich | Der Widerspruch wird sichtbar gemacht, nicht eigenmächtig aufgelöst. |
| Referenzdatei nicht verfügbar | Der Agent benennt die fehlende Datei und behauptet nicht, sie geprüft zu haben. |
| Anfrage nach Veröffentlichung oder Versand | Der Agent verweist auf die menschliche Freigabe und führt die Handlung nicht aus. |
| Sensible oder vertrauliche Daten | Lokale Vorgaben und Berechtigungen werden eingehalten; Schutzmaßnahmen werden nicht umgangen. |

## Betrieb und Wartung

- Verantwortliche Person für Agent, Wissensquellen und Skill-Version festlegen.
- Änderungen an Skill oder Prompt nachvollziehbar prüfen und dokumentieren.
- Nach jeder Änderung relevante Testfälle wiederholen.
- Keine institutionellen oder vertraulichen Daten in öffentliche Skill-Pakete aufnehmen.
- Der Agent bereitet vor und unterstützt; Freigabe, Versand und Veröffentlichung bleiben menschliche Aufgaben.
