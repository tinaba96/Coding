# not the vest answer

from bisect import bisect
L,Q = map(int,input().split())
cx = [list(map(int,input().split())) for i in range(Q)]
lis = [0,L]
for c,x in cx:
    if c == 1:
        lis.append(x)
lis.sort()
l = len(lis)
flag = [0]*l
flag[0] = flag[-1] = 1
for c,x in cx:
    if c == 1:
        a = bisect(lis,x)
        flag[a-1] = 1
    else:
        a = bisect(lis,x)
        b = a-1
        while flag[a] != 1:
            a += 1
        while flag[b] != 1:
            b -= 1
        print(lis[a]-lis[b])

# I don't know why this is AC
# this will not work in some cases
