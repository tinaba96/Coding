N, K, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for l in range(Q):
    if A[L[l]-1] == N:
        continue
    elif L[l]-1 < K-1 and A[L[l]] == A[L[l]-1]+1:
        continue
    A[L[l]-1] += 1

print(*A)
