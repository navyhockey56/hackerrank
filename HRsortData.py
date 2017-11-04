#https://www.hackerrank.com/challenges/python-sort-sort/problem
#!/bin/python

import sys

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = []
    for arr_i in xrange(n):
        arr_temp = map(int,raw_input().strip().split(' '))
        arr.append(arr_temp)
    k = int(raw_input().strip())
    arr.sort(key=lambda x: x[k])
    for i in range(n):
        print reduce(lambda x, y: x + " " + str(y), arr[i], "").strip()
