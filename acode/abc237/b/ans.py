def ints():
  return list(map(int,input().split()))
h,w = ints()
a = [ints() for i in range(h)]
b = zip(*a)
for row in b:
  print(*row)
