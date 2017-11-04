#https://www.hackerrank.com/challenges/any-or-all/problem
n = int(raw_input())
lst = map(int,raw_input().strip().split(' '))
print all(map(lambda x: x > 0, lst)) and any(map(lambda x: str(x) == str(x)[::-1], lst))
