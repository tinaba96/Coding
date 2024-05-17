from itertools import permutations
n, m = map(int, input().split())
ab_lis = [list(map(int, input().split())) for _ in range(m)]
cd_lis = [[] for _ in range(n+1)]
lis = list(map(str, range(1, n+1)))

for _ in range(m):
  c, d = map(int, input().split())
  cd_lis[c].append(d)
  cd_lis[d].append(c)

for p in permutations(lis, len(lis)):
  flag = True
  ct = 0
  for ab in ab_lis:
    a = ab[0]
    b = ab[1]
    p_i = int(p[a-1])
    p_j = int(p[b-1])

    if not p_j in cd_lis[p_i]:
      flag = False
  if flag:
    break

if flag:
  print(p)
  print("Yes")
else:
  print("No")
