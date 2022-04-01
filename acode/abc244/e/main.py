import sys
sys.setrecursionlimit(100000)

N, M, K, S, T, X = list(map(int, input().split()))

mp = [[] for _ in range(N+1)]

for i in range(M):
    U ,V = list(map(int, input().split()))

    mp[U].append(V)
    mp[V].append(U)

mod = 998244353

memo = [[[0,0] for j in range(2001)] for i in range(2001)]
#print(memo[4][5][0])

# node にcntで到着できた場合の数
def f(node, cnt, xcnt):
    if cnt == 0:
        if node == S and xcnt%2 == 0:
            return 1
        else:
            return 0
    tmp = 0
    for e in mp[node]:
        if e == X:
            if (xcnt+1)%2 != 0:

                if memo[e][cnt-1][1] != 0:
                    tmp += memo[e][cnt-1][1]
                else:
                    tmp += f(e, cnt-1, (xcnt+1)%2)%mod
            else:
                if memo[e][cnt-1][0] != 0:
                    tmp += memo[e][cnt-1][0]
                else:
                    tmp += f(e, cnt-1, (xcnt+1)%2)%mod

        else:
            if (xcnt+1)%2 != 0: # this is xcnt not xcnt+1

                if memo[e][cnt-1][1] != 0:
                    tmp += memo[e][cnt-1][1]
                else:
                    tmp += f(e, cnt-1, xcnt%2)%mod
            else:
                if memo[e][cnt-1][0] != 0:
                    tmp += memo[e][cnt-1][0]
                else:
                    tmp += f(e, cnt-1, xcnt%2)%mod
                

    if xcnt%2 == 0:
        memo[node][cnt][0] = tmp%mod
    else:
        memo[node][cnt][1] = tmp%mod

    return tmp%mod
    
print(f(T, K, 0))


