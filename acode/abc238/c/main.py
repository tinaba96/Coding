N = int(input())
ke = len(str(N))
#ans = f(ke)

if ke == 1:
    print(int(N*(N+1)/2))
    exit()

ans = 0 

m = ''
tmp = 9
for i in range(ke-1):
    m += '9'
    # should be this
    #ans += tmp*(tmp+1)//2
    ans += tmp*(tmp+1)/2
    tmp *= 10

mn = int(m)
#print(m)
#ans = mn*(mn+1)/2

vv = N - mn

# should be this
#tvv = vv*(vv+1)//2
tvv = vv*(vv+1)/2

ans += tvv


print(int(ans)%998244353)

# we should always be aware of "/" since it actually has fraction which can leads to Wrong answer when we handle large number

