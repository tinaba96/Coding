import bisect

N = int(input())
A = list(map(int, input().split()))
A.sort()
#print(A)
Q = int(input())
for b in range(Q):
    B = int(input())
    index = bisect.bisect(A, B)
    if index == 0:
        print(abs(A[index]-B))
    elif index == N:
        print(abs(A[index-1]-B))
    else:
        print(min(abs(A[index]-B), abs(A[index-1]-B)))




