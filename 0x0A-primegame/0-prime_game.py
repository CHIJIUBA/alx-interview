#!/usr/bin/python3

""" Prime Game Algorithm Python """


def createList(y):
    """ Creates a list for the set of numbers"""
    return [x for x in range(1, y + 1)]


def isPrime(x):
    """ Checks if a number given n is a prime number """
    if x >= 2:
        for n in range(2, x):
            if (x % n) == 0:
                return False
        return True
    else:
        return False


def numOfPrime(x):
    """ Calculate all primes """
    num_prime = 0
    for i in range(0, len(x)):
        if isPrime(x[i]):
            num_prime += 1
    return num_prime


def isWinner(x, nums):
    """
    x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """
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
