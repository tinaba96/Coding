N = int(input())

ans = N ** 3
for a in range(10 ** 6 + 1):
    ok = 10 ** 6
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        x = a ** 3 + (a ** 2) * mid + a * (mid ** 2) + mid ** 3
        if x >= N:
            ok = mid
        else:
            ng = mid
    x = a ** 3 + (a ** 2) * ok + a * (ok ** 2) + ok ** 3
    ans = min(ans, x)

print(ans)
