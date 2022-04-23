import copy

N,M,K=map(int,input().split())

mod=998244353

A=[]
B=[]
for i in range(K):
    if i<M:
        A.append(1)
    else:
        A.append(0)
    B.append(0)

C=tuple(B)

for i in range(N-1):
    for j in range(K-1):
        for k in range(1,M+1):
            if j+1+k<=K:
                B[j+k]+=A[j]
    A=B
    B=list(C)

ans=0
for x in range(K):
    ans+=A[x]
    if ans>=mod:
        ans=ans%mod

print(ans)


