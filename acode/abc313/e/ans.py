N = int(input())
S = input()

flg = True
for i in range(N-1):
  if S[i] != '1' and S[i+1] != '1':
    flg = False
    break

if not flg:
  print(-1)
else:
  mod = 998244353
  ans = 0
  for i in range(N-1, 0, -1):
    ans += 1
    ans += ans*(int(S[i])-1)
    ans %= mod
  ans %= mod
  print(ans)

