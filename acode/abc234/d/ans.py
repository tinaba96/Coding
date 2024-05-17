#priority queue

from heapq import heapify, heappop, heappush
n, k = map(int, input().split())
p = list(map(int, input().split()))

cp = p[:k]
print(min(cp))
heapify(cp)

for i in range(k,n):
    mn = heappop(cp)
    mn = max(mn,p[i])
    heappush(cp,mn)
    res = heappop(cp)
    print(res)
    heappush(cp,res)

# 線形（ならし）
N,K=map(int,input().split())
P=list(map(int,input().split()))

# 0：まだ出現していない　1：出現済
appear=[0]*(N+1)

for i in range(K):
    # K番目までの数を出現済に
    appear[P[i]]=1

# 0からスタート
x=0

for i in range(K-1,N):
    # P[i]を出現済に
    appear[P[i]]=1

    # もしxよりP[i]が大きければ
    if x<P[i]:
        # 次のxへ
        x+=1
        # 次に出現済みになる数までxを進める
        while appear[x]==0:
            x+=1
    
    print(x)

