N, X = list(map(int, input().split()))

A = []
B = []

for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

for i in range(2**N):
    t = bin(i)
    snot = t[2:]
    s = snot.zfill(N+1)
    val = 0
    for k in range(N):
        if s[-k-1] == '0':
            val += A[k]
        elif s[-k-1] == '1':
            val += B[k]
        else: 
            val += A[k]
        if val > X:
            break
    if val == X:
        print('Yes')
        exit()
print ('No')



