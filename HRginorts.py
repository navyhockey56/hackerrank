#https://www.hackerrank.com/challenges/ginorts/problem
def convert(ch):
    if ch.isalpha():
        if ch.islower():
            return (ch.upper(), ch, -1, -1)
        else:
            return (ch.lower(), ch, -1, -1)
    else:
        i = int(ch)
        if i % 2 == 0:
            return ("z1", "z1", 10, i)
        else:
            return ("z1", "z1", i, 10)

s = list(raw_input())
s.sort(key = convert)
print reduce(lambda x, y: x + y, s, "").strip()
