N = int(input())
T = list(map(int, input().split()))

dp = 1
tot = 0
for t in T:
    tot += t
    dp = dp | (dp<<t)
ans = sum(T)
dp=bin(dp)
for i in range(tot+1):
    if dp[-i-1] == '1':
        ans = min(ans, max(i, tot-i))



print(ans)




