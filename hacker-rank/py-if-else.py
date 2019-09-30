#!/bin/python3

# https://www.hackerrank.com/challenges/py-if-else/problem

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    isOdd = False
    if n % 2 != 0:
        isOdd = True

    if isOdd:
        print("Weird")
        sys.exit()
    
    if n >= 2 and n <= 5:
        print("Not Weird")
        sys.exit()
    
    if n >= 6 and n <= 20:
        print("Weird")
        sys.exit()
    
    if n > 20:
        print("Not Weird")
        sys.exit()