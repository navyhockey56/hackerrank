#https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    vowels = "AEIOU"
    sScore, kScore = 0, 0
    length = len(string)
    for i in range(length):
        ch = string[i]
        if ch in vowels:
            kScore += length - i
        else:
            sScore += length - i
    if sScore == kScore:
        print "Draw"
    elif sScore > kScore:
        print "Stuart " + str(sScore)
    else:
        print "Kevin " + str(kScore)
