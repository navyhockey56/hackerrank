#https://www.hackerrank.com/challenges/most-commons/problem
#!/bin/python

import sys

def updateMaxes(occ, max1, max2, max3):
    if max1[0] < occ[0]:
        max3 = max2
        max2 = max1
        max1 = occ
    elif max2[0] < occ[0]:
        max3 = max2
        max2 = occ
    elif max3[0] < occ[0]:
        max3 = occ
    return max1, max2, max3

def myprint(tup):
    print tup[1] + " " + str(tup[0])

if __name__ == "__main__":
    s = raw_input().strip()
    d = {}
    for ch in s:
        d[ch] = d[ch] + 1 if ch in d else 1
    max1, max2, max3 = [(-1, "")] * 3
    for key in d:
        max1, max2, max3 = updateMaxes((d[key], key), max1, max2, max3)
    lst = [max1, max2, max3]
    if max1[0] == max2[0]:
        if max1[0] == max3[0]:
            lst.sort(key = lambda x: x[1])
        elif max1[1] > max2[1]:
            lst = [max2, max1, max3]
    elif max1[0] == max3[0] and max1[1] > max3[1]:
        lst = [max3, max1, max2]
    elif max2[0] == max3[0] and max2[1] > max3[1]:
        lst = [max1, max3, max2]
    for ele in lst:
        myprint(ele)
        
