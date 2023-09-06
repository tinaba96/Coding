N = int(input())
F, S = [], []
maxS, choice = 0, -1
for i in range(N):
    f, s = map(int, input().split())
    if s > maxS:
        maxS = s
        choice = i
    F.append(f)
    S.append(s)

ans = 0
for i in range(N):
    if i != choice:
        t = maxS + S[i] // (2 if F[i] == F[choice] else 1)
        ans = max(ans, t)
print(ans)

# https://atcoder.jp/contests/abc315/editorial/6995
