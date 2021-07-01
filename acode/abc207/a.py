A = list(map(int, input().split()))

k = min(A)
ans = 0
flag = True
for i in range(len(A)):
    ans += A[i]


print(ans-k)


