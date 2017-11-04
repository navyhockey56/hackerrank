#https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = [int(ele) for ele in raw_input().split(" ")]
d = defaultdict(list)
for i in range(1, n+1):
    d[raw_input()].append(str(i))
for i in range(m):
    ele = raw_input()
    if ele in d:
        print reduce(lambda x, y: x + " " + y, d.get(ele))
    else:
        print "-1"
