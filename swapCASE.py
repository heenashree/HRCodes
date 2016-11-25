A = input()

Alist=list(A)
X=len(Alist)

for i in range(X):
    if (Alist[i]==Alist[i].upper()):
        Alist[i]=Alist[i].lower()
    elif (Alist[i]==Alist[i].lower()):
        Alist[i]=Alist[i].upper()

#A=Alist.split('')

A = ''.join(Alist)
print(A)
#print(A)