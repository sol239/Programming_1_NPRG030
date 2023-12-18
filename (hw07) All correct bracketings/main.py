# handle input
from math import comb
n = int(input())

def catalonan_1(n):
    """Solution using catalonan numbers computed by recursion"""
    if n == 0:
        return 1
    else:
        return int((4*n-2)/(n+1)*catalonan_1(n-1))

#print(catalonan_1(n))

def catalonan_2(n):
    """Solution using catalonan numbers computed by combinatorics"""
    if n == 0:
        return 1
    else:
        return(int((1 / (n + 1)) * comb(2 * n, n)))

print(catalonan_2(n))