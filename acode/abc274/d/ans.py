N, x, y = map(int, input().split())
A = list(map(int ,input().split()))

s = [0,0]
sx = {0}
sy = {0}
for i in range(N):
  if i == 0:
    sx = {A[i]}
  elif i %2 == 0:
    tmp_sx = set()
    for xi in sx:
      tmp_sx.add(xi-A[i])
      tmp_sx.add(xi+A[i])
    #sx = tmp_sx
    sx, tmp_sx = tmp_sx, sx
  else:
    tmp_sy = set()
    for yi in sy:
      tmp_sy.add(yi-A[i])
      tmp_sy.add(yi+A[i])
    #sy = tmp_sy
    sy, tmp_sy = tmp_sy, sy
if x in sx and y in sy:
  print("Yes")
else: print("No")
