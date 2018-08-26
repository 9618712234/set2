n=int(raw_input())
x=list(map(int,str(n)))
y=list(map(lambda a:a**3,x))
if(sum(y)==n):
 print("yes")
else:
 print("no")
