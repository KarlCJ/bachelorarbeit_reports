# Dogs Grayscale Comparison

## Was wurde getestet?

Diese Vergleichstabelle ergänzt die beiden Szenario-3-Bildtests um eine
Graustufenvariante. Testsetup, Qdrant-Namespace, Indexdaten, Ground Truth und
Metriken bleiben unverändert. Der einzige Unterschied ist der Query-Input: Vor der
Einbettung wird jedes Query-Bild in Graustufen umgewandelt und anschließend wieder
als RGB-Bild gespeichert, damit der Embedding-Endpunkt dasselbe Dateiformat wie bei
regulären Querys erhält.

Der verwendete Namespace bleibt
`collection_pfad_d_gemini_embedding_2_szenario_3`. Der Index selbst wird nicht neu
erzeugt und enthält weiterhin die regulären farbigen Indexbilder.

## Dogs Similarity

Beim Similarity-Test werden 17 Hundebilder als Querys verwendet. Davon sind 13
bewertbar, weil für diese Rassen passende Zielbilder im Index liegen. Die vier
Labrador-Retriever-Querys bleiben als diagnostische Negativkontrollen sichtbar,
werden aber nicht in die aggregierten Metriken eingerechnet.

Die reguläre Variante erreicht Hit Rate@5 = 1,0000, MRR = 0,9615 und nDCG@5 =
0,9032. Die Graustufenvariante erreicht Hit Rate@5 = 1,0000, MRR = 0,9385 und
nDCG@5 = 0,9157. Damit bleibt die Top-5-Abdeckung vollständig erhalten. Der etwas
niedrigere MRR-Wert zeigt, dass der erste relevante Treffer im Mittel geringfügig
später erscheint. Der höhere nDCG@5-Wert zeigt zugleich, dass die Verteilung
mehrerer relevanter Treffer innerhalb der Top 5 in der Graustufenvariante etwas
günstiger ausfällt.

## Dogs Identity

Beim Identity-Test werden die 40 indexierten Hundebilder selbst als Querys
verwendet. Pro Query ist genau das identische Indexbild relevant. Die
Graustufenvariante prüft, ob das System das farbige Indexbild auch dann wieder
erkennt, wenn nur die Query-Seite entfärbt wurde.

Sowohl die reguläre Variante als auch die Graustufenvariante erreichen Hit Rate@5
= 1,0000, MRR = 1,0000 und nDCG@5 = 1,0000. Das identische Bild wird also auch bei
Graustufen-Querys zuverlässig auf Rang 1 gefunden.

## Ergebnisdateien

Die kompakten Werte stehen in `dogs_grayscale_comparison.csv`. Die visuellen
Berichte liegen unter `results/dogs_similarity_grayscale/` und
`results/dogs_identity_grayscale/`.
