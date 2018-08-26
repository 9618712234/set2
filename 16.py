n,q=map(int,raw_input().split())
for i in range(n+1,q):
 if(i>1):
  for j in range(2,i):
   if(i%j==0):
   	break
   else:
   	print i,
