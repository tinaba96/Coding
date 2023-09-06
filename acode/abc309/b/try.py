import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import Counter
#mylist = ["apple","banana","apple","apple","orange"]
#mycounter = Counter(mylist)
from collections import defaultdict
#d = defaultdict(int)


N = int(input())
mp = []
out = ''
left = ''
right = ''
for i in range(N):
    #A = list(map(int, input().split()))
    A = str(input())
    mp.append(A)
    if i != 0 and i != N-1:
        right += A[-1]
        left += A[0]
    if i == 0:
        out = A

out += right
out += mp[-1][::-1]
out += left[::-1]
print(out)

#newOut = out[-1] + out[:-1]

newOut = out[-1] + out[:N*4-4-1] 

print(newOut)

mp[0] = newOut[:N]
if -N+2 == 0:
    mp[-1] = newOut[N*2-2:][::-1]
else:
    mp[-1] = newOut[N*2-2:-N+2][::-1]
#print(newOut[N*2-2:-N+2])

for i in range(N-2):
    r = newOut[N+i]
    l = newOut[N*4-4-i-1]

    mp[i+1] = l + mp[i+1][1:N-1] + r

for a in range(N):
    print(mp[a])

