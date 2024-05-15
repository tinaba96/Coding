import sys
import resource

#print(resource.getrlimit(resource.RLIMIT_STACK))
sys.setrecursionlimit(100000000)

N = int(input())

cnt = 0

mp = [[-1 for i in range(10)] for j in range(N+1)]

# 残りrで最後がdのとき、残りの埋め方
def memo(r, d):

    if r == 1:
        return 1
    if mp[r][d] != -1:
        return mp[r][d]

    val = 0

    if d != 1 and d != 9:

        if mp[r-1][d-1] == -1:
            val += memo(r-1, d-1)
        else:
            val += mp[r-1][d-1]
        if mp[r-1][d] == -1:
            val += memo(r-1, d)
        else:
            val += mp[r-1][d]
        if mp[r-1][d+1] == -1:
            val += memo(r-1, d+1)
        else:
            val += mp[r-1][d+1]

    elif d == 1:
        if mp[r-1][d] == -1:
            val += memo(r-1, d)
        else:
            val += mp[r-1][d]
        if mp[r-1][d+1] == -1:
            val += memo(r-1, d+1)
        else:
            val += mp[r-1][d+1]

    elif d == 9:

        if mp[r-1][d-1] == -1:
            val += memo(r-1, d-1)
        else:
            val += mp[r-1][d-1]
        if mp[r-1][d] == -1:
            val += memo(r-1, d)
        else:
            val += mp[r-1][d]

    mp[r][d] = val%998244353
    return val%998244353


ans = 0

for i in range(1, 10):
    #print(memo(N, i))
    ans += memo(N, i)


#print(mp)
print(ans%998244353)



