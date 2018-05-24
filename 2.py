n=int(input("enter n"))
c=[]
for i in range(0,n):
  b=int(input())
  c.append(b)
c.sort()
b=c[::-1]
print("".join(str(x) for x in b))
