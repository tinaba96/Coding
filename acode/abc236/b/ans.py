N = int(input())
A = list(map(int, input().split()))
ans = A[0]

for i in range(1, 4*N-1):
    ans = ans ^ A[i]

print(ans)


