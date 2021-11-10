import copy

N = int(input())

mp = [[] for i in range(10)]

for i in range(N):
    u, v = list(map(int, input().split()))
    mp[u].append(v)
    mp[v].append(u)

p = list(map(int, input().split()))

def correct(p):
    for i in range(8):
        if p[i] != i+1:
            return False
    return True

ans = 100100100100100

for i in range(1, 9):
    if i not in p:
        empty = i
        break
print('mp: ', mp)

#pp = copy.copy(p)
p.append(empty)
#print('p: ', p)

def check(q, p, empty):
    for ele in q:
        print('p',p)
        #print('empty', empty)
        empty = p[8]
        index = p.index(ele)
        tmp = empty
        #print(ele)
        empty = ele
        p[8] = empty
        p[index] = tmp
        if empty == 9 and correct(p):
            print('Yes')
        check(mp[empty], p, empty)

check(mp[empty], p, empty)

# if you try this way to consider the both way of edges, there will be infinite loop

