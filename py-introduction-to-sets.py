num = int(input())
A = [int(i) for i in input().split()]



#nums = [int(n) for n in text.split()]

#print("A", A)
setA = set(A)
#print("setA" , setA)
X = len(setA)
Y = sum(setA)/X
print(Y)