# Benchmark Result Artifacts

Die aktuellen Ergebnisartefakte sind nach Bewertungslogik getrennt. Für Pfad A und
Pfad B ist `pdf_deepeval_ab_comparison.*` maßgeblich, weil diese Pfade mit
DeepEval-Kontextmetriken bewertet werden. Für Pfad C und Pfad D ist
`pdf_page_cd_comparison.*` maßgeblich, weil diese Pfade vollständige PDF-Seiten
zurückgeben und daher mit deterministischen Rankingmetriken bewertet werden.

`troubleshooting_backend_comparison.*` enthält den aktualisierten Vergleich der
Troubleshooting-Varianten. `troubleshooting_rank_diagnostics.*` enthält die
Top-20-Diagnose zur Frage, ob erwartete PDF-Seiten grundsätzlich gefunden werden
oder nur außerhalb der Top 5 erscheinen.

`dogs_similarity_explanation.md` und `dogs_identity_explanation.md` erklären die
beiden Szenario-3-Bildtests. Die zugehörigen visuellen Berichte liegen unter
`results/dogs_similarity/` und `results/dogs_identity/`.

`dogs_grayscale_comparison.csv` und `dogs_grayscale_comparison_explanation.md`
ergänzen diese Tests um die Graustufen-Query-Variante. Die zugehörigen visuellen
Berichte liegen unter `results/dogs_similarity_grayscale/` und
`results/dogs_identity_grayscale/`.

Die ältere Datei `pdf_page_backend_comparison.*` ist ein Legacy-Artefakt aus der
früheren gemeinsamen Vergleichsdarstellung und sollte für die finale Thesis nicht
mehr verwendet werden.
