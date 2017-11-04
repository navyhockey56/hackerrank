#https://www.hackerrank.com/challenges/triangle-quest-2/problem
for i in range(1,int(raw_input())+1): 
    print reduce(lambda x, y: x*10 + y, range(1,i) + list(reversed(range(1,i+1))), 0)
