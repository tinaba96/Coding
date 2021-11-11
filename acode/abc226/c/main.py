from collections import deque

N = int(input())
inp = []
for i in range(N):
    A = list(map(int, input().split()))
    inp.append(A)

cnt = A[0]

q = deque(A[2:])
f = deque(A[2:])

while len(q) != 0:
    #print(q)
    a = q.pop()
    #print(a)
    #print(inp[a[0]-1][0])
    cnt += inp[a-1][0]

    #this part will exceed the maximum time
    #AC if u use set()
    #set is faster than array
    for e in inp[a-1][2:]: # until here 2*10^5 
        if e not in f: #this takes time if u use list
            f.append(e)
            q.append(e)


print(cnt)

