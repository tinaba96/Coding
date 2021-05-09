N = int(input())

A = list(map(int, input().split()))

cum = [0]*N
cum2 = [0]*N
A2 = [0]*N
cum[0] = A[0]

cnt = [0]*200

for a in range(1,N):
    cum[a] = cum[a-1] + A[a]
for i in range(N):
    cum2[i] = cum[i]%200
    A2[i] = A[i]%200

print(A2)



