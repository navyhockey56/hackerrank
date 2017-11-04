#https://www.hackerrank.com/challenges/py-check-strict-superset/problem
def isSubset(a, b):
    return len(a) < len(b) and reduce(lambda x ,y: x and (y in b), a, True)

def isSuper(a, b):
    return reduce(lambda x,y: x or (not y in b), a, False) and isSubset(b, a)

a = raw_input().split(" ")
n = int(raw_input())
isScriptSuper = True
for i in range(n):
    isScriptSuper = isScriptSuper and isSuper(a, raw_input().split(" "))
print isScriptSuper
