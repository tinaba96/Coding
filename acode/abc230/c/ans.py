import sys
from collections import defaultdict
from itertools import groupby, permutations as pm, combinations as cm, product, combinations_with_replacement as cmrp
sys.setrecursionlimit(1000000)


def input(): return sys.stdin.readline()[:-1]
def insp(): return map(int, input().split())
def stsp(): return input().split()


def solve():
    n,a,b=insp()
    p,q,r,s=insp()



    for i in range(p,q+1):
        for j in range(r,s+1):
            if (i-j)==(a-b) or (i+j)==(a+b):
                print("#",end="")
            else:
                print(".",end="")
        print()
    return 0


if __name__ == "__main__":
    solve()



'''
n,a,b = map(int,input().split())
p,q,r,s = map(int,input().split())

for i in range(p-1,q):
    rowa  = ""
    for j in range(r-1,s):
        if abs(i+1-a) == abs(b-j-1) :
            rowa += "#"
        else:
            rowa += "."
    print(rowa)

N,A,B=map(int,input().split())
P,Q,R,S=map(int,input().split())
lis=[[] for _ in range(Q-P+1)]
for y in range(P,Q+1):
  for x in range(R,S+1):
    if y-A==x-B or y-A==-x+B:
      lis[y-P].append('#')
    else:
      lis[y-P].append('.')
for k in lis:
  print(''.join(k))
      
'''

