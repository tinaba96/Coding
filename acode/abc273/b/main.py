import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

X, K = list(map(int, input().split()))

def my_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p


#for i in range(K):
    #X = my_round(X, -1-i)


from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

for p in range(K):
    keta = str(10**(p))
    keta = '1E' + str(p+1)
    X = Decimal(str(X)).quantize(Decimal(keta), rounding=ROUND_HALF_UP)
    #print(X)

print(int(X))
#print(X)

