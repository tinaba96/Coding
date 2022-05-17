N, W = list(map(int, input().split()))
A = list(map(int, input().split()))


ans = set()

for i in range(N):
    if A[i] <= W:
        ans.add(A[i])

if len(A) >= 2:
    for i in range(N):
        for j in range(i+1, N):
            v = A[i] + A[j]
            if v <= W:
                ans.add(v)


if len(A) >= 3:
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                v = A[i] + A[j] + A[k]
                if v <= W:
                    ans.add(v)


print(len(ans))





