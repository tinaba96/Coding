import sys
# import resource

#print(resource.getrlimit(resource.RLIMIT_STACK))
sys.setrecursionlimit(10000000)

N = int(input())

cnt = 0

mp = [[-1 for i in range(10)] for j in range(N+1)]

# 残りrで最後がdのとき、残りの埋め方
def memo(r, d):
    
    if r == 1:
        mp[r][d] = 1
        return 1
    if mp[r][d] != -1:
        return mp[r][d]

    val = 0

    if 1<d<9:
        val += memo(r-1, d-1)
        val = val%998244353
        val += memo(r-1, d)
        val += memo(r-1, d+1)
    elif d == 1:
        val += memo(r-1, d)
        val += memo(r-1, d+1)
    elif d == 9:
        val += memo(r-1, d-1)
        val += memo(r-1, d)

    mp[r][d] = val%998244353
    cnt += 1
    return val%998244353


ans = 0

for i in range(1, 3):
    #print(memo(N, i))
    ans += memo(N, i)


print(ans%998244353)
# print(mp)
