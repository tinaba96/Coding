import math

w, h, b = list(map(int, input().split()))

weight = b * h * h / 10000

if w-weight>0:
  print(math.ceil(w-weight))
else:
  print(0)
