import sys
sys.setrecursionlimit(202020) # これをするだけで、TLEしなくなる。

n,m=map(int,input().split())
s=[[-1]*n for i in range(n)]
t=set()
s[0][0]=0
for i in range(-n*2,n*2):
  for j in range(-n*2,n*2):
    if i**2+j**2==m:t.add((i,j))
from collections import deque
que = deque([(0,0)])
while que:
    x,y = que.popleft()
    d = s[x][y]
    for a,b in t:
      if 0<=x+a<n and 0<=y+b<n:
        if s[x+a][y+b] > -1:continue
        s[x+a][y+b] = d + 1
        que.append((x+a,y+b))
for l in s:print(*l)

