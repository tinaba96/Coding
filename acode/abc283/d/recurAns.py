import sys
sys.setrecursionlimit(10 ** 6)
S = input()
cnt = [0] * 256
i = 0
def f():
  global i
  add = []
  while i < len(S) and S[i] != ')':
    if S[i] == '(':
      i += 1
      if not f():
        return False
      assert S[i] == ')'
      i += 1
      continue
    x = ord(S[i])
    add.append(x)
    if cnt[x]:
      return False
    cnt[x] = 1
    i += 1
  for x in add:
    cnt[x] = 0
  return True
print("Yes" if f() else "No")
