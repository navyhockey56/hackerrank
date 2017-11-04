#https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
import numpy

m = numpy.array([float(ele) for ele in raw_input().split(" ")])
print numpy.floor(m)
print numpy.ceil(m)
print numpy.rint(m)
