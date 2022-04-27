from itertools import combinations
from collections import Counter

n, k = map(int, input().split())
S = [input() for _ in range(n)]

ans = 0
for r in range(1, n+1):
    for comb in combinations(range(n), r):
        partial_concat_s, cnt = [], 0
        for index in comb:
            partial_concat_s += S[index]
        #print(partial_concat_s)
        for num in Counter(partial_concat_s).values():
            if num == k:
                cnt += 1
        ans = max(ans, cnt)
print(ans)
