import heapq

N,M=map(int,input().split())
indeg=[0]*(N+1)
out=[[] for i in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    indeg[b]+=1
    out[a].append(b)

ans=[]
q=[i for i in range(1,N+1) if indeg[i]==0]
heapq.heapify(q)
while len(q)!=0:
    v=heapq.heappop(q)
    ans.append(v)
    for v2 in out[v]:
        indeg[v2]-=1
        if indeg[v2]==0:
            heapq.heappush(q,v2)
    
if len(ans)!=N:
    print(-1)
else:
    print(*ans)

#命題
# https://rikeilabo.com/proposition-formula


