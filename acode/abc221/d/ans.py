'''
[D - Online games](https://atcoder.jp/contests/abc221/tasks/abc221_d)
'''

from collections import Counter

n = int(input())
event = Counter()
for _ in range(n):
    a, b = map(int, input().split())
    event[a] += 1
    event[a+b] -= 1

ans = [0] * (n+1)
days = sorted(event.keys())
prev_day = 0
cnt = 0

for day in days:
    ans[cnt] += day - prev_day
    cnt += event[day]
    prev_day = day

print(*ans[1:])


