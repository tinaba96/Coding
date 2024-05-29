x1, y1, x2, y2 = map(int, input().split())
print(max(min(y1, y2) - max(x1, x2), 0))


