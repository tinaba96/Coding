N = int(input())
A = list(map(int, input().split()))

ans = 0
cnt = 0
a = [0]
for i in range(N):
    a.append(A[i])

for i in range(1, N+1):
    if i == a[i]:
        cnt += 1
    else:
        if a[i] > i:
            if a[a[i]] == i:
                ans += 1

for l in range(cnt-1):
    ans += cnt-1-l

print(ans)

