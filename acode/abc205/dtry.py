import bisect

N, Q = list(map(int, input().split()))

A = list(map(int, input().split()))

for i in range(Q):
    ok = 100100100
    ng = 0
    k = int(input())
    while(ok-ng > 1):
        m = (ok+ng)//2
        d = bisect.bisect_right(A, m)
        nth = m - d
        if nth >= k:
            ok = m
        if nth < k:
            ng = m

    print(ok) 




