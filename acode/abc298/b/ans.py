def solve():
  n=int(input())
  A=[list(map(int, input().split())) for _ in range(n)]
  B=[list(map(int, input().split())) for _ in range(n)]

  for _ in range(4):
    if all(A[i][j] <= B[i][j] for i in range(n) for j in range(n)):
      return True
    #print('A: ', A)
    #print(*A)
    A=[list(a)[::-1] for a in zip(*A)]
  return False

print("Yes" if solve() else "No")

# transpose by zip() and reverse -> this is same as rotate (see video editorial)
