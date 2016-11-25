stringA = input()
stringB = input()


X = len(stringA)
Y = len(stringB)
count=0
i=0
A1=0


while i < X+Y and A1>=0:
        A1 = stringA.find(stringB,i)
        i = A1+Y-1
        #print(A1)
        count=count+1

print(count-1)

