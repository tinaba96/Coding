def convert(H,W,T):
  s=set()
  for i in range(H):
    for j in range(W):
      if T[i][j]=="#":
        s.add((i,j))
  return s
        
def normalize(s):
  mx=min(x for (y,x) in s)
  my=min(y for (y,x) in s)
  return set((y-my,x-mx) for (y,x) in s)
  
HA,WA=map(int,input().split())
A=normalize(convert(HA,WA,[input() for i in range(HA)]))
HB,WB=map(int,input().split())
B=normalize(convert(HB,WB,[input() for i in range(HB)]))
HX,WX=map(int,input().split())
X=normalize(convert(HX,WX,[input() for i in range(HX)]))
ans=False
for i in range(-HX+1,HX):
  for j in range(-WX+1,WX):
    ans|=normalize(A.union((i+y,j+x) for (y,x) in B))==X

if ans:
  print("Yes")
else:
  print("No")

