h, w = map(int, input().split())
A = []
root = []
for i in range(h):
    a = list(map(int, input().split()))
    A.append(a)

def dfs(y, x, s):
    if y == h-1 and x == w-1:
        return len(set(s)) == h + w - 1
    
    ans = 0
    if (x+1 < w):
        ans += dfs(y, x+1, s + [A[y][x+1]])
    if (y+1 < h):
        ans += dfs(y+1, x, s + [A[y+1][x]])
    return ans

print(dfs(0, 0, [A[0][0]]))




