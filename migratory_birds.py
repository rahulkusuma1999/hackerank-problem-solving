


 '''
     problem statement :: https://www.hackerrank.com/challenges/migratory-birds/problem

'''

import math
import os
import random
import re
import sys


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    a = arr.count(1)
    b = arr.count(2)
    c = arr.count(3)
    d = arr.count(4)
    e = arr.count(5)
    li = [a, b, c, d, e]
    return print(1 + li.index(max(li)))


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)


