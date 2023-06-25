import sys
#input = sys.stdin.readline
from collections import defaultdict, deque
import math
from bisect import bisect_left
from collections import Counter
from heapq import heappop, heappush, heapify
sys.setrecursionlimit(10**9)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def ARR(x, y, k): return [[k for _ in range(y)] for _ in range(x)]

n, k, q = MAP()
ans = 0
q1 = []
q2 = []
mp = defaultdict(int)
st = set()  # this is for q1
for i in range(q):
    x, y = MAP()
    if mp[x] == y:
        print(ans)
        continue
    if len(st) < k:
        st.add(x)
        ans += y - mp[x]
        heappush(q1, [y, x])
    elif x in st:
        if y > mp[x]:
            ans += y - mp[x]
            heappush(q1, [y, x])
        else:
            #while q2 and (q2[0][0] != -mp[q2[0][1]] or q2[0][1] == x or q2[0][1] in st):
            while q2 and (q2[0][0] != -mp[q2[0][1]] or q2[0][1] in st):
                heappop(q2) # skip unnecessary one (not updated or exist in st)
            if not q2 or y >= -q2[0][0]:
                ans += y - mp[x]
                heappush(q1, [y, x])
            else:
                ly, lx = heappop(q2)
                ly = -ly
                st.remove(x)
                st.add(lx)
                heappush(q1, [ly, lx])
                heappush(q2, [-y, x])
                ans += ly - mp[x]    
    else:
        while q1 and (q1[0][0] != mp[q1[0][1]] or q1[0][1] not in st):
            heappop(q1)
        if y > q1[0][0]:
            ly, lx = heappop(q1)
            st.remove(lx)
            ans += y - ly
            st.add(x)
            mp[x] = y
            heappush(q1, [y, x])
            heappush(q2, [-ly, lx])
        else:
            heappush(q2, [-y, x])      
    mp[x] = y
    print(ans)
