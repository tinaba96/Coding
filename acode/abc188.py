#just for practicing

'''
#A
X, Y = list(map(int, input().split()))
if X>Y and X-Y<3:
    print('Yes')
elif Y>X and Y-X<3:
    print('Yes')
else:
    print('No')

#other
X, Y = list(map(int, input().split()))
if abs(X-Y)<3:
    print('Yes')
else:
    print('No')

#B
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total = 0

for i in range(N):
    total += A[i]*B[i]

if total == 0:
    print('Yes')
else:
    print('No')
    

#C

N = int(input())
A = list(map(int, input().split()))
tot = 2**N
first = A[0:tot//2]
last = A[tot//2:tot]
if max(first)<max(last):
    print(1+A.index(max(first)))
else:
    print(1+A.index(max(last)))

#D
N, C = list(map(int, input().split()))

x = []
y = []
z = []
cost = [0]*(10**10)

for i in range(N):
    a, b, c = list(map(int, input().split()))

    c*(b-a)

    for r in range(b-a+1):
        cost[b+r] += c
    #x.append(a)
    #y.append(b)
    #z.append(c)

for i in range(len(cost)):
    if cost[i] > C:
        cost[i] = C

print(sum(cost))

'''
#Dans
from collections import defaultdict

n, C = map(int, input().split())

D = defaultdict(int)

for i in range(n):
    a, b, c = map(int, input().split())
    D[a] += c
    D[b+1] -= c
#print(D)
days = list(D.keys())
days.sort()
#print(days)

ans = 0
cost = 0

for i in range(len(days)-1):
    d1 = days[i]
    d2 = days[i+1]
    cost += D[d1]
    ans += min(C, cost) * (d2 - d1)

print(ans)

