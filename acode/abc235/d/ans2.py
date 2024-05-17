#this is other way round from the editorial video

from collections import deque

a,N=map(int,input().split())

def digit(x):
    return len(str(x))

def slide_digit(x,x0):
    d=digit(x)-1
    result=10*(x%(10**d))+x//(10**d)
    if (digit(result)==d+1) and (result!=x0):
        return result
    return -1


queue=deque()
queue.append((N,N,0))
memo=[0]*(10**digit(N)+10)
trigger=True

while len(queue)>0:
    here=queue.popleft()

    if here[0]==1:
        trigger=False
        print(here[2])
        break

    next=slide_digit(here[0],here[1])
    if next>=0:
        if memo[next]==0:
            memo[next]=1
            queue.append((next,here[1],here[2]+1))

    if here[0]%a==0:
        if memo[here[0]//a]==0:
            memo[here[0]//a]=1
            queue.append((here[0]//a,here[0]//a,here[2]+1))


if trigger:
    print(-1)


