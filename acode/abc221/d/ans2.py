from collections import defaultdict
N = int(input())
MAXX = 2*(10**5)+2
count = defaultdict(int)
elemz = set()
for i in range(N):
    a, b = map(int, input().split())
    count[a] += 1
    count[a+b] -= 1
    elemz.add(a)
    elemz.add(a+b)


elem = sorted(list(elemz))
M = len(elem)
countD = [0]*(N+1)
#print(elem)
#print(count)
for i in range(1, M):
    dist = elem[i]-elem[i-1]
    #print(elem[i], elem[i-1], count[elem[i]], count[elem[i - 1]])
    count[elem[i]] += count[elem[i-1]]
    countD[count[elem[i-1]]] += dist
print(*(countD[1:]))

# ans.py and ans2.py is the same approach
