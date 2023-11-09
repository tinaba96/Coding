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


mp = [
['tourist', 3858],
['ksun48', 3679],
['Benq', 3658],
['Um_nik', 3648],
['apiad', 3638],
['Stonefeang', 3630],
['ecnerwala', 3613],
['mnbvmar', 3555],
['newbiedmy', 3516],
['semiexp', 3481]]


for i in range(10):
    if S == mp[i][0]:
        print(mp[i][1])
        exit()


