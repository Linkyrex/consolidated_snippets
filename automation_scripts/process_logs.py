#!/usr/bin/env python3

import re

LOG_PATTERN = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>[^\]]+)\] "(?P<method>\w+) (?P<url>[^ ]+) HTTP/1\.1" (?P<status>\d{3}) (?P<size>\d+)')


def parse_log_line(line):
    m = LOG_PATTERN.match(line)
    if m:
        return m.groupdict()
    return None


def process_log(filepath):
    counts = {}
    with open(filepath, 'r') as f:
        for line in f:
            entry = parse_log_line(line)
            if entry:
                counts[entry['status']] = counts.get(entry['status'], 0) + 1
    return counts


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: process_logs.py <logfile>')
        exit(1)
    counts = process_log(sys.argv[1])
    for status, count in counts.items():
        print(f'Status {status}: {count} hits')
