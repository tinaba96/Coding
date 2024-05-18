N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

A = sorted(A, reverse=True)
cnt = 0
c = 0

while (len(A)-c >= K):
    #m = min(A[:K])
    cnt += 1
    #cnt += m
    for k in range(K): # O(NK)
        A[k] -= 1
        if A[k] == 0:
            c += 1
    A = sorted(A, reverse=True) # O(n^2(logN))

print(cnt)


