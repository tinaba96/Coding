import sys
import heapq
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import Counter
#mylist = ["apple","banana","apple","apple","orange"]
#mycounter = Counter(mylist)
from collections import defaultdict
#d = defaultdict(int)
from bisect import bisect, insort


N = int(input())
N= 2*10**5
Q = int(input())

card = [[] for i in range(N+1)]
box = [[] for i in range(N+1)]

for i in range(N+1):
    heapq.heapify(card[i])
    heapq.heapify(box[i])
    #card.append(heapq)

'''
check later order of card[2]
heapq.heapify(card[2])
heapq.heappush(card[2], 33)
heapq.heappush(card[2], 23)
heapq.heappush(card[2], 200)
print(card)
print(card[2])
#print(heapq.heappop(card[2]))
'''

    

for q in range(Q):
    x = list(map(int, input().split()))
    if x[0] == 1:
        i = x[1]
        j = x[2]
        #heapq.heappush(box[j],i)
        #heapq.heappush(card[i],j)
        ind = bisect.bisect_left(box[j], i) # tried to do this but realized this doesn't make any difference

    if x[0] == 2:
        i = x[1]
        ans = []
        for a in range(len(box[i])):
            #print(heapq.heappop(box[i]))
            val = heapq.heappop(box[i])
            ans.append(val)
            heapq.heappush(box[i], val)
        print(*ans)
    if x[0] == 3:
        i = x[1]
        ans = []
        ans.append(heapq.heappop(box[i]))
        heapq.heappush(box[i])
        for a in range(1, len(card[i])):
            #print(heapq.heappop(box[i]))
            val = heapq.heappop(card[i])
            heapq.heappush(card[i], val)
            if val != ans[-1]:
                ans.append(val)
        print(*ans)


# main2.py is just a try in the contest. this time, it was not good approach so decided not to use it.

