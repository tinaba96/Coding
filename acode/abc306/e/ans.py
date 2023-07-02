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
            if not q2 or y >= -q2[0][0]: # if x should be in q1
                ans += y - mp[x]
                heappush(q1, [y, x])
            else: # if x should be  in q2
                ly, lx = heappop(q2)
                ly = -ly
                st.remove(x)
                st.add(lx)
                heappush(q1, [ly, lx])
                heappush(q2, [-y, x])
                ans += ly - mp[x]    
    else: # if x is not in st
        while q1 and (q1[0][0] != mp[q1[0][1]] or q1[0][1] not in st):
            heappop(q1)  # number of val that are pushed to heapq is Q times in total -> pop() will also be Q at maximum in total -> ならし計算量O(Q) -> 全体計算量O(QlogN+Q)
        if y > q1[0][0]: # new val from q2 will be insert to q1
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

'''
set() is used for check whether it is in q1.

using heapq, you can not remove the element. -> remove using set()
so I thought I should use set() but it is hard to keep the top K element using set() -> use heapq
it is hard to change the value that are already in heapq which is not minumun -> use two heapq (shown in line 42-48)

heapqは削除ができないため、挿入のみしていく。その代わりに削除されたかどうかをset()で管理していく。
'''
