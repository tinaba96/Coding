N = int(input())
M = 1002
P = [[0] * M for _ in range(M)]
for _ in range(N):
    x1, y1, x2, y2 = map(lambda x: int(x) + 1, input().split())
    for x in range(x1, x2):
        P[x][y1] += 1
        P[x][y2] -= 1
ans = [0] * (N + 1)
for x in range(1, M):
    for y in range(1, M):
        P[x][y] += P[x][y - 1]
        ans[P[x][y]] += 1
for i in range(1, N + 1):
    print(ans[i])

