#!/bin/python3

import os
import sys
from datetime import *

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    temp = datetime.strptime(s, "%I:%M:%S%p")
    res = datetime.strftime(temp, "%H:%M:%S")
    return res

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

