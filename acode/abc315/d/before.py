import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import Counter
#mylist = ["apple","banana","apple","apple","orange"]
#mycounter = Counter(mylist)
from collections import defaultdict
#d = defaultdict(int)


oH, oW = list(map(int, input().split()))

H = oH
W = oW

mp = []
origin = []

for i in range(H):
    #c = list(map(int, input().split()))
    c = str(input())
    mp.append(c)
    origin.append(c)


sd = set()


while True:
    final = False
    d = []
    for h in range(H):
        flg = True
        b_flg = False
        cnt = 0
        for w in range(W): # this is O(N^3) this should be O(m(=26)) or O(1)
            if w in sd:
                continue
            elif b_flg == False:
                base = w
                b_flg = True

            cnt += 1

            if mp[h][w] != mp[h][base]:
                flg = False
                break
        if cnt <= 1:
            break
        if flg == True:
            final = True
            d.append(h)

    d.sort(reverse=True)
    for e in d:
        del mp[e]

    H -= len(d)

    #d = []
    #sd = set()
    for w in range(W):
        if w in sd:
            continue
        flg = True
        cnt = 0
        for h in range(H):
            cnt += 1
            if mp[h][w] != mp[0][w]:
                flg = False
                break
        if cnt <= 1:
            break
        if flg == True:
            final = True
            #d.append(w)
            sd.add(w)
    '''
    for e in d:
        for h in range(H):
            mp[h] = mp[h][:e] + mp[h][e+1:]
    '''

    W -= len(d)

    #print(final)
    #print(sd)
    if final == False:
        break
    

lsd = list(sd)
lsd.sort(reverse=True)

#print(H)
for e in lsd:
    for h in range(H):
        mp[h] = mp[h][:e] + mp[h][e+1:]

#print(lsd)
#print(mp)

ans = 0
for i in range(len(mp)):
    ans += len(mp[i])
#print(ans)




# another case
H = oH
W = oW
sd = set()

mp = origin
#print(mp)

while True:
    final = False

    #d = []
    #sd = set()
    for w in range(W):
        if w in sd:
            continue
        flg = True
        cnt = 0
        for h in range(H):
            cnt += 1
            if mp[h][w] != mp[0][w]:
                flg = False
                break
        #print(flg)
        if cnt <= 1:
            break
        if flg == True:
            final = True
            #d.append(w)
            sd.add(w)
    '''
    for e in d:
        for h in range(H):
            mp[h] = mp[h][:e] + mp[h][e+1:]
    '''

    #W -= len(d)


    d = []
    for h in range(H):
        flg = True
        b_flg = False
        cnt = 0
        for w in range(W):
            if w in sd:
                continue
            elif b_flg == False:
                base = w
                b_flg = True

            cnt += 1

            if mp[h][w] != mp[h][base]:
                flg = False
                break
        if cnt <= 1:
            break
        if flg == True:
            final = True
            d.append(h)

    d.sort(reverse=True)
    for e in d:
        del mp[e]

    H -= len(d)


    #print(mp)
    #print(sd)
    if final == False:
        break


lsd = list(sd)
lsd.sort(reverse=True)

#print(H)
for e in lsd:
    for h in range(H):
        mp[h] = mp[h][:e] + mp[h][e+1:]

#print(lsd)
#print(mp)

ans2 = 0
for i in range(len(mp)):
    ans2 += len(mp[i])
print(min(ans, ans2))

