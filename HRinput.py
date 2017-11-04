#https://www.hackerrank.com/challenges/input/problem
x, k = raw_input().split(" ")
print eval(raw_input().replace("x", str(x))) == int(k)
