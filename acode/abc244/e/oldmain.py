import sys
sys.setrecursionlimit(10**6)

N, M, K, S, T, X = list(map(int, input().split()))

mp = [[] for _ in range(N+1)]

for i in range(M):
    U ,V = list(map(int, input().split()))

    mp[U].append(V)
    mp[V].append(U)

mod = 998244353


# node にcntで到着できた場合の数
def f(node, cnt, kcnt):
    if cnt == 0:
        if node == S and kcnt%2 == 0:
            return 1
        else:
            return 0
    tmp = 0
    for e in mp[node]:
        if e == K:
            tmp += f(e, cnt-1, kcnt+1)%mod
        else:
            tmp += f(e, cnt-1, kcnt)%mod

    return tmp%mod
    
print(f(T, K, 0))


