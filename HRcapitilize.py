#https://www.hackerrank.com/challenges/capitalize/problem
def capitalize(string):
    return reduce(lambda x, y: x + " " + (str.upper(y[0]) + y[1:] if y != "" else y), string.split(" "), "")[1:]
