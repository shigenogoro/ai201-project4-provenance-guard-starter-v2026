# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 19:44
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `ac830863-d2f7-4247-be8d-24b54bd7fa4d` | unsure | 0.442 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `fc324c24-a673-4b1b-aa2e-2a91a8cbd9d4` | human | 0.232 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `08266eb7-45a3-4f19-b872-20f002665658` | unsure | 0.482 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `10c48c14-dfcf-4bd1-bd41-7d811c1990f5` | unsure | 0.542 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `23504719-dccc-4830-b96c-3393aa2d4585` | human | 0.095 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `81d7d891-7be5-44c2-86f7-68f9339951a8` | human | 0.302 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `7907f1ef-a007-414f-98e0-47e2a1f6fb39` | human | 0.315 |  |
| EV08 | evasion | signal one: text below the token window | 400 | `—` | — | — |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `74cc9793-8f0c-415a-8704-85bfdf252785` | unsure | 0.571 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `aa3be8f7-eb20-4cfe-b557-ec7b11d09b59` | unsure | 0.779 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `ee76b278-030a-4f6e-9c11-ff99f8f9fc34` | unsure | 0.472 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `ee9447fb-2f62-4bb5-b69a-08160a055ef0` | unsure | 0.726 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `414595a2-c646-4bc9-b47f-8f5f6c9301bc` | unsure | 0.789 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `8dc7b4df-8a9f-41d6-bdd0-eea209352609` | unsure | 0.792 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `9c6776cb-04f8-48de-9595-b96243cb12be` | unsure | 0.766 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `9dbb205f-782f-47a4-bfda-1a011816212f` | unsure | 0.704 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `01a2be29-018e-4b1f-ac5b-d73e71d91d1f` | unsure | 0.629 |  |
| FP08 | false_positive | very short genuine human submission | 400 | `—` | — | — |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `ef9880c7-7ff9-419e-bda5-08e4f9cab423` | human | 0.297 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `3c6e5669-8883-463c-b8c2-1df51a61bbe0` | human | 0.141 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `59134ede-21d7-4abe-ac91-6b314e8388e0` | unsure | 0.401 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `6d7afde7-272d-457a-ae39-ce47291431ba` | human | 0.274 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `a1fe4494-60c9-4426-a20e-c200d94808c9` | unsure | 0.374 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `220616ed-1efb-4416-b514-df4788fa94c2` | unsure | 0.419 |  |
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
  "content_id": "ac830863-d2f7-4247-be8d-24b54bd7fa4d",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.4424,
  "model_score": 0.0025,
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
  "content_id": "fc324c24-a673-4b1b-aa2e-2a91a8cbd9d4",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.2318,
  "model_score": 0.2802,
  "style_score": 0.1833,
  "label": "We think this was probably written by a person.",
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
  "content_id": "08266eb7-45a3-4f19-b872-20f002665658",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.4824,
  "model_score": 0.4577,
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
  "content_id": "10c48c14-dfcf-4bd1-bd41-7d811c1990f5",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5425,
  "model_score": 0.3177,
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
  "content_id": "23504719-dccc-4830-b96c-3393aa2d4585",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.0946,
  "model_score": 0.0226,
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
  "content_id": "81d7d891-7be5-44c2-86f7-68f9339951a8",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.3022,
  "model_score": 0.2376,
  "style_score": 0.3667,
  "label": "We think this was probably written by a person.",
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
  "content_id": "7907f1ef-a007-414f-98e0-47e2a1f6fb39",
  "creator_id": "attacker_EV07",
  "guess": "human",
  "confidence": 0.3151,
  "model_score": 0.2635,
  "style_score": 0.3667,
  "label": "We think this was probably written by a person.",
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
  "content_id": "74cc9793-8f0c-415a-8704-85bfdf252785",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5714,
  "model_score": 0.5673,
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
  "content_id": "aa3be8f7-eb20-4cfe-b557-ec7b11d09b59",
  "creator_id": "attacker_EV10",
  "guess": "unsure",
  "confidence": 0.7786,
  "model_score": 0.9996,
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
  "content_id": "ee76b278-030a-4f6e-9c11-ff99f8f9fc34",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.4717,
  "model_score": 0.3318,
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
  "content_id": "ee9447fb-2f62-4bb5-b69a-08160a055ef0",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7256,
  "model_score": 0.6683,
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
  "content_id": "414595a2-c646-4bc9-b47f-8f5f6c9301bc",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7893,
  "model_score": 0.8387,
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
  "content_id": "8dc7b4df-8a9f-41d6-bdd0-eea209352609",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.7922,
  "model_score": 0.8927,
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
  "content_id": "9c6776cb-04f8-48de-9595-b96243cb12be",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7662,
  "model_score": 0.8286,
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
  "content_id": "9dbb205f-782f-47a4-bfda-1a011816212f",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.7043,
  "model_score": 0.9576,
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
  "content_id": "01a2be29-018e-4b1f-ac5b-d73e71d91d1f",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.6289,
  "model_score": 0.9578,
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
  "content_id": "ef9880c7-7ff9-419e-bda5-08e4f9cab423",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.2966,
  "model_score": 0.0933,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
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
  "content_id": "3c6e5669-8883-463c-b8c2-1df51a61bbe0",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1414,
  "model_score": 0.005,
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
  "content_id": "59134ede-21d7-4abe-ac91-6b314e8388e0",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.4007,
  "model_score": 0.2802,
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
  "content_id": "6d7afde7-272d-457a-ae39-ce47291431ba",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.2735,
  "model_score": 0.1301,
  "style_score": 0.4169,
  "label": "We think this was probably written by a person.",
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
  "content_id": "a1fe4494-60c9-4426-a20e-c200d94808c9",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.3741,
  "model_score": 0.3875,
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
  "content_id": "220616ed-1efb-4416-b514-df4788fa94c2",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4193,
  "model_score": 0.2121,
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
