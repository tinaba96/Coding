N, K, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for l in range(Q):
    if L[l]-1 > K-1:
        continue
    elif L[l]-1 == K-1 and A[L[l]-1] < N:
        A[L[l]-1] += 1
    elif L[l]-1 == K-1 and A[L[l]-1] >= N:
        continue
    elif A[L[l]] != A[L[l]-1]+1:
        A[L[l]-1] += 1

print(*A)
