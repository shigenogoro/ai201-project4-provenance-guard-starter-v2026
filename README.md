# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->



---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** how predictable the text is to GPT-2, run locally (`detector.py::model_signal`). Perplexity is squashed onto 0–1 with a logistic (midpoint 45, steepness 1.6, starter defaults, unchanged). Higher = more AI-like.

**Why that might differ between human and AI writing:** AI picks each next word from a probability distribution, favouring likely words, so another language model finds the result easy to predict. People choose words for what they mean, which produces more surprising choices.

**What it can't see:** predictability is not authorship. Writers with limited or deliberately plain vocabulary — second-language writers, younger writers — are as predictable as AI. My 10 second-language samples averaged **0.70**, against **0.84** for AI and **0.52** for native human prose. In the other direction, AI text with rare words scores human. Light human edits also go unseen: `borderline_02_sports` (AI text with my own hockey anecdote added) scored 0.79, the same as the unedited AI piece next to it.

### Signal two — the style signal

**What it measures:** the shape of the text, without reading it (`stylometry.py::style_signal`). Three measures, each scaled to 0 (human end) – 1 (AI end) and clamped:

| Measure | Raw value | Human end → AI end | Weight |
|---|---|---|---|
| Sentence length spread | stdev / mean of sentence lengths | 0.60 → 0.20 | 0.5 |
| Type-token ratio | unique / total, first 60 words only | 0.70 → 0.90 | 0.2 |
| Rich punctuation | `; : ( ) — – -` per 100 words | 3.0 → 0.0 | 0.3 |

A one-sentence text has no spread; it counts as neutral (0.5) rather than as evidence.

**Why that might differ between human and AI writing:** AI regresses to the typical sentence, so lengths cluster around an average; people write a three-word sentence next to a forty-word one. Native writers reach for semicolons and dashes; AI mostly doesn't.

Two findings from calibration changed the design:
- **Type-token ratio ran the opposite way from the usual assumption.** AI scored *higher* (≈0.84 on the first 60 words) than human prose (≈0.78): AI uses many distinct polished words, people repeat function words. I flipped it and gave it the lowest weight because the gap is small.
- **Total punctuation density didn't discriminate at all** — about 14 per 100 words for AI, human and second-language samples alike. I dropped it for rich punctuation only.

**What it can't see:** meaning. Anything that changes shape without changing substance moves it — breaking up sentences, pasting a quotation, adding a dash. And human writing that is uniform by convention scores AI-like: my second-language samples have spread 0.31 (AI ≈0.27) and **zero** rich punctuation, so they average 0.72 on this signal too.

### The combining rule

**The rule:** weighted average of the two signals. If they disagree by more than 0.3, the result is capped just below the AI threshold, so it can be "unsure" but never "AI". The cap is one-sided on purpose: disagreement can block an accusation, but never takes away a "human" label. (A two-sided version pulled clearly human pieces up into "unsure" and left no "human" label in my coverage set.)

**The numbers:** (`config.py`)
- `WEIGHT_MODEL_SIGNAL = 0.5`, `WEIGHT_STYLE_SIGNAL = 0.5` — the two separate about equally well on my samples, so neither gets more weight.
- `DISAGREEMENT_GAP = 0.3`
- `HUMAN_THRESHOLD = 0.35`, `AI_THRESHOLD = 0.80` — AI raised from the starter's 0.65. My second-language samples top out at 0.79 combined and overlap the AI samples (0.72–0.89). At 0.65, 8 of 10 would be labelled AI; at 0.80, none are. The cost: 4 of 9 AI samples land in "unsure" instead of "AI".

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:** `samples/coverage/human_01_three_men.txt` (Jerome K. Jerome, 1889). Model signal **0.74**: plain, everyday vocabulary that GPT-2 predicts easily. Style signal **0.32**: sentence lengths vary widely. The gap is 0.42 > 0.3, so the cap applies. The average is 0.53, already below the cap, so it stays at 0.53, which is "unsure". Without the cap, a piece averaging above 0.80 with signals this far apart would have been labelled AI on one signal's say-so.

**Calibration caveat:** the ranges, weights and thresholds above were read off the same 30 samples that `criteria.md` checks against. That flatters the results. Unit 8's unseen attack set is the honest test.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | We think this was probably written by a person. |
| unsure | above 0.35, below 0.80 | We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing — a lot of people's own work lands here. You don't need to do anything. |
| high-confidence AI | 0.80 – 1.00 | We think this was probably written with AI. Our check can be wrong, especially with plain or simple writing. If you wrote this yourself, you can appeal: tell us in your own words how you wrote it — for example, where the idea came from or what drafts you made. A person, not the computer, will review your appeal. |

The text lives in `scoring.py` (`LABEL_HUMAN`, `LABEL_UNSURE`, `LABEL_AI`); the ranges come from `config.py`. Every score from 0 to 1 maps to exactly one label, and all three appear on my sample set.

**Why I worded the "unsure" one this way:**

All 10 of my second-language samples — my own writing — land in "unsure", and so do most of the native human samples. So the typical reader of this label wrote every word. My first draft explained *why* ("because of the sentence structure, vocabulary and punctuation") and asked the writer to give reasoning so the system could re-evaluate. Read as that writer, it said two things I didn't mean: *your English is the problem*, and *prove you're innocent*. It also promised a re-evaluation the system doesn't do. So the final version only says honestly that we couldn't tell, says outright that it is not an accusation or a judgement of their writing, and asks nothing of them.


---

## Sample Run

Run against the live service (`python app.py`), one piece from `samples/ai/03_climate.txt`.

**A submission**

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Climate change is one of the most pressing issues facing humanity today. Rising global temperatures are leading to more frequent and severe weather events, including hurricanes, droughts, and heatwaves. These changes have significant impacts on ecosystems, agriculture, and human health. One of the primary drivers of climate change is the burning of fossil fuels, which releases greenhouse gases into the atmosphere. To mitigate these effects, it is essential to transition to renewable energy sources such as solar and wind power. Additionally, individuals can contribute by reducing energy consumption, using public transportation, and supporting sustainable practices. Governments also play a crucial role by implementing policies that encourage emissions reductions. While the challenge is significant, collective action at every level can make a meaningful difference in protecting the planet for future generations.", "creator_id": "writer-02"}'
```

```json
{
  "confidence": 0.8816,
  "content_id": "d4ff6775-7bf6-4841-9870-417c023c8cec",
  "guess": "ai",
  "label": "We think this was probably written with AI. Our check can be wrong, especially with plain or simple writing. If you wrote this yourself, you can appeal: tell us in your own words how you wrote it — for example, where the idea came from or what drafts you made. A person, not the computer, will review your appeal.",
  "model_score": 0.9337,
  "style_score": 0.8295
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "d4ff6775-7bf6-4841-9870-417c023c8cec", "reasoning": "I wrote this for my environmental science class. I outlined the causes and solutions first, then wrote it in one sitting."}'
```

```json
{
  "content_id": "d4ff6775-7bf6-4841-9870-417c023c8cec",
  "message": "Your appeal was received. A person will review this piece and your explanation.",
  "status": "under_review"
}
```

**What the log shows afterwards**

The original decision is untouched; the appeal is appended after it.

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.8816,
      "content_id": "d4ff6775-7bf6-4841-9870-417c023c8cec",
      "creator_id": "writer-02",
      "guess": "ai",
      "label": "We think this was probably written with AI. Our check can be wrong, especially with plain or simple writing. If you wrote this yourself, you can appeal: tell us in your own words how you wrote it — for example, where the idea came from or what drafts you made. A person, not the computer, will review your appeal.",
      "model_score": 0.9337,
      "status": "decided",
      "style_score": 0.8295,
      "timestamp": "2026-11-03T16:23:49+00:00"
    },
    {
      "content_id": "d4ff6775-7bf6-4841-9870-417c023c8cec",
      "creator_id": "writer-02",
      "event": "appeal",
      "reasoning": "I wrote this for my environmental science class. I outlined the causes and solutions first, then wrote it in one sitting.",
      "status": "under_review",
      "timestamp": "2026-11-03T16:23:54+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
