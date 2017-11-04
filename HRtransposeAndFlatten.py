#https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
import numpy

n, m = [int(ele) for ele in raw_input().split(" ")]

matrix = []
for i in range(n):
    matrix.append([int(ele) for ele in raw_input().split(" ")])

matrix = numpy.array(matrix)
print matrix.transpose()
print matrix.flatten()
