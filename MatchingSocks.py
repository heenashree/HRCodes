#!/bin/python3

import sys


n = int(input().strip())
A = [int(c_temp) for c_temp in input().strip().split(' ')]


def dupSocks(A):
    j = 0
    A.sort()
    i = len(A) - 1
    while i > 0:
        if A[i] == A[i - 1]:
            j=j+1
            i=i-2
        elif A[i] != A[i-1]:
            i=i-1

    print(j)
    return A

dupSocks(A)
