n,x=map(int,input().split())
a=[]
l=[]
for i in range(n):
  t=list(map(int,input().split()))
  a.append(t[1:])
  l.append(t[0])
ans=0
def prod(idx,p):
  global ans
  for i in range(l[idx]):
    tmpp=p*a[idx][i]
    if idx==n-1:
      if tmpp==x:
        ans+=1
    else:
      prod(idx+1,tmpp)
prod(0,1)
print(ans)
