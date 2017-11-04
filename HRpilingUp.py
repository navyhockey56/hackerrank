#https://www.hackerrank.com/challenges/piling-up/problem
def isInOrder(lst):
    return True if len(lst) == 0 else (0 != reduce(lambda x, y: 0 if x < y else y, lst, lst[0]))

n = int(raw_input())

for i in range(n):
    numOfCudes = int(raw_input())
    cubes = [int(ele) for ele in raw_input().split(" ")]
    minLocation = cubes.index(min(cubes))
    head = cubes[:minLocation]
    tail = cubes[minLocation:]
    tail.reverse()
    if isInOrder(head) and isInOrder(tail):
        print "Yes"
    else:
        print "No"
