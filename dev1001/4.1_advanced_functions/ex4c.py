# reduce() Exercise
#
# Given a list of booleans, use reduce() and a lambda to determine if
# at least one of the values in the list is True.
# Test it with all 3 lists.
from functools import reduce

flags1 = [True, False, True, True]
flags2 = [False, False]
flags3 = []

test1 = reduce(lambda acc, current: acc or current == True, flags1, False)
print(f'Test results: {test1}')

test2 = reduce(lambda acc, current: acc or current == True, flags2, False)
print(f'Test results: {test2}')

test3 = reduce(lambda acc, current: acc or current == True, flags3, False)
print(f'Test results: {test3}')