N, M = list(map(int, input().split()))

for n in range(N):
    B = list(map(int, input().split()))
    if n >= 1:
        if B[0] != 7 + st:
            print('No')
            exit()
    st = B[0]
    if n == 0:
        if st%7+ M >= 8:
            print('No')
            exit()
    for m in range(1, M):
        if B[m] != B[m-1] + 1:
            print('No')
            exit()

print('Yes')


