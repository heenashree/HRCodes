#Name=input()
#X=len(Name)
#Replace=input()
#valA, val2, val3= Replace.strip( )
#val1=int(valA)
#if(val1<=X):
#    Name = Name[:val1]+val3+Name[val1+1:]
#print(Name)


Name=input()
X=len(Name)
l=list(Name)
Replace=input()
#valA,val2,val3, val4 = Replace.split( )

Replace=Replace.split(' ')
#print(Replace)
val1=int(Replace[0])
#print(val1)

val3=Replace[1]
#print(val3)
if(val1<X):
    l[val1]=val3
    Name=''.join(l)
    print(Name)

