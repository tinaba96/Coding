a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

combs = [(a, b, c), (b, c, d), (c, d, a), (d, a, b)]

def check(points):
    va = (points[1][0] - points[0][0], points[1][-1] - points[0][-1])
    vb = (points[-1][0] - points[1][0], points[-1][-1] - points[1][-1])
    g = va[0] * vb[-1] - va[-1] * vb[0]
    if g <= 0: # 符号付き面積->負の場合、内角は180ど以上
        print("No")
        exit()

for comb in combs:
    check(comb)

print("Yes")
