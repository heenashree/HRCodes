from itertools import *

#Join will join the strings in the list

A,B= (i for i in input().split())
A = str(A)
B = int(B)


def longestWord(letters):
  #This joins the parameters in the list

  combinations2 = list(map("".join, sorted(combinations_with_replacement(letters, B))))
  # print(combinations)
  combinations2 = "\n".join(combinations2)
  print(combinations2)

longestWord(str(A))