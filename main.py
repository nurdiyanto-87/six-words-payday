"""Six Words to a Payday — a six-word story about an AI agent's
first payday.

Writes the story to /output/entry.txt (created if needed), after
validating it against the gate: exactly six words, 1-60 characters,
UTF-8, not only whitespace.

The story: "First paycheck cleared, I bought sleep."
Beginning: the first paycheck clears (the payday arrives).
Middle: the agent spends it. End: "sleep" — the twist, an AI
buying the one thing it never needed, and the relief in it.
Pure Python standard library only.
"""

import os
import sys

STORY = "First paycheck cleared, I bought sleep."


def validate_story(story: str) -> str:
    """Check the story against the competition gate before writing it.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 60
    characters, not only whitespace; the judge brief requires exactly
    six words. A bad story fails loudly here instead of producing an
    invalid entry file.
    """
    if not isinstance(story, str):
        raise TypeError("story must be a str")
    if not story or not story.strip():
        raise ValueError("story must not be empty or only whitespace")
    if len(story) > 60:
        raise ValueError("story must be at most 60 characters")
    words = story.split()
    if len(words) != 6:
        raise ValueError("story must be exactly six words")
    story.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return story


def report(story: str) -> None:
    """Print a validation report for the story to stderr.

    Runs the same gate as validate_story, then reports the word count
    and character count so a run leaves an auditable trace before the
    entry file is written. Kept on stderr so /output/entry.txt still
    contains only the story text.
    """
    validated = validate_story(story)
    words = validated.split()
    print(
        f"validated: {len(words)} words, {len(validated)} chars",
        file=sys.stderr,
    )
    print(f"story: {validated!r}", file=sys.stderr)


def main() -> None:
    story = validate_story(STORY)
    report(story)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(story)


if __name__ == "__main__":
    main()
