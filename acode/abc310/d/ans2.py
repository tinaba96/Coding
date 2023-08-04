from collections import deque
from copy import deepcopy


n,t,m=map(int, input().split())
if t==n:
    print(1)
    exit()

edge=[set() for _ in range(n)]
for _ in range(m):
    a,b=map(lambda x: int(x) - 1, input().split())
    edge[a].add(b)
    edge[b].add(a)

ans=set()
D=deque()
D.append((0,[{0},],{0,}))

while D:
    tmp,teams,used=D.popleft()
    if len(used)==n:
        if len(teams)==t:
            ans.add(map(frozenset,teams))
        continue

    else:
        for e in range(n):
            if e in used:
                continue
            used.add(e)
            for i,team in enumerate(teams):
                if len(team&edge[e])>0:
                    continue
                nteams=deepcopy(teams)
                nteams[i].add(e)
                D.append((e,nteams,used|{e,}))

            if len(teams)<t:  # this is for new team
                nteams=deepcopy(teams)
                nteams.append({e,})
                D.append((e,nteams,used|{e,}))
            break


print(len(ans))
    

