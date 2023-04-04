#!/usr/bin/python3

def createList(y):
    return [x for x in range(1, y + 1)]


def isPrime(x):
    if x >= 2:
        for n in range(2, x):
            if (x % n) == 0:
                return False
        return True
    else:
        return False


def numOfPrime(x):
    num_prime = 0
    for i in range(0, len(x)):
        if isPrime(x[i]):
            num_prime += 1
    return num_prime


def isWinner(x, nums):
    bwin = 0
    mwin = 0

    for i in range(0, x):
        if (numOfPrime(createList(nums[i]))) % 2 == 0:
            bwin += 1
        else:
            mwin += 1
    if bwin > mwin:
        return "Ben"
    elif bwin == mwin:
        return None
    else:
        return "Maria"
