N, X = list(map(int, input().split()))

A = list(map(int, input().split()))

B = []


# remove()


for i in range(N):
    if A[i] != X:
        B.append(A[i])

for i in range(len(B)):
    print(B[i], end=' ')


