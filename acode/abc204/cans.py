n,m=map(int,input().split())
G=[[] for _ in range(n)]
for _ in range(m):
  a,b=map(int,input().split())
  G[a-1].append(b-1)


ans=0
for i in range(n):
  seen=[False]*n
  seen[i]=True
  todo=[i]
  cnt=1
  while len(todo)>0:
    # maybe DFS
    tmp=todo.pop()
    # maybe BFS
    #tmp=todo.pop(0)
    for j in G[tmp]:
      if seen[j]==False:
        seen[j]=True
        todo.append(j)
        cnt+=1
  ans+=cnt
print(ans)
