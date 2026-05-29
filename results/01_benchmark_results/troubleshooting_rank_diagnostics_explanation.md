# Troubleshooting Rank Diagnostics

## Was wurde getestet?

Diese Diagnose erweitert ausgewählte Troubleshooting-Läufe von Top 5 auf Top 20.
Sie wurde erstellt, weil die Top-5-Auswertung zeigte, dass viele Backends zwar
Referenz-Screenshots finden, die passende PDF-Seite aber selten innerhalb der Top
5 erscheint.

Getestet werden dieselben zehn Troubleshooting-Query-Bilder wie in der
Backend-Comparison. Der Unterschied ist, dass pro Query zwanzig statt fünf Treffer
ausgewertet werden.

## Inputs und Outputs

Input ist wieder das jeweilige Fehlersymbol-Query-Bild beziehungsweise bei der
Multimodal-Variante Bild plus fester Hilfetext. Output ist eine Top-20-Liste aus
Referenz-Screenshots und PDF-Seiten.

Die Diagnose zählt zusätzlich, wie viele manuelle Referenz-Screenshots und wie
viele PDF-Seiten in den ersten fünf Treffern liegen. Damit wird sichtbar, ob ein
Backend die Top-5-Liste mit Referenzbildern dominiert und PDF-Seiten erst später
zulässt.

## Ground Truth und optimale Werte

Die Ground Truth ist identisch mit dem Troubleshooting-Backendvergleich:
passender Referenz-Screenshot und passende PDF-Seite. In der Top-20-Diagnose ist
der optimale Wert für `reference_hit_at_20` und `page_hit_at_20` jeweils 1,0.
Zusätzlich wären niedrige durchschnittliche Ränge ideal, insbesondere ein
`avg_reference_rank` nahe 1 und ein `avg_page_rank` nahe 2.

## Metriken

`avg_reference_rank` ist der durchschnittliche Rang des passenden
Referenz-Screenshots über alle zehn Querys. Niedriger ist besser.

`avg_page_rank` ist der durchschnittliche Rang der passenden PDF-Seite. Niedriger
ist besser. Ein Wert deutlich größer als 5 erklärt, warum `page_hit_at_k` in der
Top-5-Auswertung niedrig ist.

`reference_hit_at_20` misst, ob der passende Referenz-Screenshot innerhalb der Top
20 gefunden wurde.

`page_hit_at_20` misst, ob die passende PDF-Seite innerhalb der Top 20 gefunden
wurde.

`avg_manual_reference_count_top5` und `avg_pdf_page_count_top5` beschreiben die
Zusammensetzung der ersten fünf Treffer. Sie zeigen, ob ein Backend vor allem
Referenz-Screenshots oder früh auch PDF-Seiten zurückgibt.
