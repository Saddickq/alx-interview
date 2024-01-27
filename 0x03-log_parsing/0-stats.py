#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""
import re
import sys


try:
    dictionary = {}
    fileSize = 0
    for i, line in enumerate(sys.stdin, start=1):
        segments = line.split()
        try:
            fileSize += int(segments[-1])
            statuses = [200, 301, 400, 401, 403, 404, 405, 500]

            if int(segments[-2]) in statuses:
                if segments[-2] not in dictionary:
                    dictionary[segments[-2]] = 1
                else:
                    dictionary[segments[-2]] += 1
        except Exception as err:
            continue
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
