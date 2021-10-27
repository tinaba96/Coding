from itertools import product


n = input()

ans = 0
for bits in product([0,1], repeat=len(n)):
  left = []
  right = [] 
  for i in range(len(n)):
    if bits[i] == 0:
      left.append(n[i])
    else:
      right.append(n[i])
  left.sort(reverse=True)
  right.sort(reverse=True)
  if len(left) == 0 or len(right) == 0:
    continue

  ans = max(ans, int("".join(left))*int("".join(right)))

print(ans)
