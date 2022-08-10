from collections import defaultdict

N, K = list(map(int, input().split()))
a = list(map(int, input().split()))


d = defaultdict(int)

l = 0
r = 0

d[r] = 1

ans = 0

while r < N-1:
    r += 1 
    if a[r] not in d:
        if len(d) != K:
            d[r] += 1
        else:
            while l <= r:
                l += 1
                d[l-1] -= 1
    ans = max(ans, r-l)


print(ans)








