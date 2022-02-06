N = int(input())
ke = len(str(N))
#ans = f(ke)

if ke == 1:
    print(int(N*(N+1)/2))
    exit()

def f(x):
    k = len(str(x))
    m = ''
    if k >= 2:
        for i in range(k-1):
            m += '9'
        m = int(m)
    else:
        m = 0

    val = x - m
    return val

ans = 0 

m = ''
tmp = 9
for i in range(ke-1):
    m += '9'
    ans += tmp*(tmp+1)/2
    tmp *= 10

mn = int(m)
#print(m)
#ans = mn*(mn+1)/2

vv = N - mn

tvv = vv*(vv+1)/2

ans += tvv


v = N*(N+1)/2
t = 1
for i in range(ke-1):
    t *= 10
t -= 1
vm = t*(t+1)/2

val = v - vm

#ans += val

print(int(ans)%998244353)

