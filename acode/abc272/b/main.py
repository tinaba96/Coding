import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N, M = list(map(int, input().split()))

mp = []

al = set()

for i in range(M):
    x = list(map(int, input().split()))
    mp.append(x)
    for j in range(1, x[0]+1):
        for k in range(j+1, x[0]+1):
            al.add((x[j], x[k]))

#print(al)


for p in range(1, N+1):
    for q in range(p+1, N+1):
        if (p, q) not in al:
            print('No')
            #print((p, q))
            exit()



print('Yes')










