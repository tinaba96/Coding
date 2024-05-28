# not the best way

n = int(input())
a = [[-1] * 2001 for _ in range(2001)]
for _ in range(n):
    x, y = [int(i) + 1000 for i in input().split()]
    a[x][y] = 0

cnt = 0
for i in range(2001):
    for j in range(2001):
        # O(N^2)
        if a[i][j] != 0: continue # if is visited already or not black, will skip
        
        cnt += 1
        stack = [[i, j]]
        while stack: # time complexity: N in Total O(N)
            x, y = stack.pop()
            for dx, dy in [[-1, -1], [-1, 0], [0, -1], [0, 1], [1, 0], [1, 1]]:
                xx, yy = x + dx, y + dy
                if not (0 <= xx < 2001 and 0 <= yy < 2001) or a[xx][yy] != 0:
                    continue
                a[xx][yy] = cnt # putting a number (cnt) to each block
                stack.append([xx, yy])

print(cnt)

# O(N^2 + N)? -> O(N^2)

