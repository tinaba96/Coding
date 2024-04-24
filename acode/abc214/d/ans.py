n = int(input())

par = list(range(n))
size = [1] * n
def find(x):
    """ 根のノードの値を見つけて返す """
    if x != par[x]:
        par[x] = find(par[x])
    return par[x]

def unite(x, y):
    """xとyを結合する"""
    rootx = find(x)
    rooty = find(y)

    if rootx == rooty:
        return False
    else:
        if size[rootx] < size[rooty]:
            par[rootx] = rooty
            size[rooty] += size[rootx]
        else:
            par[rooty] = rootx
            size[rootx] += size[rooty]
        return True

def same(x, y):
    """ xとyが同じ集合に属しているか """
    return find(x) == find(y)

uvw = []
for _ in range(n-1):
    u, v, w = map(int, input().split())
    uvw.append((u-1, v-1, w))

uvw = sorted(uvw, key=lambda x: x[2])

# 重みが小さい辺から
ans = 0
for u, v, w in uvw:
    ls = size[find(u)]
    rs = size[find(v)]
    ans += w*(ls*rs)
    unite(u, v)

print(ans)




