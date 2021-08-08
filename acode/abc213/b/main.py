N = int(input())
A = list(map(int, input().split()))

ma = max(A)
ans = 0
for i in range(len(A)):
    if A[i] != ma:
        ans = max(ans, A[i])


print(A.index(ans)+1)


