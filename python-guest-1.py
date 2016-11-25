#for i in range(1,int(input())):
 #   for j in range(i):
  #       print (i, end='')
   # print(end='\n')

## print (i for i in range(1,int(input())) for j in range(i))

# (([x for x in range(1,int(input())) for y in range(x)]))

print (int(''.join([i for i in range(1,int(input())) for j in range(i)])))