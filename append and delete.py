'''

 problem statement ::  https://www.hackerrank.com/challenges/append-and-delete/problem


'''





import math
import os
import random
import re
import sys


# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    s_length = len(s)
    t_length = len(t)

    if s_length + t_length < k: return 'Yes'

    same = 0
    for s_l, t_l in zip(s, t):
        if s_l == t_l:
            same += 1
        else:
            break

    extra_s = s_length - same
    extra_t = t_length - same
    difference = extra_s + extra_t

    if difference <= k and difference % 2 == k % 2: return 'Yes'
    return 'No'


if __name__ == '__main__':
    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)
    print(result)
