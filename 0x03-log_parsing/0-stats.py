#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys
import signal
from typing import Dict


def print_stats(_: int, __: int) -> None:
    """Signal handler function to print statistics.

    Prints the total file size and the number of lines with each
    status code, sorted in ascending order.

    Args:
        signum (int): The signal number (ignored).
        frame: The current stack frame (ignored).
    """
    global total_size, status_counts

    print("Total file size:", total_size)
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


signal.signal(signal.SIGINT, print_stats)

total_size: int = 0
status_counts: Dict[int, int] = {}

for i, line in enumerate(sys.stdin):
    line = line.strip()

    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])
    except BaseException:
        continue

    total_size += file_size
    status_counts[status_code] = status_counts.get(status_code, 0) + 1

    if (i + 1) % 10 == 0:
        print_stats(None, None)

print_stats(None, None)
