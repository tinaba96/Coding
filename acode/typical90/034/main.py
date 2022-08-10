N, K = list(map(int, input().split()))
a = list(map(int, input().split()))

mp = set()
l = 0
r = 0
mp.add(a[l])

ans = 0

while r < N-1:
    r += 1 
    if a[r] not in mp:
        if len(mp) != K:
            mp.add(r)
        else:
            while l <= r:
                l += 1
                if a[l-1] != a[l]:
                   mp.remove(a[l-1])
                   break
    ans = max(ans, r-l)


print(ans)








