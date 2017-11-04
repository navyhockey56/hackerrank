#https://www.hackerrank.com/challenges/np-sum-and-prod/problem
import numpy

n, m = [int(ele) for ele in raw_input().split(" ")]

a = []
for i in range(n):
    a.append([int(ele) for ele in raw_input().split(" ")])
a = numpy.array(a)
a = numpy.sum(a, axis=0)
print numpy.prod(a)
