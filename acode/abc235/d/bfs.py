import sys
#import resource

sys.setrecursionlimit(10**8)
#print(sys.getrecursionlimit())
# naximum recursion is 1000
a, N = list(map(int, input().split()))

ans = 100100100100

def sizeint(v):
    ss = str(v)
    size = len(ss)
    return size

#print(sizeint(123445))

def strch(x):
    s = str(x)
    if len(s) == 1:
        return x
    elif len(s) == 2:
        an = s[-1] + s[0]
        r = int(an)
        return r
    else:
        l = len(s)
        an = s[-1] + s[:l-1]
        r = int(an)
        return r

#print(strch(123456))
def ch(cnt, val):
    #print(val)
    global ans
    if sizeint(N) < sizeint(val):
        #print(sizeint(val))
        return
    if N == val:
        ans = min(ans, cnt)
        return
    else:
        ch(cnt+1, val*a)
        ch(cnt+1, strch(val))

ch(0, 1)
if ans == 100100100100:
    print(-1)
else:
    print(ans)


