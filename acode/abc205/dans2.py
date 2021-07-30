N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
K = []

def cnt(m):
  bottom, top = 0, N
  while top - bottom > 1:
    mid = (top + bottom) // 2
    if A[mid] <= m:
      bottom = mid
    else:
      top = mid
    if m < A[0]:
      top = 0
  return m-top

def solve(k):
  bottom, top = 0, 10**19
  while top - bottom >1:
    mid = (top + bottom) // 2
    if cnt(mid) < k:
      bottom = mid
    else:
      top = mid
  return top

for i in range(Q):
  k = int(input())
  print(solve(k))
  


