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
S = str(input())

flg = False
final = False
for i in range(N):
    if S[i] == '*':
        if flg == False:
            print('out')
            exit()
        else:
            final = True

    if S[i] == "|":
        if flg == False:
            flg = True
        else:
            if final == True:
                print('in')
                exit()
            else:
                print('out')
                exit()



