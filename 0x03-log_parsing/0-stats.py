#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys
import re


status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0}

total_size = 0

while True:
    for line in sys.stdin:
        match = re.search(r'^(\S+) - \[(.*?)\] "(.*?)" (\d+) (\S+)', line)

        if match:
            try:
                status = match.group(4)
                size = match.group(5)

                if status in status_counts:
                    status_counts[status] += 1
                    total_size += size

            except ValueError:
                continue

    print('File size: %d' % total_size)
    for key in sorted(status_counts):
        print('%d: %d' % (key, status_counts[key]))
