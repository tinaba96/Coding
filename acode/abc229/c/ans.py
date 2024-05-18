'''
N,W = map(int,input().split())

C = []

for i in range(N):
    a,b = map(int,input().split())
    C.append([a,b])

C.sort(reverse=True)

w = 0
d = 0
for i in range(N):
    a,b = C[i]
    if b <= W:
        d += (a * b)
        W -= b
    else:
        d += (a * W)
        break
print(d)
'''

oN, W = map(int, input().split())
AB = []
for _ in range(N):
    AB.append(list(map(int, input().split())))

AB.sort(reverse=True)

ans = 0
for ab in AB:
    a = ab[0]
    b = ab[1]
    weight = min(W, b)
    ans += a * weight
    W -= weight
print(ans)


