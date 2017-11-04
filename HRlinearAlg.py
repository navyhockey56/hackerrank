#https://www.hackerrank.com/challenges/np-linear-algebra/problem
import numpy

n= int(raw_input())

a = []
for i in range(n):
    a.append([float(ele) for ele in raw_input().split(" ")])
a = numpy.array(a)
print numpy.linalg.det(a)
