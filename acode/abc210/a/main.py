#!/usr/bin/env PyPy3

N, A, X, Y = list(map(int, input().split()))

if N <= A:
    print(X*N)
else:
    print(X*A + (N-A)*Y)

