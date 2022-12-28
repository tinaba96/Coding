import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import defaultdict
d = defaultdict(int)

beforeS = str(input())

S = ['(']

for l in range(len(beforeS)):
    S.append(beforeS[l])

S.append(')')

#print(S)
S = ''.join(S)
#print(S)

box = set()

def addItem(i):
    localBox = set()
    if S[i] == '(':
        addItem(i+1)
    while S[i] != ')':
        if S[i] in box:
            print('No')
            exit()
        else:
            box.add(S[i])

    #if S[i] == ')':

stack = []

check = [False for g in range(3*10**5+1)]
now = 0
for s in range(len(S)):
    if S[s] != '(' and S[s] != ')':
        if check[d[S[s]]] == True:
            #print(s, S[s])
            print('No')
            exit()
        d[S[s]] = now

    if S[s] == '(':
        now += 1
        stack.append(now)
        check[now] = True

    if S[s] == ')':
        p = stack.pop()
        check[p] = False
        now += 1


print('Yes')

