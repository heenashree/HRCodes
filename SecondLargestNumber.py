# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
A=[]

for x in input().split():
        A.append(int(x))
#A = [int(a) for a in input().split(" ")]
print(A)

def my4_remove_duplicates(A):
    A.sort()
    i = len(A) - 1
    while i > 0:
        if A[i] == A[i - 1]:
            A.pop(i)
        i -= 1
    return A


my4_remove_duplicates(A)
print("After popper",A)
x=-100
m=-100
for e in A:
    if x<e:
        x=e
A.remove(x)

for e in A:
    if m<e:
        m=e
print ("Secpmd",m)


