#!/usr/bin/env python3

# no-idea
# https://www.hackerrank.com/challenges/no-idea/problem

import sys
import os
import math
import pprint
pp = pprint.PrettyPrinter(indent=4)

def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

def JumpSearch (lys, val):
    length = len(lys)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and lys[left] <= val:
        right = min(length - 1, left + jump)
        if lys[left] <= val and lys[right] >= val:
            break
        left += jump;
    if left >= length or lys[left] > val:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and lys[i] <= val:
        if lys[i] == val:
            return i
        i += 1
    return -1

def FibonacciSearch(lys, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys)-1))
        if (lys[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1] == val):
        return index+1;
    return -1


def main():
    line = input().split(" ")
    n, m = [i for i in line]

    elements = input().split(" ")
    a = input().split(" ")
    b = input().split(" ")
    hapiness = 0

    """ print('--------------')
    print(len(elements))
    print(len(a))
    print(len(b))

    print('--------------')
    sys.exit() """

    a.sort()
    b.sort()

    for element in elements:
        #result = BinarySearch(a, element)
        #result = JumpSearch(a, element)
        result = FibonacciSearch(a, element)
        if result != -1:
            hapiness += 1

        result = BinarySearch(b, element)
        if result != -1:
            hapiness -= 1

    print(hapiness)


if __name__ == "__main__":
    main()