import sys
sys.setrecursionlimit(100000)

N, M, K, S, T, X = list(map(int, input().split()))

mp = [[] for _ in range(N+1)]

for i in range(M):
    U ,V = list(map(int, input().split()))

    mp[U].append(V)
    mp[V].append(U)

mod = 998244353

stack = [T]

cnt = K
memo = [[[0,0] for j in range(2001)] for i in range(2001)]
ans = 0

while len(stack) > 0:
    ele = stack.pop()

    if ele == X:
        xcnt += 1


    if memo[ele][cnt][xcnt%2] != 0:
        ans += memo[ele][cnt][xcnt%2]
        continue

    


    if cnt == 0:
        if ele == S and xcnt%2 == 0:
            return 1
        else:
            return 0

    cnt -= 1
    for e in mp[ele]:
        stack.append(e)

# while ループとstackを用いて書き換えようと試みたが、
# 深さ（step）が必要な場合や、漸化式のように前の階層（深さ）を用いて現在の値を用いる場合は、stack&whileでは難しいと思われる。




'''
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
            if (xcnt)%2 != 0:

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
'''


