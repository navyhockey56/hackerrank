#https://www.hackerrank.com/challenges/np-eye-and-identity/problem
import numpy

n, m = [int(ele) for ele in raw_input().split(" ")]
print numpy.eye(n, m)
