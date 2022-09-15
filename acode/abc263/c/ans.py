'''

see the video editorial
- dfs using recursion
- without using recursion

https://www.youtube.com/watch?v=8RI_IJX6VQY

'''

import sys
#
def gil():
  a=list(map(int,sys.stdin.readline().replace("\n","").split()))
  return a
#
def dfs(l):
  global N,M
  global res
  #
  if len(l)==0:
        for i in range(1,M+1):
              dfs(l+[i])
        return 0
  elif len(l)<N and l[-1]==M:
        return 0
  elif len(l)<N:
        for i in range(l[-1]+1,M+1):
              dfs(l+[i])
        return 0
  else:
        res.append(tuple(l))
        return 0
#
N,M=gil()
res=[]
dfs([])
res.sort()
#
for rr in res:
  print(' '.join([str(a) for a in rr]))

'''
import sys
import itertools

rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
for com in itertools.combinations(range(1, m+1), n):
    print(*com)


'''
