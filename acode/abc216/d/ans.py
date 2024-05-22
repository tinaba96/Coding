N,M = map(int,input().split())
G = [[]for i in range(N)]
rG = [[]for i in range(N)]
for i in range(M):
    k = int(input())
    a = list(map(int,input().split()))
    for i in range(k-1):
        G[a[i]-1].append(a[i+1]-1)
        rG[a[i+1]-1].append(a[i]-1)
inedge = [len(rG[i]) for i in range(N)]
L = []
import queue
S = queue.Queue()
for i in range(N):
    if inedge[i]==0:
        S.put(i)
while not S.empty():
    n = S.get()
    L.append(n)
    for i in G[n]:
        inedge[i] -= 1
        if inedge[i] == 0:
            S.put(i)
if len(L)==N:
    print("Yes")
else:
    print("No")


