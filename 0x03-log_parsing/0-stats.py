#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys
import signal
from typing import Dict

total_size = 0
status_counts = {}


def print_stats(signum, frame):
    """Prints statistics for the current state of the program."""
    print("Total file size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))


signal.signal(signal.SIGINT, print_stats)

for i, line in enumerate(sys.stdin):
    line = line.strip()

    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])
    except:
        continue

    total_size += file_size
    status_counts[status_code] = status_counts.get(status_code, 0) + 1

    if (i + 1) % 10 == 0:
        print_stats(None, None)

print_stats(None, None)
