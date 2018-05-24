n=int(input("enter n"))
c=[]
for i in range(0,n):
  b=int(input())
  c.append(b)
for i in c:
  if(c.count(i)!=1):
    print(i)
    break
