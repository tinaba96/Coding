N, M = list(map(int, input().split()))

table = [[] for i in range(N+1)]
#table = {}
a = []
b = []

qu = [i for i in range(1, N+1)] # when this become null, it means it is the end
#print(qu)

for i in range(M):
    A, B = list(map(int, input().split()))
    table[A].append(B)
    a.append(A)
    b.append(B)
#print('table', table)

def app(arr, q):
    #print('def')
    q.sort()
    # b should be considered here before it appends to the 'arr'
    while q[0] > qu[0]: 
        if qu[0] in arr:
            break
        else:
            e = qu.pop(0)
            arr.append(e) # it appends without considering whether there are other nodes to be appended first or not
            if table[e] != []:
                app(arr, table[e])
            if q[0] == [] or qu[0] == []:
                break

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
    if i not in b and i not in arr: #this is the start to choose the node that doesn't have edge to come
        qu.pop(qu.index(i))
        arr.append(i)
        if table[i] != []:
            app(arr, table[i])
            if qu == []:
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
#print('table', table)
#print('qu', qu)
if len(arr) == N:
    L=[str(a) for a in arr]
    L=" ".join(L)
    print(L)
else:
    print(-1)

# it is needed to consider b, so that it is able to know the node is ready to picked up or not.
# in this way, it can never know whether the node is ready to choose or not. it just considers whether it is already pciked up (arr). 
# b is considered only at the first place but it is needed to be considered during the process as well

