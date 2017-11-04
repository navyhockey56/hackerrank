#https://www.hackerrank.com/challenges/hex-color-code/problem
import re

def matches(r, s):
    return re.match(r, s) != None

n = int(raw_input())
r1 = "(#\w{3}\s*\{{0,1}$)|(#\w{6}\s*\{{0,1}$)"
r2 = ".*(#\w{3})|(#\w{6})"

lst = []
for i in range(n):
    line = raw_input().strip()
    if not matches(r1, line) and matches(r2, line):
        i = 0
        while i < len(line):
            ch = line[i]
            if ch == "#":
                code = "#"
                i += 1
                cont = True
                while i < len(line) and cont:
                    ch = line[i]
                    if ch.lower() in "0123456789abcdef":
                        code += ch
                    else:
                        cont = False
                    i += 1
                if len(code) == 4 or len(code) == 7:
                    lst.append(code)
            else:
                i += 1
                              
for ele in lst:
    print ele
    
