#!/usr/bin/python3

import sys
import signal

# Define a signal handler function to print statistics
def print_stats(signum, frame):
    global total_size, status_counts

    print("Total file size:", total_size)
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


# Set the signal handler for SIGINT (CTRL+C)
signal.signal(signal.SIGINT, print_stats)

# Initialize counters
total_size = 0
status_counts = {}

# Read input from standard input line by line
for i, line in enumerate(sys.stdin):
    line = line.strip()

    # Parse line and extract file size and status code
    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])
    except:
        continue

    # Update counters
    total_size += file_size
    status_counts[status_code] = status_counts.get(status_code, 0) + 1

    # Print statistics every 10 lines
    if (i + 1) % 10 == 0:
        print_stats(None, None)

# Print final statistics
print_stats(None, None)
