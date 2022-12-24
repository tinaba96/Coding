import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


S = str(input())

cnt = 0
ind = 0


while ind < len(S):
    if ind < len(S)-1 and S[ind] == '0' and S[ind+1] == '0':
        ind += 1
    cnt += 1
    ind += 1

print(cnt)

