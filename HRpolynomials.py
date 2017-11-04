#https://www.hackerrank.com/challenges/np-polynomials/problem
import numpy

print numpy.polyval([float(ele) for ele in raw_input().split(" ")], float(raw_input()))
