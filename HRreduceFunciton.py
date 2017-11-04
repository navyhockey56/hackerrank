#https://www.hackerrank.com/challenges/reduce-function/problem
def product(fracs):
    t = reduce(lambda x, y : x * y, fracs, Fraction(1,1))
    print(str(t.numerator) +  " " + str(t.denominator))
