#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
n = int(raw_input())
marksIndex = filter(lambda x: x != "", raw_input().strip().split(" ")).index("MARKS")    
l = [int(filter(lambda x: x != "", raw_input().strip().split(" "))[marksIndex]) for i in range(n)]
print(round(reduce(lambda x,y: x+y, l) / float(n), 2))
