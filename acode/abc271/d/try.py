import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N, S = list(map(int, input().split()))

mp = []

for r in range(N):
    D = list(map(int, input().split()))
    mp.append(D)

memo = [[0 for i in range(N+1)] for j in range(S+1)]

def search(st, left, i):
    if left == 0:
        print('Yes')
        print(st)
        exit()
    if i == N+1 or left < 0:
        return -1
    #print('S: ', S)
    if memo[left-mp[i-1][0]][i] != -1:
        memo[left-mp[i-1][0]][i] = search(st+'H', left-mp[i-1][0], i+1)


    if memo[left-mp[i-1][1]][i] != -1:
        memo[left-mp[i-1][1]][i] = search(st+'T', left-mp[i-1][1], i+1)


search('', S, 1)
print('No')

