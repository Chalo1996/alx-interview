#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""


import sys
import re

total_size = 0  # total size of all files
num_lines_by_status_code = {}

# Read stdin line by line
for line in sys.stdin:
    line = sys.stdin.readline()
    match = re.search(r'^ (\S + ) - \[(.*?)\] "(.*?)" (\d+) (\S + )', line)
    if match:
        status_code = match.group(4)
        file_size = match.group(5)
        if not status_code.isdigit():
            continue

        # Sum up file sizes for each valid line
        file_size = int(file_size)
        total_size += file_size

        # Increment number of lines by status code
        if status_code not in num_lines_by_status_code:
            num_lines_by_status_code[status_code] = 0
        num_lines_by_status_code[status_code] += 1

        # Print the output after every 10 lines or a keyboard interruption
        if (sys.stdin.readline() % 10 == 0) and sys.stdin.isatty():
            print("Total file size: {}".format(total_size))
            for k, v in sorted(num_lines_by_status_code.items()):
                print("{}: {}".format(k, v))
