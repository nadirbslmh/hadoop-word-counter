#!/usr/bin/env python3
"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    for word in words:
        print(f"{word}\t{1}")
