# Troubleshooting Backend Comparison

## Was wurde getestet?

Diese Tabelle vergleicht Varianten des unabhängigen Troubleshooting-Bildtests. Der
Test simuliert den Fall, dass ein Nutzer ein Foto oder einen Screenshot eines
Fehlersymbols der Quantum-Weaver-Maschine hochlädt und das Retrieval-System die
passende Troubleshooting-Evidenz finden soll.

Der Index enthält 73 visuelle Einheiten: 63 eindeutige PDF-Seiten aus Szenario 1
und Szenario 2 inklusive Noise-Seiten sowie zehn manuell ausgeschnittene
Referenz-Screenshots aus der Troubleshooting-Tabelle des Quantum-Weaver-Handbuchs.

Verglichen werden direkte Bild-Queries, Caption-to-Text-Queries, eine
Gemini-Multimodal-Variante mit Bild plus festem Hilfetext, eine Icon-Crop-
Referenzvariante sowie Graustufen-Querys. Dadurch wird geprüft, ob ein Backend
eher das exakt passende Referenzbild findet, die originale PDF-Seite erreicht oder
von Darstellungsvarianten wie Farbe und Ausschnitt abhängig ist.

## Inputs und Outputs

Input ist jeweils eines von zehn nutzerbereitgestellten Query-Bildern. Jedes Bild
zeigt ein Fehlersymbol beziehungsweise einen Fehlercode. Bei Caption-Varianten
wird das Query-Bild zuerst von GPT-5.4 Mini beschrieben und anschließend als
Text-Query eingebettet. Bei der Gemini-Multimodal-Variante wird das Query-Bild
zusammen mit dem festen Text `Das Display der Maschine zeigt mir folgenden fehler
an, was muss ich tun?` eingebettet.

Output ist eine Top-5-Liste aus visuellen Indexeinheiten. Ein Treffer kann ein
manueller Referenz-Screenshot oder eine PDF-Seite sein. Bewertet wird, ob das
System den passenden Referenz-Screenshot und die PDF-Seite mit der passenden
Fehlerzeile findet.

## Ground Truth und optimale Werte

Für jede Query wurden zwei Zielobjekte festgelegt: Der passende manuelle
Referenz-Screenshot ist das ideale Ziel auf Rang 1. Die PDF-Seite, auf der die
entsprechende Fehlerzeile im Handbuch vorkommt, ist das ideale Ziel auf Rang 2.
Diese Ground Truth wurde über die stabil benannten Fehlercodes und die manuell
ausgeschnittenen Referenz-Screenshots festgelegt.

Der optimale Wert für `reference_hit_at_1`, `reference_hit_at_k`,
`page_hit_at_k`, `ordered_pair_hit_at_2`, `hit_rate_at_5`, `mrr` und `ndcg_at_5`
ist jeweils 1,0. Besonders streng ist `ordered_pair_hit_at_2`, weil diese Metrik
nur dann 1,0 ist, wenn beide erwarteten Ziele in der idealen Reihenfolge
erscheinen.

## Metriken

`reference_hit_at_1` misst, ob der passende Referenz-Screenshot exakt auf Rang 1
liegt. Diese Metrik prüft die Fähigkeit, das konkrete Fehlersymbol wiederzufinden.

`reference_hit_at_k` misst, ob der passende Referenz-Screenshot innerhalb der Top
5 erscheint.

`page_hit_at_k` misst, ob die PDF-Seite mit der passenden Fehlerzeile innerhalb
der Top 5 erscheint. Diese Metrik ist wichtig, weil die PDF-Seite den eigentlichen
Dokumentkontext liefert.

`ordered_pair_hit_at_2` misst den Idealfall: Referenz-Screenshot auf Rang 1 und
passende PDF-Seite auf Rang 2. Niedrige Werte bedeuten nicht zwangsläufig, dass
das Backend gar nichts findet, sondern häufig, dass die Seite erst später gerankt
wird.

`hit_rate_at_5`, `mrr` und `ndcg_at_5` bewerten die kombinierte Top-5-Rangliste
gegen die relevanten Zielobjekte. Hit Rate@5 misst die Top-5-Abdeckung, MRR die
Position des ersten relevanten Treffers und nDCG@5 die Qualität der Rangfolge bis
Rang 5.
