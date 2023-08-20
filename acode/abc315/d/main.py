# sample 2 のケースを落とすために、試行錯誤した。
# 2x2まではこのアプローチで行けるが、それ以上やると、行から実行するのか、列から実行するのかで、答えが変わってしまう。
# 2x2以降は、それぞれのパターンをやることでACするかも。
# ただ、高い確率でTLEする可能性あり
# TLEの原因はおそらくここになく、そもそものアプローチがTLEだと思われる。
# なぜなら、同じことを2回書くことで対策したが、2回書いても書かなくても、提出時に表示された実行時間に差はなかったから。



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

minus = 0

while True:
    final = False
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

    if len(d) > 0:
        check = mp[d[-1]][0]
        #print(check)

    for e in d:
        del mp[e]

    if len(mp) == 1 and H-len(d) == 1:
        if check in mp[0]:
            minus = mp[0].count(check)

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
print(ans-minus)




'''
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

    # no need
    for e in d:
        for h in range(H):
            mp[h] = mp[h][:e] + mp[h][e+1:]

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
'''

