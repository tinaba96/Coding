import sys
sys.setrecursionlimit(10**9)
N,M=map(int,input().split())
G=[[] for i in range(N)]
for _ in range(M):
    u,v=map(int,input().split())
    u-=1;v-=1
    G[u].append(v)
    G[v].append(u)
color=[0 for i in range(N)]
def dfs(v,p,c):
    ret=[0,0]
    color[v]=c
    if c==1:
        ret[0]+=1
    else:
        ret[1]+=1
    for u in G[v]:
        if(u==p or color[u]==-c):continue
        if (color[u]==c):return (-1,-1)
        res=dfs(u,v,-c)
        if res[0]==-1:return (-1,-1)
        ret[0]+=res[0]
        ret[1]+=res[1]
    return tuple(ret)

ans=(N*(N-1))//2-M
for i in range(N):
    if not(color[i]):
        res=dfs(i,-1,1)
        if res[0]==-1:
            print(0)
            exit()
        ans-=res[0]*(res[0]-1)//2
        ans-=res[1]*(res[1]-1)//2
print(ans)

# it is better to do it this way (get val and finally subtract from all) since you can only think of one block in order to get the value.
# otherwise you have to consider each onnection between different blocks which is quite complicated.
