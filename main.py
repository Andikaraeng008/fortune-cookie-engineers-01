"""Fortune Cookie Funnies for Engineers — one-line entry.

Writes the fortune cookie message for a software engineer to the
grader's output file. The line is one fortune (120 characters at most),
short and declarative, with its twist in the final words.
Candidate F1 (dark, 106 characters) — chosen by Ahmad.
"""
import os

LINE = "Your code will outlive you. The bug you didn't write already has your name on it. Lucky numbers: 404, 500."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
