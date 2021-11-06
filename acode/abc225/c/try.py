# follows video editorial
N, M = list(map(int, input().split()))
for n in range(N):
    B = list(map(int, input().split()))
    for b in range(M):
        B[b] -= 1

    if n == 0:
        p = B[0]//7
        q = B[0]%7
        #print(p, 'o', q)
    if q + M - 1 >= 7:
            print('No')
            exit()

    for m in range(M):
        #if m+q >= 7:
        #    print('No')
        #    exit()
        if B[m] != (n+p)*7+(m+q):
            print('No')
            exit()


print('Yes')




