from collections import defaultdict

Q = int(input())

A = defaultdict(lambda: -1)
N = 2 **20

for q in range(Q):
    t, x = list(map(int, input().split()))
    if t == 1:
        h = x
        while A[h%N] != -1:
            h += 1
        A[h%N] = x
    else:
        print(A[x%N])
    

