"""Entry for make.fun bounty "The Best Meal You Ever Had".

Entry text (159 characters, limit: at most 200 characters).
No trailing newline is written, per the bounty text format.
"""

import os

ENTRY = "Grandma's fried rice at midnight, eaten straight from the wok as rain drummed the roof - no plate, no manners, just smoke, chili, and the best meal of my life."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
