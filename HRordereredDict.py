#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
from collections import OrderedDict
n = int(raw_input())
d = OrderedDict()
for i in range(n):
    line = raw_input().split(" ")
    item = reduce(lambda x,y: x + " " + y, line[0:len(line) - 1])
    price = int(line[len(line) - 1])
    if item in d.keys():
        d[item] += int(price)
    else: 
        d[item] = int(price)
for k in d.keys():
    print k + " " + str(d[k])
