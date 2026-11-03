# Milestone 1 — Trace a submission

## 1. The path a submission takes

1. **User sends text** — `POST /submit` with JSON `{"text": ..., "creator_id": ...}`.
2. **app.py `/submit` validates input** — `text` missing / empty / not a string / too long / too short to score → return **400 Bad Request** with `error` + `message`, and record it with `audit.log_rejection`. Nothing below runs.
3. **app.py generates `content_id`** (uuid) — every later step, the log, and `/appeal` stick with this id.
4. **detector.py `model_signal`** — runs GPT-2 locally, computes perplexity (raw, ~10–200), squashes it to a 0–1 `model_score`. Closer to 0 = more human-like, closer to 1 = more AI-like.
5. **stylometry.py `style_signal`** — measures the text as text: sentence length spread, vocabulary repetition (type-token ratio), punctuation density → one 0–1 `style_score`, same direction (higher = more AI).
6. **scoring.py `combine_signals`** — merges `model_score` and `style_score` (e.g. weighted average) into one `confidence` score, 0–1.
7. **scoring.py `score_to_label`** — two thresholds split the score into three outcomes: high-confidence human / **unsure** / high-confidence AI. Returns a short `guess` and a full-sentence `label` a reader can understand.
8. **audit.py `log_decision`** — appends one JSON line to `logs/audit.jsonl`: timestamp, content_id, creator_id, guess, model_score, style_score, combined score, label, status `decided`.
9. **Response** — **200 OK** with `content_id`, `guess`, `confidence`, `label`, `model_score`, `style_score`.
10. *(later, optional)* **Writer appeals** — `POST /appeal` with `content_id` + reasoning → `audit.log_appeal` records it, status becomes `under_review`.

## 2. The two signals

### Signal 1 — detector.py (model signal)
- **Measures:** how predictable the text is to a language model (GPT-2 perplexity). Low perplexity → high `model_score` → more AI-like.
- **Why human vs AI might differ:** AI generates each next word by sampling from a probability distribution, favouring high-probability words — so another language model finds that text easy to predict. Humans choose words based on what they want to say and grammar, which produces more surprising choices.
- **Blind spot:** predictability ≠ authorship.
  - *False positive:* writers with limited or deliberately plain vocabulary — second-language writers, younger writers, people writing simply on purpose — are just as predictable as AI.
  - *Evasion:* ornate prose full of rare words is hard to predict, so it scores human even if AI wrote it.

### Signal 2 — stylometry.py (style signal)
- **Measures:** the shape of the text without reading it — sentence length spread, vocabulary variety (type-token ratio), punctuation density → one 0–1 `style_score`, higher = more AI-like.
- **Why human vs AI might differ:** AI tends toward the most typical sentence structure, so sentence lengths cluster around an average. Humans vary sentence length freely depending on preference, context, and mood — a three-word sentence next to a forty-word one.
- **Blind spot:** it cannot read; it only sees shape.
  - *False positive:* human writing that is uniform by convention — manuals, bullet-point reports, legal text, technical documentation — has even sentences and repeated vocabulary, so it scores AI-like.
  - *Evasion:* deliberately varying sentence length, vocabulary, and punctuation lowers the score (looks human) without changing the content, even if the content is meaningless.

## 3. Tracing the false positive

- **Who:** a second-language writer submitting a poem they wrote themselves.
- **Score they get:** both signals likely run high *at the same time* — they lean on familiar words (predictable → high `model_score`) and familiar sentence patterns (even lengths, repeated vocabulary → high `style_score`). The two blind spots hit the same person, so averaging doesn't cancel the error. Combined score around 0.75.
- **What the label says to them:** with the current thresholds (AI > 0.65) they get the high-confidence AI label — an accusation on work they wrote. They feel helpless and frustrated.
- **What they can do:** appeal. `POST /appeal` with their `content_id` and their explanation → recorded in the audit log, status moves to `under_review` so a human reviewer can look at it. The label itself must tell them this option exists.
- **What this means for the design:** two agreeing signals ≠ certainty when they share a blind spot. The AI threshold should sit high enough (and the unsure band be wide enough) that this writer lands in "unsure" rather than "AI" — decided in Milestones 4–5.

## 4. Endpoint contracts

### POST /submit

**Request** (JSON)

| Field | Type | Required | Rule |
|---|---|---|---|
| `text` | string | yes | at least 20 words; at most `config.DETECTOR_MAX_TOKENS` (400) tokens ≈ 300 words — the detector only reads the first 400 tokens, so longer text would be judged on a part the model never saw |
| `creator_id` | string | yes | non-empty |

**200 OK**

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string (uuid) | id for this submission; needed for `/appeal` |
| `guess` | `"ai"` \| `"human"` \| `"unsure"` | machine-readable verdict |
| `confidence` | float 0–1 | combined score; 0 = confidently human, 1 = confidently AI |
| `label` | string | full sentence shown to the reader |
| `model_score` | float 0–1 | signal 1, higher = more AI-like |
| `style_score` | float 0–1 | signal 2, higher = more AI-like |

**400 Bad Request** — `{"error": "<code>", "message": "<human-readable reason>"}`, also written to the log via `audit.log_rejection`.

| `error` | When |
|---|---|
| `invalid_json` | body isn't a JSON object |
| `missing_field` | `text` or `creator_id` absent, not a string, or empty |
| `text_too_short` | fewer than 20 words |
| `text_too_long` | more than 400 tokens |

### POST /appeal

**Request** (JSON)

| Field | Type | Required | Rule |
|---|---|---|---|
| `content_id` | string | yes | must exist in the audit log |
| `reasoning` | string | yes | non-empty — the writer's explanation |

`creator_id` is not sent; it's taken from the original decision in the log.

**200 OK**

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string | the item appealed |
| `status` | `"under_review"` | new status |
| `message` | string | confirmation to the writer, e.g. "Your appeal was received. A person will review this piece." |

No re-scoring — the same detector would give the same answer. A human reviews it.

**Errors** — same `{"error", "message"}` shape:

| Status | `error` | When |
|---|---|---|
| 400 | `invalid_json` / `missing_field` | body not JSON, or `content_id` / `reasoning` missing or empty |
| 404 | `not_found` | `content_id` not in the log |
| 409 | `already_under_review` | this item already has an appeal |
