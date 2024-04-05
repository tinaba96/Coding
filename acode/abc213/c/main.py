H, W, N = list(map(int,  input().split()))
a = []
b = []
c = []
for n in range(N):
    A, B = list(map(int, input().split()))
    a.append(A)
    b.append(B)
    c.append((A, B))

baseh = {}
basew = {}
#print(mp)
a = list(set(a))
b = list(set(b))
a.sort()
b.sort()
hh = 0


tmp = 0
for ele in a:
    baseh[ele] = ele - 1 - tmp
    tmp += 1

tmp = 0
for ele in b:
    basew[ele] = ele - 1 - tmp
    tmp += 1
'''
for h in range(1, H+1):
    if h not in a:
        hh += 1
    else:
        baseh[h] = hh




ww = 0
#print('b', b)
for w in range(1, W+1):
    if w not in b:
        ww += 1
    else:
        basew[w] = ww

'''

#print(baseh)
        
for n in range(N):
    print(c[n][0]-baseh[c[n][0]], c[n][1]-basew[c[n][1]])





