#https://www.hackerrank.com/challenges/np-dot-and-cross/problem
import numpy

n = int(raw_input())

a = []
for i in range(n):
    a.append([int(ele) for ele in raw_input().split(" ")])
a = numpy.array(a)

b = []
for i in range(n):
    b.append([int(ele) for ele in raw_input().split(" ")])
b = numpy.array(b).transpose()

c = []
for i in range(n):
    c.append([])   
    for j in range(n):
        c[i].append(numpy.dot(a[i], b[j]))

print numpy.array(c)
