import sys
N = int(sys.stdin.buffer.readline())
A = set(map(int, sys.stdin.buffer.readline().split()))
ans = 0
c = 0
for i in range(1, N+1):
  c += 2-(i in A)
  if c > N:
    break
  ans = i
print(ans)
