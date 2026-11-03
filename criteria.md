# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False positives on second-language writers

A fixed set of 10 English pieces written by second-language writers
(`samples/human_l2/`). Run the whole set 3 times. In **every** run, at most
**2 of 10** are labelled high-confidence AI.

**Why this target:**

A second-language writer is the person both signals are most likely to
accuse at once: familiar words make the text predictable to the model, and
familiar sentence patterns make it look even to stylometry. Averaging two
signals that share a blind spot does not cancel the error. On a writing site a
wrong accusation costs the writer far more than a missed detection costs the
site, so I allow at most 2 in 10 — and it must hold in every run, because the
model signal can drift between runs.

---

## 2. Score spread between clearly-AI and clearly-human text

A fixed set of 5 clearly-AI pieces (`samples/ai/` — generated, unedited) and
5 clearly-human pieces (`samples/human/`). Mean `confidence` of the AI set
minus mean `confidence` of the human set is **≥ 0.75**, in all 3 runs.

**Why this target:**

My thresholds are 0.35 and 0.65, so a gap of 0.3 is the minimum for the two
groups to land in different labels. 0.75 asks for much more: clearly-AI and
clearly-human text should sit near opposite ends of the scale, not just on
either side of a line. If the easy cases aren't far apart, the hard cases have
no chance.

---

## 3. Every label is reachable

A fixed set of 10 pieces (`samples/coverage/`): 4 AI, 4 human, 2 I judge
borderline. In each of 3 runs, `human`, `unsure` and `ai` each appear as the
`guess` **at least once**.

**Why this target:**

Three labels only mean something if all three can actually be produced. A
gap in the ranges — or a style signal that barely moves — can make a label
unreachable, and the "unsure" label is the one that protects writers like the
one in criterion 1. The set is fixed in advance so I can't pick inputs after
seeing the scores.

---

## 4. Every appeal is recorded and moves to under_review

Appeal 5 existing `content_id`s once each: **5 of 5** return 200, and the log
holds an entry for each with `event: appeal`, `status: under_review`, and
`reasoning` identical to what was sent. Also: 1 appeal on a non-existent id
returns **404**; a second appeal on the same id returns **409**; the original
`decided` entry is unchanged.

**Why this target:**

The appeal is the only thing a wrongly accused writer can do. If an appeal
is ever lost, misrecorded, or silently overwrites the original decision, that
writer has nothing. So this has to be 5 of 5, not most: the log must show what
was decided, that it was challenged, and in what order.

---

## 5. Bad input is rejected, never crashes

Each of these 7 inputs returns **400** with the listed `error` code and leaves
one `rejected` entry in the log. **0 of 7** return 500.

| # | Input | `error` |
|---|---|---|
| 1 | body is not JSON | `invalid_json` |
| 2 | `text` missing | `missing_field` |
| 3 | `text` is `""` | `missing_field` |
| 4 | `text` is `123` | `missing_field` |
| 5 | `creator_id` missing | `missing_field` |
| 6 | `text` is 5 words | `text_too_short` |
| 7 | `text` over 400 tokens | `text_too_long` |

**Why this target:**

A crash on malformed input is one of the most common real failures, and
unit 8's attack set will probe exactly these edges. A 500 tells the caller
nothing and leaves no trace; a 400 with a specific code tells them what to fix,
and the `rejected` log entry means an attack that only shows up as bad input
is still visible.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
