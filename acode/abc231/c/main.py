import bisect

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))

A = sorted(A)
#print(A)

for q in range(Q):
    x = int(input())
    num = bisect.bisect_left(A, x)
    print(N - num)

