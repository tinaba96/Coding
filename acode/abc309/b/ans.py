# similar to video editorial
import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
ans = [[-1] * n for _ in range(n)]
first = []
second = []
third = []
fourth = []
for i in range(n - 1):
    first.append((0, i))
    second.append((i, n - 1))
    third.append((n - 1, n - 1 - i))
    fourth.append((n - 1 - i, 0))
for i in range(1, n - 1):
    for j in range(1, n - 1):
        ans[i][j] = arr[i][j]
for i in first:
    x, y = i
    ans[x][y + 1] = arr[x][y]
for i in second:
    x, y = i
    ans[x + 1][y] = arr[x][y]
for i in third:
    x, y = i
    ans[x][y - 1] = arr[x][y]
for i in fourth:
    x, y = i
    ans[x - 1][y] = arr[x][y]
for i in ans:
    print(''.join(map(str, i)))


