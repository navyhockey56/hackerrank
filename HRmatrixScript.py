#https://www.hackerrank.com/challenges/matrix-script/problem
#!/bin/python

import sys
import re

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
matrix = []
matrix_i = 0
messageMatrix = []
for matrix_i in xrange(n):
    matrix_t = str(raw_input())
    matrix.append(matrix_t)

messageMatrix = []
for i in range(m):
    messageMatrix.append([])

for rowPos in range(n):
    for colPos in range(m):
        messageMatrix[colPos].insert(rowPos, matrix[rowPos][colPos])
            
message = ""
for list in messageMatrix:
    for ch in list:
        message += ch

def matches(reg, message):
    return re.match(reg, message) != None

startOfMessage, endOfMessage = 0, len(message)
while endOfMessage >= startOfMessage and matches(r'[^\w]+', message[startOfMessage:]):
    startOfMessage += 1
while startOfMessage < endOfMessage and matches(r'.*[^\w+]$', message[startOfMessage:endOfMessage]):
    endOfMessage -= 1

subMessage = message[startOfMessage:endOfMessage]
subMessage = re.sub(r'[^\w]', " ", subMessage)
subMessage = re.sub(r'\s+', " ", subMessage)

formattedMessage = str(message[:startOfMessage] + subMessage + message[endOfMessage:])
print formattedMessage
    
            
        
