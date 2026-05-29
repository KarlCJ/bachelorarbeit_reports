# Pfad C/D PDF-Seitenretrieval

## Was wurde getestet?

Diese Tabelle vergleicht Pfad C und Pfad D in den PDF-Szenarien 1 und 2. Beide
Pfade arbeiten nicht mit Docling-Chunks, sondern mit vollständig gerasterten
PDF-Seiten als Retrieval-Einheiten. Damit ist der Output jedes Treffers eine
konkrete PDF-Seite.

Pfad C verwendet ColQwen2 mit Qdrant-MaxSim-Multivektoren. Jede Seite wird als
Matrix lokaler visueller Tokenvektoren gespeichert. Pfad D verwendet
Single-Vector-Backends: Gemini Embedding 2 als gehostetes multimodales
Embedding-Modell und VDR-2B-Multi als lokales Modell. Jede Seite wird dort zu
einem einzelnen dichten Vektor verdichtet.

Szenario 1 enthält ausschließlich die beiden Primärdokumente. Szenario 2 enthält
zusätzlich ein großes thematisch irrelevantes Noise-PDF. Szenario 2 misst daher,
ob die Seitenretrieval-Backends die relevante Seite auch dann weit oben ranken,
wenn viele irrelevante Seiten im Suchraum liegen.

## Inputs und Outputs

Input ist jeweils eine fachliche Textfrage aus dem Benchmark-Manifest. Pro
Szenario wurden zwölf Text-Queries verwendet. Die Fragen beziehen sich auf
Fließtext, Spezifikationstabellen, Prozessdiagramme, Kreis- und Balkendiagramme
sowie handschriftliche Wartungsinformationen.

Output ist eine Top-5-Liste gerasterter PDF-Seiten aus der jeweiligen
Qdrant-Collection. Bewertet wird nicht, ob eine Antwort generiert wird, sondern ob
die erwartete PDF-Seite in dieser Rangliste erscheint und wie hoch sie platziert
ist.

## Ground Truth und optimale Werte

Die Ground Truth wurde im Benchmark-Manifest auf Seitenebene festgelegt. Für jede
Query sind eine oder mehrere relevante Seiten-IDs definiert. Diese Festlegung ist
deterministisch, weil Pfad C und Pfad D vollständige Seiten zurückgeben und keine
parserabhängigen Chunks beurteilt werden müssen.

Der optimale Wert für `hit_rate_at_5`, `mrr` und `ndcg_at_5` ist jeweils 1,0. Das
bedeutet, dass für jede Query ein relevantes Ziel gefunden wurde und idealerweise
direkt auf Rang 1 steht. Werte unter 1,0 zeigen, dass relevante Seiten fehlen oder
zu spät in der Top-5-Liste erscheinen.

## Metriken

`hit_rate_at_5` misst, ob mindestens eine relevante PDF-Seite innerhalb der ersten
fünf Treffer gefunden wurde. Die Metrik beantwortet also die Frage: Ist die
richtige Seite überhaupt in Top 5 enthalten?

`mrr` steht für Mean Reciprocal Rank. Für jede Query wird der Kehrwert des ersten
relevanten Rangs berechnet. Rang 1 ergibt 1,0, Rang 2 ergibt 0,5, Rang 5 ergibt
0,2. MRR ist deshalb sensibel dafür, ob die relevante Seite ganz oben oder nur
weiter hinten gefunden wird.

`ndcg_at_5` steht für normalized Discounted Cumulative Gain bis Rang 5. Die Metrik
belohnt relevante Treffer auf frühen Rängen stärker als relevante Treffer auf
späteren Rängen und kann mehrere relevante Seiten pro Query berücksichtigen. Ein
Wert von 1,0 entspricht der idealen Rangfolge innerhalb der Top 5.

Jede Tabellenzeile basiert auf fünf Wiederholungen derselben zwölf Queries pro
Szenario. Die Werte sind arithmetische Mittel über diese fünf Läufe.
