# Dogs Similarity Test

## Was wurde getestet?

Der Dogs-Similarity-Test ist der semantische Bild-zu-Bild-Test aus Szenario 3.
Er prüft, ob der Pfad-D-Lauf mit Gemini Embedding 2 visuell ähnliche Hunde nach
Rassemerkmalen findet, obwohl der Index zusätzlich Katzenbilder als visuelles
Rauschen enthält.

Der Index `collection_pfad_d_gemini_embedding_2_szenario_3` enthält 80 Bilder:
40 Hundebilder aus 10 Rassen und 40 Katzenbilder als Noise. Von jeder indexierten
Hunderasse liegen vier Bilder im Index. Die Query-Menge enthält 17 Hundebilder:
5 Golden-Retriever-Querys, darunter ein nutzerbereitgestelltes Bild, sowie jeweils
4 Querys für German Shepherd, Siberian Husky und Labrador Retriever.

Labrador Retriever ist bewusst nicht im Index vertreten. Diese vier Querys sind
diagnostische Negativkontrollen: Sie bleiben im CSV und im HTML-Bericht sichtbar,
werden aber nicht in die aggregierten Qualitätsmetriken eingerechnet, weil es für
sie kein relevantes indexiertes Zielbild gibt.

## Inputs und Outputs

Input ist jeweils ein Query-Bild eines Hundes. Das Bild wird mit
`google/gemini-embedding-2-preview` eingebettet und gegen die Qdrant-Collection
gesucht. Es wird keine Textbeschreibung und kein Rassename als Query verwendet.
Die Suche ist also ein reiner Vektorvergleich auf Basis des Bildes.

Output ist eine Top-5-Liste indexierter Bilder. Ein Treffer kann ein Hundebild
oder ein Katzenbild sein. Für bewertbare Querys gilt ein Treffer als relevant,
wenn das gefundene indexierte Hundebild dieselbe Rasse wie das Query-Bild hat.

## Ground Truth und optimale Werte

Die Ground Truth wurde über das reproduzierbare Szenario-3-Manifest festgelegt.
Für jede bewertbare Query sind alle indexierten Bilder derselben Rasse relevant.
Da pro Rasse vier Bilder indexiert wurden, hat eine bewertbare Query typischerweise
vier relevante Zielbilder.

Für Labrador Retriever gibt es absichtlich keine relevanten Zielbilder im Index.
Diese Fälle prüfen, wie das System mit nicht abgedeckten Rassen umgeht, werden
aber aus den aggregierten Metriken ausgeschlossen.

Der optimale Wert für `hit_rate_at_5`, `mrr` und `ndcg_at_5` ist 1,0. Das bedeutet:
Mindestens ein gleichrassiges Bild wurde in Top 5 gefunden, der erste relevante
Treffer steht möglichst weit oben, und die relevanten Treffer sind ideal gerankt.

## Metriken

`hit_rate_at_5` misst, ob mindestens ein relevantes Bild derselben Rasse innerhalb
der ersten fünf Treffer vorkommt.

`mrr` steht für Mean Reciprocal Rank. Die Metrik bewertet den Rang des ersten
relevanten Treffers. Ein relevanter Treffer auf Rang 1 ergibt 1,0, Rang 2 ergibt
0,5 und Rang 5 ergibt 0,2.

`ndcg_at_5` steht für normalized Discounted Cumulative Gain bis Rang 5. Die Metrik
bewertet die Qualität der gesamten Top-5-Rangfolge und berücksichtigt, ob mehrere
gleichrassige Bilder früh erscheinen.

`included_in_aggregate` zeigt, ob eine Query in die aggregierten Metriken
eingerechnet wurde. Labrador-Querys sind hier `false`, weil sie keine relevanten
indexierten Zielbilder besitzen.

## Ergebnisdateien

Der visuelle Bericht liegt unter `results/dogs_similarity/index.html`. Die
fünfmalige Zusammenfassung liegt in `results/dogs_with_5_iterations.csv`.
