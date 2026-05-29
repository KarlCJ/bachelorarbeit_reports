# Bewertungsmetriken

## DeepEval-Metriken für Pfad A und Pfad B

Contextual Precision bewertet, ob relevante Kontexte in der Trefferliste möglichst
weit oben stehen. Hohe Werte bedeuten, dass relevante Chunks oder Bildregionen früh
im Top-k-Kontext erscheinen.

Contextual Recall bewertet, ob die zurückgegebenen Kontexte die manuell definierte
Referenzinformation ausreichend abdecken. Hohe Werte bedeuten, dass die für die
Antwort benötigte Evidenz im Retrieval-Kontext enthalten ist.

Contextual Relevancy bewertet, ob die zurückgegebenen Kontexte zur Query passen und
nicht überwiegend thematisch irrelevante Informationen enthalten.

Average Score ist der arithmetische Mittelwert aus Contextual Precision,
Contextual Recall und Contextual Relevancy. Er ersetzt nicht die Einzelmetriken,
sondern verdichtet sie nur für Tabellen und Diagramme.

## Deterministische Rankingmetriken für Pfad C, Pfad D und Troubleshooting

Hit Rate@5 misst, ob mindestens ein relevantes Ziel innerhalb der ersten fünf
Treffer gefunden wurde. Die Metrik ist gut für Top-k-Abdeckung, unterscheidet aber
nicht, ob ein Treffer auf Rang 1 oder Rang 5 liegt.

MRR steht für Mean Reciprocal Rank. Für jede Query wird der Kehrwert des Rangs des
ersten relevanten Treffers berechnet. Ein Treffer auf Rang 1 zählt 1,0, Rang 2
zählt 0,5 und Rang 5 zählt 0,2. MRR bestraft relevante Treffer auf späteren Rängen
daher stärker als Hit Rate@5.

nDCG@5 steht für normalized Discounted Cumulative Gain bis Rang 5. Die Metrik
berücksichtigt mehrere relevante Treffer und gewichtet frühe Ränge höher als späte
Ränge. Sie ist besonders nützlich, wenn mehr als ein Ziel relevant sein kann.

reference_hit_at_1 misst im Troubleshooting-Test, ob der passende manuelle
Referenz-Screenshot exakt auf Rang 1 liegt.

reference_hit_at_k misst, ob der passende Referenz-Screenshot innerhalb der Top-k
Treffer vorkommt.

page_hit_at_k misst, ob die PDF-Seite mit der passenden Fehlerzeile innerhalb der
Top-k Treffer vorkommt.

ordered_pair_hit_at_2 ist die strengste Troubleshooting-Metrik. Sie ist nur dann
1,0, wenn der Referenz-Screenshot auf Rang 1 und die passende PDF-Seite auf Rang 2
liegt.
