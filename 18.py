x,y=map(int,raw_input().split())
for i in range(x,y):
 l=len(str(i))
 s=0
 temp=i
 while i>0:
  a=i%10
  s=s+(a**1)
  i=i/10
if(s==temp):
 print temp,
