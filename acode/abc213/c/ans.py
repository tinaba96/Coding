'''
# 座標圧縮
def compression(arr):
    return {e : i + 1 for i, e in enumerate(sorted(set(arr)))}

h, w, n = map(int, input().split())
l = []
tate = []
yoko = []
for i in range(n):
    x, y = map(int, input().split())
    tate.append(x)
    yoko.append(y)
    l.append([x, y])
comp_tate = compression(tate)
comp_yoko = compression(yoko)

for x, y in l:
    print(comp_tate[x], comp_yoko[y])


h, w, n = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
a, b = [list(i) for i in zip(*l)]

sa = list(set(a))
sa.sort()
sb = list(set(b))
sb.sort()


def binary_search(numbers, value):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid + 1
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1

for j in range(n):
    print(binary_search(sa, a[j]), binary_search(sb, b[j]))
'''
H, W, N = map(int, input().split())
R = []
C = []

for _ in range(N):
    r, c = map(int, input().split())
    R.append(r)
    C.append(c)

Rs = sorted(set(R))  # `set`で重複を省いてソートしたリスト`Rs`
Cs = sorted(set(C))

# Rd = {Rs[i]: i+1 for i in range(len(Rs))} と同じです
Rd = {x: i for i, x in enumerate(Rs, 1)}
Cd = {x: i for i, x in enumerate(Cs, 1)}

for r, c in zip(R, C):
    print(Rd[r], Cd[c])
'''
for i in range(N):
    print(Rd[R[i]], Cd[C[i]])
'''
