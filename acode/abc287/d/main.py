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


S = str(input())
T = str(input())

def comp(s, t):
    for i in range(len(s)):
        if s[i] == '?' or t[i] == '?':
            continue
        if s[i] != t[i]:
            return False
    return True

cind = 0
for c in range(1, len(T)+1):
    if comp(S[-c],T[-c]) == True:
        cind += 1
    else:
        break




flg = True
tt = T
ss = S[len(S)-len(T):]

if comp(tt, ss):
    print('Yes')
    flg = True
else:
    print('No')
    flg = False

sflg = True

for i in range(1, len(T)+1):
    ind = len(T) - i
    ss = S[:i] + S[len(S)-ind:]

    if sflg == False:
        print('No')
        continue



    if comp(S[i-1], T[i-1]) == False:
        print('No')
        sflg = False
        flg = False
        continue
    else:
        if flg == True:
            print('Yes')
            flg = True
            continue
        else:
            if ind <= cind:
                print('Yes')
                flg = True
                continue
            else:
                print('No')
                flg = False
                continue




        








