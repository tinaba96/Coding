import sys
from collections import deque

queue = deque([[0, 1]])
#queue = [[1]]
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
cnt = 0

# 1. you did not cosider 0 at the end which leads to be difficult to finish the while loop since the val will possible to decrease which should not be
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

# 2. pas should be set() instead of an array. which makes very fast doing "not in pas" since it uses hash table to search
pas = []

while queue:
    tmp = queue.popleft()
    c = tmp[0]
    now = tmp[1:]
    #if now == []:
        #continue
    #print('q', queue)
    #print(pas)
    cnt = c + 1
    #print(now)

    for el in now:
        nex = [cnt]
        if sizeint(N) < sizeint(el):
            continue
        if N == el:
            ans = min(ans, cnt)
        if sizeint(N) < sizeint(el*a):
            if strch(el) not in pas:
                nex.append(strch(el))
                pas.append(strch(el))
            else:
                nex = []

        else:
            if el*a not in pas:
                pas.append(el*a)
                nex.append(el*a)
            if strch(el) not in pas:
                pas.append(strch(el))
                nex.append(strch(el))
        if nex != []:        
            #nex.insert(0, cnt)
            #print('nex', nex)
            queue.append(nex)
#ch(0, 1)
if ans == 100100100100:
    print(-1)
else:
    print(ans-1)


# As I tested using main2.py and main3.py, I found out that 2 changes above is needed to make it AC
# 1. is for solving WA and 2. is for solving TLE
