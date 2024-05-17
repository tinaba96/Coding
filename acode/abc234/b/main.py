import math

N = int(input())
arr = []
for i in range(N):
    x, y = list(map(int, input().split()))
    arr.append((x, y))

ans = 0

for i in range(N):
    for j in range(i, N):
        a, b = arr[i]
        c, d = arr[j]
        leng = math.sqrt((a-c)**2 + (b-d)**2)
        ans = max(ans, leng)


print(ans)



