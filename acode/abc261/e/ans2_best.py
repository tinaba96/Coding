N,C = map(int,input().split())
data = [[0,1] for _ in range(30)]

now = C
def f(n):
    if n == 0: return 0
    else: return 1

for _ in range(N):
    T,A = map(int,input().split())
    for i in range(30):
        for j in range(2):
            if T == 1: data[i][j] &= f(A & (1<<i))  # Aの左からi桁目
            if T == 2: data[i][j] |= f(A & (1<<i))  # Aの左からi桁目
            if T == 3: data[i][j] ^= f(A & (1<<i))  # Aの左からi桁目
    nxt = 0
    for i in range(30):
        bit = f(now & (1<<i))  # nowのi桁目のbitが立っているか（0 or 1）
        nxt += data[i][bit] * (1<<i)
    print(nxt)
    now = nxt

'''
N, x = map(int, input().split())
m = 2 ** 30 - 1
s1 = m
s0 = 0
for _ in range(N):
    t, a = map(int, input().split())
    if t == 1:
        s1 &= a
        s0 &= a
    elif t == 2:
        s1 |= a
        s0 |= a
    else:
        s1 ^= a
        s0 ^= a
    x = (x & s1) | ((x ^ m) & s0)
    print(x)

'''
