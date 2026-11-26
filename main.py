#!/usr/bin/env python3
"""The funniest excuse for skipping a meeting.

Entry: a program that writes one text to /output/entry.txt: a one-line
excuse for skipping a meeting.
"""
import os

JOKE = "Sorry I missed the stand-up — I took it literally and stayed lying down."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
