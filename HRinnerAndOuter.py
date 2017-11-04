#https://www.hackerrank.com/challenges/np-inner-and-outer/problem
import numpy

a = numpy.array([int(ele) for ele in raw_input().split(" ")])
b = numpy.array([int(ele) for ele in raw_input().split(" ")])
print numpy.inner(a, b)
print numpy.outer(a, b)
