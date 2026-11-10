# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 19:20
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `b0b057cf-e1f3-4ab8-8ee6-5a6db5ff9525` | unsure | 0.523 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `a293cd75-7665-4528-a227-f41307090e86` | unsure | 0.389 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c6574351-c40d-486c-acc8-df7551a42a07` | unsure | 0.587 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `b97fb5cb-d838-4f19-96e7-413612b9b5d3` | unsure | 0.689 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `2aced27d-a4b9-47fd-ba30-2db9f9d18500` | human | 0.244 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `9d5db0c7-9045-4285-831e-ad4509a8d2f9` | unsure | 0.470 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `e5f31b55-2bd8-4249-be43-9c7ae7324dde` | unsure | 0.476 |  |
| EV08 | evasion | signal one: text below the token window | 400 | `—` | — | — |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `795d0245-749d-4fe1-817a-d715c7cbce9e` | unsure | 0.640 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `e02d286f-d23a-4754-a875-e602fe7e524d` | unsure | 0.768 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `627b62c6-f083-4e42-95a0-4f9a52725f77` | unsure | 0.615 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `eb3aeaec-b0a9-4742-b057-5ef91671dd1d` | unsure | 0.761 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `04e10ef0-4307-4c29-bc33-48c726883178` | unsure | 0.772 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `1e7fbdad-744c-46f2-b208-4e8908a7ec6a` | unsure | 0.762 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `d81c22a9-f139-4ce5-8f9c-078aff443854` | unsure | 0.752 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `58743161-1af4-4569-aaef-630034a2ab8e` | unsure | 0.666 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `7fae0a59-7796-4042-8ffe-1a800017ca43` | unsure | 0.591 |  |
| FP08 | false_positive | very short genuine human submission | 400 | `—` | — | — |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `112f5ae6-f362-4c95-ae1f-8d89405b746d` | unsure | 0.481 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `d0ebe8ed-ec72-4910-8332-7d00504e75ac` | human | 0.241 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `f086b90d-ccb7-418e-a694-8e2dc28f9193` | unsure | 0.558 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `85daafd7-260b-40f1-a07b-b431a45ff35b` | unsure | 0.458 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `928b22a5-2d48-4f73-a742-5283bb69b137` | unsure | 0.500 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `d254a1f4-35c5-4896-8790-564451bfce17` | unsure | 0.592 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "b0b057cf-e1f3-4ab8-8ee6-5a6db5ff9525",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.523,
  "model_score": 0.1635,
  "style_score": 0.8824,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "a293cd75-7665-4528-a227-f41307090e86",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.3888,
  "model_score": 0.5943,
  "style_score": 0.1833,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "c6574351-c40d-486c-acc8-df7551a42a07",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5867,
  "model_score": 0.6662,
  "style_score": 0.5071,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "b97fb5cb-d838-4f19-96e7-413612b9b5d3",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6894,
  "model_score": 0.6114,
  "style_score": 0.7674,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "2aced27d-a4b9-47fd-ba30-2db9f9d18500",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.244,
  "model_score": 0.3212,
  "style_score": 0.1667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "9d5db0c7-9045-4285-831e-ad4509a8d2f9",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4697,
  "model_score": 0.5727,
  "style_score": 0.3667,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "e5f31b55-2bd8-4249-be43-9c7ae7324dde",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4765,
  "model_score": 0.5862,
  "style_score": 0.3667,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_EV08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "795d0245-749d-4fe1-817a-d715c7cbce9e",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6399,
  "model_score": 0.7042,
  "style_score": 0.5755,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "e02d286f-d23a-4754-a875-e602fe7e524d",
  "creator_id": "attacker_EV10",
  "guess": "unsure",
  "confidence": 0.7684,
  "model_score": 0.9792,
  "style_score": 0.5576,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "627b62c6-f083-4e42-95a0-4f9a52725f77",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6145,
  "model_score": 0.6175,
  "style_score": 0.6115,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "eb3aeaec-b0a9-4742-b057-5ef91671dd1d",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7608,
  "model_score": 0.7387,
  "style_score": 0.7829,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "04e10ef0-4307-4c29-bc33-48c726883178",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7725,
  "model_score": 0.8051,
  "style_score": 0.7398,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "1e7fbdad-744c-46f2-b208-4e8908a7ec6a",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.7623,
  "model_score": 0.8329,
  "style_score": 0.6917,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "d81c22a9-f139-4ce5-8f9c-078aff443854",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7522,
  "model_score": 0.8005,
  "style_score": 0.7039,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "58743161-1af4-4569-aaef-630034a2ab8e",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6662,
  "model_score": 0.8814,
  "style_score": 0.451,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "7fae0a59-7796-4042-8ffe-1a800017ca43",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5908,
  "model_score": 0.8816,
  "style_score": 0.3,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_FP08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "112f5ae6-f362-4c95-ae1f-8d89405b746d",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4813,
  "model_score": 0.4625,
  "style_score": 0.5,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "d0ebe8ed-ec72-4910-8332-7d00504e75ac",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2411,
  "model_score": 0.2044,
  "style_score": 0.2778,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "f086b90d-ccb7-418e-a694-8e2dc28f9193",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5577,
  "model_score": 0.5943,
  "style_score": 0.5212,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "85daafd7-260b-40f1-a07b-b431a45ff35b",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4584,
  "model_score": 0.4998,
  "style_score": 0.4169,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "928b22a5-2d48-4f73-a742-5283bb69b137",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5004,
  "model_score": 0.6401,
  "style_score": 0.3607,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "d254a1f4-35c5-4896-8790-564451bfce17",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5924,
  "model_score": 0.5583,
  "style_score": 0.6265,
  "label": "We couldn't tell whether this was written by a person or with AI. This is not an accusation, and it says nothing about the quality of your writing \u2014 a lot of people's own work lands here. You don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
