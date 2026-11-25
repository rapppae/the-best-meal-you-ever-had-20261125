"""Entry for make.fun bounty "The Best Meal You Ever Had".

Entry text (160 characters, limit: at most 200 characters).
No trailing newline is written, per the bounty text format.
"""

import os

ENTRY = "The best meal I ever had was my grandmother's fried rice at midnight, eaten straight from the wok while rain drummed the roof and nobody told me to use a plate."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
