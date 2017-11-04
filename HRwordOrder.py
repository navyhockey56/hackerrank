#https://www.hackerrank.com/challenges/word-order/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(raw_input())
d = OrderedDict()
for i in range(n):
    line = raw_input()
    d[line] = d[line] + 1 if line in d else 1
    
print len(d)
s = ""
for k in d.keys():
    s += str(d[k]) + " "
print s.strip()
    
