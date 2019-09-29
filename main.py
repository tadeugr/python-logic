#!/usr/bin/env python3

import sys
import os
import pprint
pp = pprint.PrettyPrinter(indent=4)

def sortDictKeepIdx():
    myList = {
        "a": 1,
        "b": 2,
        "c": 3
    }

    auxList = []
    for item in myList:
        auxList.append((item, myList[item]))
    
    auxListLen = len(auxList)
    for i in range(0, auxListLen):
        for j in range(0, auxListLen):
            if auxList[i] > auxList[j]:
                tmp = auxList[j]
                auxList[j] = auxList[i]
                auxList[i] = tmp
    print("-----")
    print(auxList)
    print("-----")

    keepIdx = {}
    for item in auxList:
        keepIdx[item[0]] = item[1]
    print("-----")
    print(keepIdx)
    print("-----")

def main():
    sortDictKeepIdx()
    print(input())

if __name__ == "__main__":
    main()