#!/bin/python

import sys

a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]


L = a+b+c+d
M = b+c+d+e
N = a+c+d+e
O = a+b+d+e
P = a+b+c+e
a = [L,M,N,O,P]

a = sorted(a)
print(a[0],a[4])
