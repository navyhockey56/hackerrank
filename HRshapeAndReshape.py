#https://www.hackerrank.com/challenges/np-shape-reshape/problem
import numpy

input = numpy.array([int(ele) for ele in raw_input().split(" ")])
input.shape = (3,3)

print input

