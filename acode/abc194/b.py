N = int(input())
a = []
b = []
amin = 10*5
bmin = 10*5
ai = 0
bi = 0
aa = False
bb = False
for n in range(N):
    A, B = list(map(int, input().split()))
    a.append(A)
    b.append(B)
    if (A < amin):
        amin = min(amin, A)
        ai += 1
    elif A == amin:
        aa = True

    if (B < bmin):
        bmin = min(bmin, B)
        bi += 1
    elif B == bmin:
        bb = True

amin = min(a)
bmin = min(b)

ai = a.index(amin)
bi = b.index(bmin) #　this changes made it better -> check the reasons

#print(a.index(amin), b.index(bmin))
#print(ai, bi)
a.remove(amin)
amin2 = min(a)
#print(amin)
b.remove(bmin)
bmin2 = min(b)
#if (ai != bi or aa == True or bb == True):
if (ai != bi):
    print(max(amin, bmin))
else:
    #print(max(amin,bmin2))
    print(min(amin+bmin, min( max(amin,bmin2), max(amin2,bmin))))



