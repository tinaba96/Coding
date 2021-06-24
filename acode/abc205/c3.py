A, B, C = list(map(int, input().split()))

def p(x, y):
    ans = x
    if y == 1:
        return x
    else:
        t = 0
        while True:
            tmp = ans
            ans = tmp * tmp
        



f = pow_r(A,C)
s = pow_r(B,C)

if f > s:
    print(">")
elif f < s:
    print("<")
else:
    print('=')
