'''

        https://www.hackerrank.com/challenges/day-of-the-programmer/problem

'''

import math
import os
import random
import re
import sys


# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if (year == 1918):
        return print("26.09.1918")
    if year in range(1700, 1917):
        if year % 4 == 0:
            return print("12.09.{}".format(year))
        else:
            return print("13.09.{}".format(year))
    if year in range(1917, 2701):
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):

            return print("12.09.{}".format(year))
        else:
            return print("13.09.{}".format(year))


if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)

