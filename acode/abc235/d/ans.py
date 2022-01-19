import sys,random,bisect
from collections import deque,defaultdict,Counter
from heapq import heapify,heappop,heappush
from itertools import permutations,combinations
import math
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))

a=int(lines[0].split()[0])
n=int(lines[0].split()[1])

l=[-1]*(10**6)
l[1]=0
k=0
q=deque()
q.append(1)
while len(q):
    c=q.popleft()
    dc=l[c]
    if a*c<10**6 and l[a*c]==-1:
        l[a*c]=dc+1
        q.append(a*c)
    s=str(c)
    z=int(s[-1]+s[:-1])
    if z<10**6 and c%10!=0 and c>=10 and l[z]==-1:
        l[z]=dc+1
        q.append(z)
print(l[n])


