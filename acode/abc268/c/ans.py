N = int(input())
P = list(map(int,input().split()))

C = [0]*N

for i in range(N):
    C[(N - P[i] + i) % N] += 1
    C[(N - P[i] + i - 1) % N ] += 1
    C[(N - P[i] + i + 1) % N ] += 1

print(max(C))
