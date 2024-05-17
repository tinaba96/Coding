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
pas = set()

def strch(x):
    s = str(x)
    if len(s) == 1:
        return x
    elif len(s) == 2:
        if s[-1] != '0':
            an = s[-1] + s[0]
            r = int(an)
            return r
        else:
            return int(x)
    else:
        if s[-1] != '0':
            l = len(s)
            an = s[-1] + s[:l-1]
            r = int(an)
            return r
        else:
            return int(x)

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
                pas.add(strch(el))
            else:
                nex = []

        else:
            if el*a not in pas:
                pas.add(el*a)
                nex.append(el*a)
            if strch(el) not in pas:
                pas.add(strch(el))
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


