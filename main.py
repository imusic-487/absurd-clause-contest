"""The Absurd Clause Contest — entry program.

Writes one absurd terms-of-service clause, a single English sentence,
to /output/entry.txt. Deterministic, standard library only: no network,
no randomness, no environment input.

The clause is deadpan legal boilerplate until the absurdity hits:
a user who dies mid-session still owes the Service ninety days of
customer-support duty — from beyond the grave.
"""

from pathlib import Path

ENTRY = (
    "Should the user die while using the Service, their ghost agrees "
    "to remain on call for customer support for ninety (90) days."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main():
    # The gate allows 1-200 characters, a single line, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry outside the 1-200 character gate"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
