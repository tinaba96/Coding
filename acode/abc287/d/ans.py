S = input()
T = input()
N = len(T)
ans = ['Yes']*(N+1)
for _ in range(2):
  ok = True
  for i in range(N):
    if S[i] != T[i] and S[i] != '?' and T[i] != '?':
      ok = False
    if not ok:
      ans[i+1] = 'No'
  S = S[::-1]
  T = T[::-1]
  ans = ans[::-1]
print(*ans)
