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


N, K = list(map(int, input().split()))

if N == 0:
    print(0)
    exit()


memoList = [(0, 0) for i in range(45)] # when %10**5, it only comes 0-45

def oneLoop(v):
    i = 0
    while True:
        if  v == 0 or v > 10**5:
            v %= 10**5
            break
        s = str(v)
        tmp = 0
        for i in range(len(s)):
            tmp += int(s[i])
        v += tmp
        i += 1
    return v, i


# preprocess
for p in range(45):
    a, b = oneLoop(p)
    memoList[p] = (a, b)

#print(memoList)

oK = K

a, b = oneLoop(N)
K -= b

t = a

while K > 0:
    #print(K)
    if t == 0:
        print(0)
        exit()
    if K >= memoList[t][1]:
        t = memoList[t][0]
        K -= memoList[t][1]
    else:
        break

if K < 0:
    K = oK
    #print('yrs')


# t is the starting index
while K > 0:
    #print(K)
    s = str(t)
    tmp = 0
    for i in range(len(s)):
        tmp += int(s[i])
    t += tmp
    K -= 1

print(t)


