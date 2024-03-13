N = int(input())

A = list(map(int, input().split()))

total = 0
tot = 0

for i in range(N):
    total += A[i]**2

for j in range(N):
    tot += A[j]

tot2 = tot**2

print(N*total-tot2)


