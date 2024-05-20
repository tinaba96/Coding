N = int(input())
XY = []
points = set()
for i in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))
    points.add((x, y))

XY.sort()

cnt = 0
for i in range(N-1):
    x1, y1 = XY[i]
    for j in range(i+1, N):
        x2, y2 = XY[j]
        if x1 >= x2 or y1 >= y2:
            continue
        if (x1, y2) in points and (x2, y1) in points:
            cnt += 1

print(cnt)


