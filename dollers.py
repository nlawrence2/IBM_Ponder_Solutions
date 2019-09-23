import operator as op
from functools import reduce
import math
import itertools
import numpy as np

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def find_subset(number, banknotes):
    subset = []
    for bill in banknotes:
        if math.floor(number / bill) != 0:
            subset.append(bill)
            number -= math.floor(number / bill) * bill
    if number > 0:
        return "Bad Banknotes!"
    return str(subset)

def probability(banknotes):
    banknotes = banknotes + list(reversed(range(21,86))) + [1]
    print("Banknotes:", banknotes)
    subsets = dict()
    probability = 0
    for number in range(100):
        subset = find_subset(number, banknotes)
        subsets[subset] = subsets.get(subset, 0) + 1
    for subset in subsets:
        value = subsets[subset]
        probability += value*(value-1)
    return probability / 9900

def cool_number(number):
    return number*(number-1)

def find_combinations():
    cool_numbers = []
    for i in range(2,21):
        cool_numbers.append(cool_number(i))
    for vector in itertools.combinations_with_replacement(range(5), 19):
            print(vector)
            sum = np.inner(vector, cool_numbers)
            if sum < 400:
                print(sum)
            if sum == 396:
                print(sum)


print(probability([97,94,90,86]))