#https://www.hackerrank.com/challenges/py-collections-deque/problem
from collections import deque
n = int(raw_input())
d = deque()
for i in range(n):
    line = raw_input().split(" ")
    if len(line) == 1:
        action = line[0]
        if action == "pop":
            d.pop()
        else:
            d.popleft()
    else:
        action, ele = line
        if action == "append":
            d.append(ele)
        else:
            d.appendleft(ele)
print reduce(lambda x,y: x + " " + y, d)
        
