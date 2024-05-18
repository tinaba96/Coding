from collections import defaultdict

Q = int(input())

A = defaultdict(lambda: -1)
# if it is defined as array, it will not be TLE
# it is time consuming to create each keys as the default value of -1 than creating an array whose length is N
# A = [-1] * N 
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
    

