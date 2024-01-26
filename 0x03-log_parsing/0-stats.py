#!/usr/bin/env python3
"""A script that reads stdin line by line and computes metrics"""
import re
import sys


def check_api(line):
    """check api method"""
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
    r'\[([^\]]+)\] "GET \/projects\/260 HTTP\/1.1" (\d{3}) (\d+)$'
    api = re.match(pattern, line)
    return True if api else False

try:
    dictionary = {}
    fileSize = 0
    for i, line in enumerate(sys.stdin, start=1):
        if not check_api(line):
            continue
        segments = line.split()
        try:
            fileSize += int(segments[-1])
        except Exception as err:
            pass
        if segments[-2] not in dictionary:
            dictionary[segments[-2]] = 1
        else:
            dictionary[segments[-2]] += 1
        my_dict = dict(sorted(dictionary.items()))
        if i % 10 == 0:
            print(f"File size: {fileSize}")
            for key, value in my_dict.items():
                print(f"{key}: {value}")
except KeyboardInterrupt:
    pass
finally:
    print(f"File size: {fileSize}")
    for key, value in my_dict.items():
        print(f"{key}: {value}")
