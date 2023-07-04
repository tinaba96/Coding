import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N = int(input())
S = str(input())
C = []

for h in range(len(S)):
    C.append(S[h])


flg = False

for i in range(len(C)):
    #print(flg)
    #print(C[i])
    #print("\"")
    if C[i] == "\"":
        # !flg not good??? -> need to use "if not flg"
        if flg == False:
            flg = True
        else:
            flg = False
        flg = flg
    elif C[i] == ',':
        if flg == False:
            C[i] = '.'

print(''.join(C))





