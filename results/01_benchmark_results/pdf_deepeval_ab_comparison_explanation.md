# Pfad A/B DeepEval Retrieval

## Was wurde getestet?

Diese Tabelle vergleicht Pfad A und Pfad B in den PDF-Szenarien 1 und 2. Beide
Pfade verwenden Docling als vorgelagerten PDF-Parser und erzeugen dadurch
parserabhängige Retrieval-Einheiten. Pfad A beschreibt extrahierte Bild- und
Tabellenregionen zunächst mit GPT-5.4 Mini und indexiert anschließend Text-Chunks
und Captions. Pfad B verzichtet auf Captioning und indexiert Text-Chunks sowie
extrahierte visuelle Regionen direkt im gemeinsamen Gemini-Embedding-Raum.

Szenario 1 enthält die beiden Primärdokumente: das Quantum-Weaver-Handbuch und den
AeroNova-Geschäftsbericht. Szenario 2 enthält dieselben Primärdokumente plus ein
großes thematisch irrelevantes Noise-PDF. Der Szenario-2-Test prüft also, ob die
Docling-basierten Pfade unter zusätzlichem irrelevanten Kontext weiterhin
semantisch passende Evidenz zurückgeben.

## Inputs und Outputs

Input pro Testfall ist ein Eintrag aus `tests/evals/.dataset.json`. Ein Testfall
kann eine reine Textfrage, eine Bildfrage oder eine kombinierte Bild-Text-Query
sein. Die Query wird mit Gemini Embedding 2 eingebettet und gegen die jeweilige
Qdrant-Collection von Pfad A oder Pfad B gesucht.

Output des Retrievers ist keine finale Antwort, sondern eine Top-k-Liste von
Kontexten. Diese Kontexte können Text-Chunks, Tabelleninhalte, Captions oder
extrahierte visuelle Regionen sein. DeepEval bewertet anschließend, ob diese
zurückgegebenen Kontexte die manuell definierte Ground Truth stützen.

## Ground Truth und optimale Werte

Die Ground Truth wurde manuell in der DeepEval-Dataset-Datei festgelegt. Sie
enthält Referenztexte und, falls nötig, Referenzbilder. Sie enthält bewusst keine
Qdrant-Punkt-IDs, weil bei Docling nicht stabil vorhergesagt werden kann, ob eine
fachlich relevante Information als Text, Tabelle, Caption oder Bildregion
extrahiert wird.

Alle DeepEval-Metriken liegen idealerweise bei 1,0. Ein Wert von 1,0 bedeutet, dass
die zurückgegebenen Kontexte nach Einschätzung des Judges vollständig und passend
zur Referenz sind. Niedrigere Werte zeigen entweder fehlende Evidenz, schlechte
Rangpositionen relevanter Evidenz oder irrelevante Zusatzkontexte.

## Metriken

`contextual_precision` bewertet, ob relevante Kontexte möglichst früh in der
Top-k-Liste stehen. Ein hoher Wert bedeutet, dass wichtige Evidenz nicht erst
spät oder zwischen vielen irrelevanten Treffern erscheint.

`contextual_recall` bewertet, ob die zurückgegebenen Kontexte die manuelle
Referenz ausreichend abdecken. Ein hoher Wert bedeutet, dass die zur Beantwortung
der Query notwendige Evidenz im Retrieval-Kontext enthalten ist.

`contextual_relevancy` bewertet, ob die zurückgegebenen Kontexte zur Query passen
und nicht überwiegend thematisch irrelevante Informationen enthalten.

`average_score` ist der arithmetische Mittelwert aus Contextual Precision,
Contextual Recall und Contextual Relevancy. Er dient als kompakte
Vergleichsgröße, ersetzt aber nicht die Interpretation der Einzelmetriken.

Jede Tabellenzeile basiert auf fünf wiederholten Suite-Ausführungen. Die
angegebenen Werte sind arithmetische Mittel über diese fünf Läufe.
