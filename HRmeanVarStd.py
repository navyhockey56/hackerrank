#https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
import numpy

n, m = [int(ele) for ele in raw_input().split(" ")]

a = []
for i in range(n):
    a.append([int(ele) for ele in raw_input().split(" ")])
a = numpy.array(a)

print numpy.mean(a, axis=1)
print numpy.var(a, axis=0)
print numpy.std(a)
