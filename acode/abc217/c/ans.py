lines = []
for _ in range(2):
  lines.append(input())

N = int(lines[0])
P = [int(_) for _ in lines[1].split(' ')]

Q = [0] * N

for idx , p in enumerate(P):
  Q[p - 1] = str(idx + 1)
    
print(' '.join(Q))
