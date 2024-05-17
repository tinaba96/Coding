N = int(input())
S = str(input())

from collections import deque

dl = deque('')
dr = deque('')

bef = 0
for i in range(N):
    if S[i] == 'L':
        dr.appendleft(str(i))
    else:
        dl.append(str(i))
    bef = i
dl.append(str(N))

print(' '.join(list(dl+dr)))




