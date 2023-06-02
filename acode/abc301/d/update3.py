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
#if len(target) > len(S):
for i in range(len(S)):
    if S[i] == '?':
        answer.append('1')
    else:
        answer.append(S[i])

an = ''.join(answer)

decimal_number = int(an, 2)

if decimal_number < N:
    #print('max')
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

last_q = -1

mid_q = -1 # this is new
flag_mid = False # this is new
point = -1

for i in range(len(S)):

    if S[i] == '1' and tt[i] == '0':
        flag = True
        if mid_q == -1:
            mid_q = last_q
            point = i

    if S[i] == '0' and tt[i] == '1':
        flag = True

    if S[i] == '?' and tt[i] == '1':
        last_q = i

    if flag == True and S[i] == '?':
        aa += '1'
        continue
    if S[i] == '?':
        aa += tt[i]
        continue
    aa += S[i]

int_aa = int(aa, 2)

# this was one of the cause of WA but this is not enough -> check below
if mid_q != -1 and int_aa > N:
    list_aa = list(aa)
    list_aa[mid_q] = '0'
    for p in range(mid_q+1, point+1):
        if S[p] == '?':
            list_aa[p] = '1'   # this is needed. to cover necessary "?"

    int_aa = int(''.join(list_aa), 2)

print(int_aa)


'''
input
?1?00?
42
output
29

expected ouput: 25



S ?1?00?
N 101010

'''

