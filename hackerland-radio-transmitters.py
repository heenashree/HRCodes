#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
x = [int(x_temp) for x_temp in input().strip().split(' ')]
x = sorted(x)

count=0
i=0
j=0
for i in range(x[n-1]):
    while j < x[n-1]:
        #count = count +1
        if (i==j):
            j = j+(k+1)
            #count = count +1
            print(j)
            break
    break
