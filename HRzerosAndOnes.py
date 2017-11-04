#https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
import numpy

shape = tuple([int(ele) for ele in raw_input().split(" ")])
print numpy.zeros(shape, dtype = numpy.int)
print numpy.ones(shape, dtype = numpy.int)
