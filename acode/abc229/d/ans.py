from bisect import bisect_left
S = input()
K = int(input())
dots_cnt = [1 if s =='.' else 0 for s in S]

ans = 0
r = 0
n = len(S)
sum = 0
for l in range(n):
    while r<n and sum+dots_cnt[r]<=K:
        sum +=dots_cnt[r]
        r+=1
    ans = max(ans,r-l)
    sum -= dots_cnt[l]
print(ans)

