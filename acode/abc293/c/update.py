H, W = list(map(int, input().split()))
mp = []
for h in range(H):
    l = list(map(int, input().split()))
    mp.append(l)
ans = 0
def search(y, x, path):
    global ans
    if (y,x) == (H-1, W-1):
        ans += 1
    if y < H-1:
        if mp[y+1][x] not in path:
            path.add(mp[y+1][x])
            search(y+1, x, path)
            path.remove(mp[y+1][x])
    if x < W-1:
        if mp[y][x+1] not in path:
            path.add(mp[y][x+1])
            search(y, x+1, path)
            path.remove(mp[y][x+1])
path = set()
path.add(mp[0][0])
search(0, 0, path)
print(ans)

