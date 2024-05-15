N = int(input())
a = list(map(int, input().split()))
from collections import deque

t = deque()
v = [a[0], 0]
for i in range(N):
    ball = a[i]
    t.append(ball)
    #print('b', int(ball))
    #print('v', v[1]+1)
    if ball == v[0] and int(ball) == 1+v[1]:
        for k in range(v[1]+1):
            t.pop()
    else:
        if v[0] != ball:
            v[0] = ball
            v[1] = 1
        else:
            v[1] += 1
    print(len(t))
    



