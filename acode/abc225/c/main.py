N, M = list(map(int, input().split()))

for n in range(N):
    B = list(map(int, input().split()))
    if n >= 1:
        if B[0] != 7 + st:
            print('No')
            exit()
    st = B[0]
    if n == 0:
        #if (st%7 == 0 and M > 1) or st%7+ M-1 >= 8:
        if st%7+ M >= 8: # this is wrong. above is correct
            print('No')
            exit()
    for m in range(1, M):
        if B[m] != B[m-1] + 1:
            print('No')
            exit()

print('Yes')


