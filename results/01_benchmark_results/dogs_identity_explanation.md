# Dogs Identity Test

## Was wurde getestet?

Der Dogs-Identity-Test ist ein Kontrolltest für Szenario 3. Er prüft, ob Gemini
Embedding 2 exakt die bereits indexierten Hundebilder wiederfindet, wenn dasselbe
Bild erneut als Query verwendet wird. Dieser Test misst damit nicht semantische
Generalisierung auf neue Bilder, sondern die technische Wiederauffindbarkeit
identischer Indexbilder.

Der Test nutzt dieselbe Qdrant-Collection wie der Dogs-Similarity-Test:
`collection_pfad_d_gemini_embedding_2_szenario_3`. Der Index enthält 40
Hundebilder aus 10 Rassen und 40 Katzenbilder als visuelles Rauschen.

## Inputs und Outputs

Input ist jeweils eines der 40 indexierten Hundebilder. Dieses Bild wird erneut
mit `google/gemini-embedding-2-preview` eingebettet und als Bild-Query gegen die
Collection gesucht.

Output ist eine Top-5-Liste indexierter Bilder. Der optimale Treffer ist das
identische Bild, das bereits im Index liegt. Katzenbilder und andere Hundebilder
sind für diesen Test nicht relevant, selbst wenn sie visuell ähnlich sind.

## Ground Truth und optimale Werte

Die Ground Truth ist pro Query genau ein Zielbild: die identische indexierte
Bilddatei. Die relevanten Punkt-IDs stammen aus dem Szenario-3-Manifest und den
Qdrant-Payloads. Dadurch ist die Bewertung deterministisch und benötigt keinen
LLM-Judge.

Der optimale Wert für `hit_rate_at_5`, `mrr` und `ndcg_at_5` ist 1,0. Da es pro
Query genau ein relevantes Ziel gibt, bedeutet ein perfekter Wert, dass das
identische Bild auf Rang 1 gefunden wurde.

## Metriken

`hit_rate_at_5` misst, ob das identische Bild innerhalb der ersten fünf Treffer
gefunden wurde.

`mrr` steht für Mean Reciprocal Rank. Bei diesem Test ist MRR besonders direkt zu
lesen: Rang 1 ergibt 1,0, Rang 2 ergibt 0,5 und Rang 5 ergibt 0,2.

`ndcg_at_5` steht für normalized Discounted Cumulative Gain bis Rang 5. Weil es
pro Query nur ein relevantes Zielbild gibt, entspricht ein Wert von 1,0 dem
identischen Bild auf Rang 1. Spätere Ränge senken den Wert.

## Warum ist dieser Test wichtig?

Der Identity-Test prüft, ob die technische Embedding- und Retrieval-Pipeline
grundsätzlich stabil funktioniert. Wenn ein System bereits identische Indexbilder
nicht zuverlässig auf Rang 1 findet, wären semantische Similarity-Ergebnisse kaum
interpretierbar. Ein perfekter Identity-Test beweist aber noch keine semantische
Generalisierung; dafür ist der Dogs-Similarity-Test zuständig.

## Ergebnisdateien

Der visuelle Bericht liegt unter `results/dogs_identity/index.html`. Die
zugehörige CSV-Quelle ist
`outputs/scenario3_gemini/collection_pfad_d_gemini_embedding_2_szenario_3_identity_scored.csv`.
