#https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
    n = len(string)
    m = n/k
    t = []
    i = 0
    curr = 0
    for i in range(m):
        t.append("")
        for j in range(k):
            ch = string[curr]
            t[i] = t[i] if ch in t[i] else t[i] + ch
            curr = curr + 1
    for ele in t:
        print ele
        
