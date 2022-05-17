N = int(input())

ch = set()
ans = 0
score = 0

for i in range(N):
    S, T = list(map(str, input().split()))
    T = int(T)
    if S not in ch:
        ch.add(S)
        if T > score:
            ans = i+1
            score = T

print(ans)





