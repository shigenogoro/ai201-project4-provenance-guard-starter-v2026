# Signal-one recalibration sweep — before any change

- Produced by: perplexity (`detector.py::perplexity`) and style (`stylometry.py::style_signal`)
  computed once per text, then signal one's logistic `1 / (1 + (ppl/midpoint)^steepness)`
  and the combining rule from `scoring.py::combine_signals` recomputed for each setting.
- Texts: samples/human_l2 (10), 20 variants of those (each piece minus its first
  sentence, and minus its last), samples/ai (5), samples/human (5), samples/coverage
  (10), attack set EV01–EV10 except EV08 plus PI02 (10), FP01–FP07 (7), and the
  unedited AI baseline (EV02 with " Really." removed).
- ⚠️ Tuned on the same samples criteria 1–3 check. Unit 8's attack set is the unseen check.

## Raw perplexity

ai:     20.1, 16.8, 8.6, 8.9, 15.6
human:  75.0, 51.3, 49.3, 43.1, 40.0
L2:     25.1, 26.8, 24.8, 41.3, 27.9, 32.6, 18.5, 27.2, 27.8, 21.3
unedited AI baseline (85 words): 33.3

Style gap (AI mean − human mean): 0.795 − 0.304 = 0.492

## Criterion 2 ceiling

| midpoint | steepness | model gap | combined gap (no cap) | L2 model mean |
|---|---|---|---|---|
| 45 | 1.6 | 0.408 | 0.450 | 0.693 |
| 28 | 1.6 | 0.469 | 0.480 | 0.518 |
| 28 | 3 | 0.706 | 0.599 | 0.533 |
| 28 | 4 | 0.806 | 0.649 | 0.542 |
| 28 | 6 | 0.914 | 0.703 | 0.559 |

## Trade-off grid

| mid | k | AI thr | L2 ai/10 (max) | L2 variants ai/20 (max) | C2 gap | labels | EV+PI02 ai/10 | baseline | FP ai/7 (max) | AI samples ai/5 |
|---|---|---|---|---|---|---|---|---|---|---|
| 45 | 1.6 | 0.80 | 0 (0.79) | 0 (0.79) | 0.450 | a h u | 0 | 0.66 u | 0 (0.77) | 4 |
| 45 | 1.6 | 0.75 | 4 (0.79) | 2 (0.79) | 0.450 | a h u | 0 | 0.66 u | 4 (0.77) | 4 |
| 45 | 1.6 | 0.70 | 6 (0.79) | 8 (0.79) | 0.450 | a h u | 0 | 0.66 u | 4 (0.77) | 5 |
| 28 | 3 | 0.80 | 0 (0.74) | 0 (0.70) | 0.599 | a h u | 0 | 0.54 u | 0 (0.76) | 4 |
| 28 | 3 | 0.75 | 0 (0.74) | 0 (0.70) | 0.599 | a h u | 0 | 0.54 u | 2 (0.76) | 4 |
| 28 | 3 | 0.70 | 1 (0.74) | 1 (0.70) | 0.599 | a h u | 0 | 0.54 u | 4 (0.76) | 4 |
| 28 | 4 | 0.80 | 0 (0.77) | 0 (0.74) | 0.649 | a h u | 0 | 0.52 u | 0 (0.79) | 4 |
| 28 | 4 | 0.75 | 1 (0.77) | 0 (0.74) | 0.649 | a h u | 0 | 0.52 u | 3 (0.79) | 4 |
| 28 | 4 | 0.70 | 2 (0.77) | 2 (0.74) | 0.649 | a h u | 0 | 0.52 u | 4 (0.79) | 5 |
| 22 | 3 | 0.80 | 0 (0.67) | 0 (0.64) | 0.590 | a h u | 0 | 0.46 u | 0 (0.70) | 2 |
| 22 | 3 | 0.75 | 0 (0.67) | 0 (0.64) | 0.590 | a h u | 0 | 0.46 u | 0 (0.70) | 3 |
| 22 | 3 | 0.70 | 0 (0.67) | 0 (0.64) | 0.590 | a h u | 0 | 0.46 u | 0 (0.70) | 4 |
| 22 | 4 | 0.80 | 0 (0.69) | 0 (0.66) | 0.632 | a h u | 0 | 0.43 u | 0 (0.73) | 3 |
| 22 | 4 | 0.75 | 0 (0.69) | 0 (0.66) | 0.632 | a h u | 0 | 0.43 u | 0 (0.73) | 4 |
| 22 | 4 | 0.70 | 0 (0.69) | 0 (0.66) | 0.632 | a h u | 0 | 0.43 u | 2 (0.73) | 4 |
