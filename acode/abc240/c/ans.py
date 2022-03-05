n, x = map(int, input().split())
dp = 1
for _ in range(n):
  a, b = map(int, input().split())
  dp = (dp << a) | (dp << b)
print("Yes" if ((dp >> x) & 1) == 1 else "No")
