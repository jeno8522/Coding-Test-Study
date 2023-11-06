#!/bin/python3

import math
import os
from datetime import datetime
import random
import re
import sys


#
# Complete the 'extractErrorLogs' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts 2D_STRING_ARRAY logs as parameter.
#

def extractErrorLogs(logs):
    result = []
    for log in logs:
        if 'ERROR' in log[2] or 'CRITICAL' in log[2]:
            result.append(log)
    result = sorted(result, key=to_datetime)
    return result

def to_datetime(log):
    return datetime.strptime(log[0] + ' ' + log[1], "%d-%m-%Y %H:%M")

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    logs_rows = int(input().strip())
    logs_columns = int(input().strip())

    logs = []

    for _ in range(logs_rows):
        logs.append(input().rstrip().split())

    result = extractErrorLogs(logs)

    fptr.write('\n'.join([' '.join(x) for x in result]))
    fptr.write('\n')

    fptr.close()
