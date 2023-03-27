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


def check(string):
    tar = list(string)
    c = Counter(tar)
    for ele in c:
        if c[ele] != 2:
            return False
    return True



A = str(input())

mp = {}

for i in range(len(A)):
    mp[A[i]] += 1



