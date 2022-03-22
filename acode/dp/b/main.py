N, K  = list(map(int, input().split()))
h  = list(map(int, input().split()))

# K飛んで位置pに辿り着いたコスト
def f(p):
    if p == 0:
        return 0

    mi = 10**5
    for i in range(1, K+1):
        mi = min(mi, f(p-i))

    return mi

print(f(N-1))




