# the-minion-game
# https://www.hackerrank.com/challenges/the-minion-game/problem

import sys
import re

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

def minion_game(string):
    stuartPoints = 0 # consonants
    kevinPoints = 0 # vowels

    vowels = ["A","E","I","O","U"]

    vSeq = []
    cSeq = []

    for i in range(0, len(string)):
        letter = string[i]
        auxVSeq = ""
        auxCSeq = ""
        for j in range(i, len(string)):
            if letter in vowels:       
                auxVSeq += string[j]
                if auxVSeq not in vSeq:
                    vSeq.append(auxVSeq)
            else:
                auxCSeq += string[j]
                if auxCSeq not in cSeq:
                    cSeq.append(auxCSeq)
    for c in vSeq:
        substrCount = occurrences(string, c)
        #print("%s occurs %s times in %s" % (c, substrCount, string) )
        kevinPoints += substrCount
    #print("-------")
    for c in cSeq:
        #print("%s occurs %s times in %s" % (c, substrCount, string) )
        substrCount = occurrences(string, c)
        stuartPoints += substrCount
    
    if stuartPoints == kevinPoints:
        print("Draw")
        sys.exit()
    if stuartPoints > kevinPoints:
        print("Stuart %s" % stuartPoints)
    else:
        print("Kevin %s" % kevinPoints)
    
    sys.exit()


if __name__ == '__main__':
    s = input()
    minion_game(s)