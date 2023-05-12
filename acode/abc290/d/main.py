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


T = int(input())


for t in range(T):
    N, D, K = list(map(int, input().split()))
    ini = D*(K-1) # this is for when there is no Collision
    if N % D == 0: # this is not the only case it will collide -> gcd(N, D) != 1 is the case it will collide (ex. N=12 D=8) 
        if K > N//D:
            ini += (K-1)//(N//D) # ずれた分
    print(ini%N)

# //D is not enough for considering the case for collision. 
# you need to think //gcd(N, D) for collision

# ans.py 参照

