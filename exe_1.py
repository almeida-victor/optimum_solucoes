#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    a = 0;

    if n == 0:
        a = 1
    elif n == 1:
        a = 2
    elif (n%2) != 0:
        while n > 1:
            a = int(a + 2**(int(n/2) + 1))
            n = n - 2
        a = int(a + 2)
    else:
        while n > 1:
            a = int(a + 2**(int(n/2)))
            n = n -2
        a = int(a + 1)
    return a





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
