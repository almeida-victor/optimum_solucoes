#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    i = sum(arr)
    mymin = i - arr[-1]
    mymax = i - arr[0]
    mylist = [mymin,mymax]
    return print(*mylist)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
