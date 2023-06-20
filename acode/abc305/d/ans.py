from bisect import *
n = int(input())
A = list(map(int, input().split())) + [10**9+1]
RA = [0]
for i, ai in enumerate(A):
    if i == 0: continue
    if i%2==0:
        RA.append(RA[-1] + A[i] - A[i-1])
    else:
        RA.append(RA[-1])


# print(RA)

def solv(r):
    rp = bisect_right(A, r)
#    print(rp, RA[rp-1], A[rp-1], r)
    if rp%2 == 0:
        ret = RA[rp-1] + (r - A[rp-1])
    else:
        ret = RA[rp-1]
    return ret




q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    ret = solv(r) - solv(l)
    print(ret)
