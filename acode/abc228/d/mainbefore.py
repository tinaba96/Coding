from collections import defaultdict

Q = int(input())

N = 2 **20
A = defaultdict(lambda: -1)
mp = [0 for i in range(N+1)]

for q in range(Q):
    t, x = list(map(int, input().split()))
    if t == 1:
        h = x
        while A[h%N] != -1:
            h += mp[h%N] + 1
        A[h%N] = x
        mp[x%N] = h-x
    else:
        print(A[x%N])
    






