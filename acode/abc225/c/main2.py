N, M = list(map(int, input().split()))
for n in range(N):
    B = list(map(int, input().split()))
    if n == 0:
        p = (B[0]-1)//7
        q = (B[0]-1)%7
        #print(p, 'o', q)
    for m in range(M):
        if m+q+1 >= 8:
            print('No')
            exit()
        if B[m] != (n+p)*7+(m+q+1):
            print('No')
            exit()

print('Yes')




