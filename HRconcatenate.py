#https://www.hackerrank.com/challenges/np-concatenate/problem
import numpy

n, m, p = [int(ele) for ele in raw_input().split(" ")]

matrix1 = []
matrix2 = []

for i in range(n):
    matrix1.append([int(ele) for ele in raw_input().split(" ")])
    
for i in range(m):
    matrix2.append([int(ele) for ele in raw_input().split(" ")])
    
matrix1 = numpy.array(matrix1)
matrix2 = numpy.array(matrix2)
print numpy.concatenate((matrix1, matrix2), axis = 0)
