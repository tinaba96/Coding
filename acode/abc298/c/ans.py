n = int(input())
q = int(input())
M = 200010
box = [[] for _ in range(n+1)]
card = [set() for _ in range(M)]
ans = []
for _ in range(q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        i, j = q[1:]
        box[j].append(i)
        card[i].add(j)
    elif q[0] == 2:
        print(' '.join(map(str, sorted(box[q[1]]))))
    else:
        print(' '.join(map(str, sorted(card[q[1]]))))

# you can use sorted() for set()

'''

import pdb
from sys import platform, setrecursionlimit, stdin
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')
#MOD=10**9+7
#MOD=998244353
#MOD= 67_280_421_310_721
#MOD=170_141_183_460_469_231_731_687_303_715_884_105_727
#MOD=20_988_936_657_440_586_486_151_264_256_610_222_593_863_921
INF=10**18
LOW_ALF='abcdefghijklmnopqrstuvwxyz'
UP_ALF='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
debug_print=print if platform=='darwin' else lambda *args:args
debug_trace=pdb.set_trace if platform=='darwin' else lambda *args:args
input=lambda:stdin.readline().strip()
#input=stdin.readline
setrecursionlimit(10**9)

N=int(input())
Q=int(input())

box=[[] for _ in range(N+1)]
cards=[set() for _ in range(2*10**5+1)]
for q in range(Q):
  t,*ij=list(map(int,input().split()))
  if t==1:
    i,j=ij
    box[j].append(i)
    cards[i].add(j)
  elif t==2:
    i=ij.pop()
    print(*sorted(box[i]))
  else:
    i=ij.pop()
    print(*sorted(cards[i]))


'''








