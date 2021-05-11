N = int(input())

A = list(map(int, input().split()))

ans = 0

for l in range(N): #O(10^4)
    x = A[l]
    for r in range(l, N):  #O(10^4)
        x = min(x, A[r])
        ans = max(ans, x*(r-l+1))

print(ans)

# O(10^8)

# if I use Pypy3, this will be AC 
# but if I use Python3, this will be TLE


