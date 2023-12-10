from collections import deque

N = int(input())
inp = []
for i in range(N):
    A = list(map(int, input().split()))
    inp.append(A)

cnt = A[0]

q = set(A[2:])
f = set(A[2:])

while len(q) != 0:
    #print(q)
    a = q.pop()
    #print(a)
    #print(inp[a[0]-1][0])
    cnt += inp[a-1][0]

    #this part will exceed the maximum time
    #no need to use queue since you only need from N to 1 as shown in the video editorial
    for e in inp[a-1][2:]:
        if e not in f:
            f.add(e)
            q.add(e)


print(cnt)

