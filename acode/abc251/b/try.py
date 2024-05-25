N, W = list(map(int, input().split()))
A = list(map(int, input().split()))


ans = set()

for i in range(N):
    if A[i] <= W:
        ans.add(A[i])

for i in range(N):
    for j in range(i+1, N):
        v = A[i] + A[j]
        if v <= W:
            ans.add(v)


for i in range(N):
    print('confirm')
    for j in range(i+1, N):
        for k in range(j+1, N):
            v = A[i] + A[j] + A[k]
            print('check')
            if v <= W:
                ans.add(v)


print(len(ans))





