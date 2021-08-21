N, L = list(map(int, input().split()))
K = int(input())
A = list(map(int, input().split()))

def maxcut(minlength):
    res = 0
    last = 0
    for a in A:
        if a - last >= minlength and L - a >= minlength:
            res += 1
            last = a
    return res

l = 0
r = L + 1
while r - l > 1:
    m = (r + l) // 2
    if maxcut(m) >= K: l = m
    else: r = m
print(l)

