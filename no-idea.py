NandM=input()
NandM=NandM.split(' ')
n=int(NandM[0])
m=int(NandM[1])

Array = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

count = 0

for i in list(Array):
    if i in A:
        count = count + 1
              #print("inside A", count)
    elif i in B:
        count = count -1
              #print("inside B", count)
    else:
        count = count + 0

print(count)

