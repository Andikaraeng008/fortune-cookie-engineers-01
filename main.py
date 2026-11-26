"""Fortune Cookie Funnies for Engineers — one-line entry.

Writes the fortune cookie message for a software engineer to the
grader's output file. The line is one fortune (120 characters at most),
short and declarative, with its twist in the final words.
"""
import os

LINE = "You will deploy on Friday at 5 p.m. The server will forgive you. Your on-call phone will not."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
