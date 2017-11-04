#https://www.hackerrank.com/challenges/np-min-and-max/problem
import numpy

n, m = [int(ele) for ele in raw_input().split(" ")]

a = []
for i in range(n):
    a.append([int(ele) for ele in raw_input().split(" ")])
a = numpy.array(a)

print numpy.max(numpy.min(a, axis=1))
