"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

# Calibration, read off the 30 samples (see README). Each range is
# (human end, AI end): the raw value that maps to 0.0 and to 1.0.
SPREAD_RANGE = (0.60, 0.20)   # sample means: human ~0.6, AI ~0.27
TTR_RANGE = (0.70, 0.90)      # sample means: human ~0.78, AI ~0.84
PUNCT_RANGE = (3.0, 0.0)      # sample means: human ~1.8-3.0, AI ~0.8
TTR_WINDOW = 60

# Spread separates best; TTR's gap is small, so it counts least.
STYLE_WEIGHT_SPREAD = 0.5
STYLE_WEIGHT_TTR = 0.2
STYLE_WEIGHT_PUNCT = 0.3

def sentence_length_spread(text: str) -> float | None:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.

    Decided: coefficient of variation (stdev / mean). LOW = more AI-like.
    One sentence returns None: "can't measure" must not count as evidence,
    so style_signal treats it as neutral.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    if len(lengths) < 2:
        return None
    return statistics.stdev(lengths) / statistics.mean(lengths)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.

    Decided: computed on the first TTR_WINDOW words only, so length doesn't
    leak in. Direction is the OPPOSITE of the usual assumption — on my samples
    AI scored higher (≈0.84) than human (≈0.78): AI reaches for many distinct
    "polished" words, people repeat function words. HIGH = more AI-like.
    """
    ws = words(text)[:TTR_WINDOW]
    return len(set(ws)) / len(ws) if ws else 0.0


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.

    Decided: only the "rich" marks — ; : ( ) and dashes — per 100 words.
    Total punctuation scored ~14 for AI, human and L2 alike: no signal.
    LOW = more AI-like. Known cost: the L2 samples use none of these at all.
    """
    ws = words(text)
    marks = re.findall(r"[;:()—–-]", text)
    return 100 * len(marks) / len(ws) if ws else 0.0


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.
    """
    parts = [
        (STYLE_WEIGHT_SPREAD, _scale(sentence_length_spread(text), *SPREAD_RANGE)),
        (STYLE_WEIGHT_TTR, _scale(type_token_ratio(text), *TTR_RANGE)),
        (STYLE_WEIGHT_PUNCT, _scale(punctuation_density(text), *PUNCT_RANGE)),
    ]
    return round(sum(w * v for w, v in parts), 4)


def _scale(value, human_end: float, ai_end: float) -> float:
    """Map a raw measure onto 0 (human end) .. 1 (AI end), clamped. None -> 0.5."""
    if value is None:
        return 0.5
    return min(max((value - human_end) / (ai_end - human_end), 0.0), 1.0)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
