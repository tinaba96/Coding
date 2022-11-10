import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N = int(input())
A = list(map(int, input().split()))

minimum = min(A)

a = []

for i in range(30):
        for j in range(30):
            if (2**i)*(3**j) <= 10**9:
                a.append((2**i)*(3**j))

#print(len(a))

fil = set()

cnt = 0

for g in range(N):
    flg = False
    if A[g] in fil:
        flg = True
    fil.add(A[g])
    for c in range(len(a)):
        if A[g] >= a[c] and A[g]%a[c] == 0:
            if A[g]//a[c] in fil:
                flg = True
            fil.add(A[g]//a[c])
    if flg == False:
        print(-1)
        exit()
    else:
        cnt += 1

print(cnt)
