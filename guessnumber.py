import random
random = random.SystemRandom()
print(random)
r=random.random()
print(r)
print(r - 1e-8 / 2)
print(r + 1e-8 / 2)


def guessnumber(guessnum, randnum):
    guessnum = float(guessnum)
    isLess = guessnum < randnum - 1e-8 / 2;
    isMore = guessnum > randnum + 1e-8 / 2;
    isPass = False
    if not isMore and not isLess:
        isPass = True
    return isLess, isMore, isPass

guess="NaN"

Less,More,Pass = guessnumber(guess,r)
print(Less)
print(More)
print(Pass)