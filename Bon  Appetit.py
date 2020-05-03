import math
import os
import random
import re
import sys

'''

https://www.hackerrank.com/challenges/bon-appetit/problem


'''




# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    inc = sum(bill)
    bill.pop(k)
    summation = sum(bill)

    actualpayed = summation / 2
    if actualpayed == b:
        return print('Bon Appetit')
    else:
        return print(abs(int(actualpayed - b)))


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
