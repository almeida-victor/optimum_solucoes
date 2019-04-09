#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    a = " "
    b = "#"
    c = ""
    k = 1
    while n >=1:
        for i in range(n-1):
            c = c + a
        for j in range(k):
            c = c + b
        k = k+1
        n = n-1
        print(c)
        c = ""

if __name__ == '__main__':
    n = int(input())

    staircase(n)
