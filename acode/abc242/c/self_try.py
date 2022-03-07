import sys

sys.setrecursionlimit(10**6)

N = int(input())

cnt = 0

mp = [[-1 for i in range(10)] for j in range(10000)]

def memo(l, n, f):
    global cnt


    if l == N-1:
        cnt += 1
        mp[l][f] = cnt
    elif l == N:
        return

    if mp[l][n] != -1:
        if N-l > l:
            l += l
            cnt += mp[l][n]
        
    if n != 1 and n != 9:
        memo(l+1, n-1, f)
        memo(l+1, n, f)
        memo(l+1, n+1, f)
    elif n == 1:
        memo(l+1, n, f)
        memo(l+1, n+1, f)
    elif n == 9:
        memo(l+1, n-1, f)
        memo(l+1, n, f)

ans = 0

for i in range(1, 10):
    memo(0, i, i)


print(cnt)



