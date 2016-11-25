#!/bin/python3

import sys


s_len = int(input().strip())
word = input().strip()


X=len(word)

wordNew=list(word)
print(wordNew)
S=[]

for i in range(X-3):
    if(wordNew[i]==wordNew[i+2] and wordNew[i+1]== wordNew[i+3] and wordNew[i] != wordNew[i+1]):

       # S.append(wordNew[i])
        # S.append(wordNew[i+1])

        i=i+1
        print(i)
print("printintg...",S)
Y=len(S)
count=0
#for i in range(Y-2):
 #   if(S[i]==S[i+1]):
  #      S.remove(S[i])
   #     count=count+1



