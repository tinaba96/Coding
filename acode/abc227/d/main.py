N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

A = sorted(A, reverse=True)
cnt = 0
c = 0

while (len(A)-c >= K):
    m = min(A[:K])
    '''
    if m <= 0:
       print(cnt)
       exit()
    '''
    cnt += m
    for k in range(K): # O(NK)
        A[k] -= m
        if A[k] == 0:
            c += 1
    A = sorted(A, reverse=True) # O(n^2(logN))
    #print(A)



print(cnt)


