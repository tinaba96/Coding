n=int(input())
a=list(map(int,input().split()))
b=[0]*n
b2=[0]*n
b3=[0]*n
for i in range(n):
  c=a[i]
  while c%2==0:
    c//=2
    b2[i]+=1
  while c%3==0:
    c//=3
    b3[i]+=1
  b[i]=c
if len(set(b))>1:
  print (-1)
else:
  print (sum(b2)+sum(b3)-min(b2)*n-min(b3)*n)
  
