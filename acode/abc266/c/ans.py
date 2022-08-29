a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

combs = [(a, b, c), (b, c, d), (c, d, a), (d, a, b)]

def check(points): 
    va = (points[1][0] - points[0][0], points[1][1] - points[0][1])  # x of vector
    vb = (points[2][0] - points[1][0], points[2][1] - points[1][1])  # y of vector
    g = va[0] * vb[1] - va[1] * vb[0] # 外積計算
    if g <= 0: # 符号付き面積->負の場合、内角は180ど以上
        print("No")
        exit()

for comb in combs:
    check(comb)

print("Yes")


# gift wrapping methof
'''
def wrap(ps):
  # ギフト包装法を使って凸包を求める。
  # 各点[x, y]をリストとして与えると凸包の各点をリストとして返す。
  qs = []
  # 最初の点
  x = [p[0] for p in ps]
  min_i = x.index(min(x))
  qs.append(ps[min_i]) # xが最小になる点をqs[0]とする。
  # 各点
  n = -1
  while True:
    n += 1
    for i in range(len(ps)):
      flag = False
      for p1 in ps:
        if qs[n] == ps[i]:
          flag = True
          break
        result = gaiseki(qs[n], ps[i], p1)
        if result > 0 : # left
          flag = True
          break
      if flag == False:
        this_i = i
    if ps[this_i] == qs[0]:
      break
    qs.append(ps[this_i])
  return qs

def gaiseki(moto, saki0, saki1):
  # moto->saki0 の直線に対し saki1がどちら側にあるか
  # >0 ならば 左側 <0 ならば 右側
  x0 = saki0[0] - moto[0]
  y0 = saki0[1] - moto[1]
  x1 = saki1[0] - moto[0]
  y1 = saki1[1] - moto[1]
  gaiseki = x0 * y1 - x1 * y0
  return gaiseki
xy = []
for _ in range(4):
    x, y = map(int, input().split())
    xy.append((x,y))
totsuhou = wrap(xy)

if len(totsuhou) ==4:
    print('Yes')
else:
    print('No')

'''

# https://atcoder.jp/contests/abc266/submissions/34444882
# https://stabucky.com/wp/archives/14340
