def solve():
  x = x3 if x1 == x2 else x2 if x1 == x3 else x1
  y = y3 if y1 == y2 else y2 if y1 == y3 else y1
  print(x, y)
 
 
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
solve()
