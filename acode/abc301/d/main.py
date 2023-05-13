import math
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
N = int(input())


ans = -1

'''
a = math.log2(10**18)
border = int(a+1)


if  border+1 < len(S):
    print(ans)
    exit()
'''



target = bin(N)[2:]
answer = []

#maximum
if len(target) > len(S):
    for i in range(len(S)):
        if S[i] == '?':
            answer.append('1')
        else:
            answer.append(S[i])

    an = ''.join(answer)

    decimal_number = int(an, 2)

    if decimal_number < N:
        print(decimal_number)
        exit()



tt = '{:0>{}}'.format(target, len(S))

#print(S)
#print(tt)

# minimum
m = ''
for k in range(len(S)):
    if S[k] == '?':
        m += '0'
    else:
        m += S[k]

compare = int(m,2)

if compare > N:
    print(-1)
    exit()

aa = ''
flag = False

for i in range(len(S)):
    if S[i] == '0' and tt[i] == '1':
        flag = True
    if flag == True and S[i] == '?':
        aa += '1'
        continue
    if S[i] == '?':
        aa += tt[i]
        continue
    aa += S[i]

int_aa = int(aa, 2)

print(int_aa)




