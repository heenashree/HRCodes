num1 = int(input())
A = [int(i) for i in input().split()]
num2 = int(input())
B = [int(i) for i in input().split()]
print(A)
print(B)
setA = set(A)
setB = set(B)

print (setA)
print (setB)

setC = setA.union(setB)
print ("union", setC)
setD = setA.intersection(setB)
print ("internsettion" , setD)
setE = setC.difference(setD)
print ("setE",setE)
setF = sorted(setE)
print (setF)
X = len(setF)

for i in range(X):
    print (setF[i])
