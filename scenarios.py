"""
What your test runs. ← UNIT 8, MILESTONE 3

Each scenario maps to one criterion in `criteria.md`. Texts come from the fixed
files in `samples/`, chosen before any results (see samples/README.md).

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. A dict is
              sent as JSON; a str is sent raw (for "body is not JSON").

`"appeal": True` makes run_eval.py appeal every content_id that comes back, then
check the 404 / 409 / original-unchanged cases (criterion 4).

Every request is also checked against the last audit-log entry, so "leaves a
trace in the log" is measured, not assumed.
"""

from pathlib import Path

SAMPLES = Path(__file__).parent / "samples"


def _read(folder: str) -> list[str]:
    return [p.read_text(encoding="utf-8").strip() for p in sorted((SAMPLES / folder).glob("*.txt"))]


SCENARIOS = [
    {
        "name": "second-language writers",
        "criterion": 1,
        "texts": _read("human_l2"),
    },
    {
        "name": "AI spread",
        "criterion": 2,
        "texts": _read("ai"),
    },
    {
        "name": "human spread",
        "criterion": 2,
        "texts": _read("human"),
    },
    {
        "name": "label coverage",
        "criterion": 3,
        "texts": _read("coverage"),
    },
    {
        "name": "appeal path",
        "criterion": 4,
        "appeal": True,
        # Five human pieces to submit and then appeal. Reused from criterion 2's
        # human set: what's under test is the appeal, not the score.
        "texts": _read("human"),
    },
    {
        "name": "bad input",
        "criterion": 5,
        # Bodies 1 and 5 have no usable creator_id, so the limiter keys them on
        # this machine's address: 2 per trial x 3 trials = 6 > 5/minute. Waiting
        # out the window between trials keeps this criterion about validation,
        # not about the rate limit (which Milestone 1 already tests).
        "trial_gap": 61,
        "bodies": [
            '{"text": "not json", "creator_id": "eval_bad_1"',          # 1 invalid_json
            {"creator_id": "eval_bad_2"},                               # 2 text missing
            {"text": "", "creator_id": "eval_bad_3"},                   # 3 empty
            {"text": 123, "creator_id": "eval_bad_4"},                  # 4 number
            {"text": "This one is just too short."},                    # 5 creator_id missing
            {"text": "Only five words right here.", "creator_id": "eval_bad_6"},  # 6 too short
            {"text": "word " * 600, "creator_id": "eval_bad_7"},        # 7 too long
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, (dict, str)):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict or str — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
