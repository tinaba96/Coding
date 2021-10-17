N, M = list(map(int, input().split()))

table = [[] for i in range(N+1)]
#table = {}
a = []
b = []

qu = [i for i in range(1, N+1)]
print(qu)

for i in range(M):
    A, B = list(map(int, input().split()))
    table[A].append(B)
    a.append(A)
    b.append(B)

def app(arr, q):
    #print('def')
    q.sort()
    while q and qu:
        while q[0] > qu[0]:
            e = qu.pop(0)
            arr.append(e)
            if table[e] != []:
                app(arr, table[e])

        if q == [] or qu == []:
            return
        e = q.pop(0)
        if e not in arr:
            qu.pop(qu.index(e))
            arr.append(e)
            if table[e] != []:
                app(arr, table[e])

arr = []
#print(table)
for i in range(1, N+1):
    if i not in b and i not in arr:
        qu.pop(qu.index(i))
        arr.append(i)
        if table[i] != []:
            app(arr, table[i])
            break
    else:
        continue

'''
for i in range(1, N+1):
    print(i)
    if i not in b and i not in arr:
        arr.append(i)
        if table[i] != []:
            app(arr, table[i])
    else:
        continue
'''
print(arr)


