N, Q = list(map(int, input().split()))
X = list(map(int, input().split()))

mp = [[]*(N+1)]

for i in range(N):
    A, B = list(map(int, input().split()))
    mp[A].append(B)
    mp[B].append(A)


