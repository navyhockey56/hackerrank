#https://www.hackerrank.com/challenges/np-array-mathematics/problem
import numpy

n, m = [int(ele) for ele in raw_input().split(" ")]

a, b = [], []
for i in range(n):
    a.append([int(ele) for ele in raw_input().split(" ")])
for i in range(n):
    b.append([int(ele) for ele in raw_input().split(" ")])

a, b = numpy.array(a), numpy.array(b)
print a + b
print a - b
print a * b
print a / b
print a % b
print a ** b
