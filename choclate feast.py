import math
import os
import random
import re
import sys


# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    choc = n // c
    wrap = choc
    while (choc >= m):
        wrap += choc // m
        choc = choc // m + choc % m
    return wrap


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
