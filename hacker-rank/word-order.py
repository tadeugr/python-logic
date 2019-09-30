#!/usr/bin/env python3

# word-order
# https://www.hackerrank.com/challenges/word-order/problem

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

def countOccurrences(arr, n, x): 
    res = 0
    for i in range(n): 
        if x == arr[i]: 
            res += 1
    return res 

def main():
    n = int(input())
    strings = []
    distincts = {}
    for i in range (0, n):
        string = str(input())
        strings.append(string)
        distincts[string] = string

    strings.sort()
    counts = []
    for distinct in distincts:
        #count = countOccurrences(strings, len(strings), distinct)
        idx = 0
        count = 0
        auxStrings = strings
        while True:
            idx = FibonacciSearch(strings, distinct)
            if idx == -1:
                break
            del auxStrings[idx]
            count += 1
        counts.append(str(count))

    print(len(distincts))
    print(" ".join(counts))


if __name__ == "__main__":
    main()