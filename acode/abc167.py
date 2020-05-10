'''
#A
S = str(input())
T = str(input())
if S == T[:len(T)-1]:
    print('Yes')
else:
    print('No')
#B
A, B, C, K = list(map(int, input().split()))

if A ==

if K <= A:
    print(K)
else:
    val = K
    val -= A
    ans = A
    if val <= B:
        print(ans)
    else:
        val -= B
        print(ans-val)

#C
from collections import defaultdict
N, M, X = list(map(int, input().split()))
li = defaultdict(list)





for i in range(N):
    ca = list(map(int, input().split()))
    li[ca[0]] = ca[1:]
li = sorted(li.items())

A = [0]*M
for i in range(len(li)):
    su += int(li[i][0])
    for j in range(M):
        A[j] += int(li[i][1][j])
#print(A)
if any(A[j]<X for j in range(len(A))):
    print('-1')
    exit()
#print(len(li))
#print(su)
ans = su
temp = []
tem = []
for i in range(len(li)-1, -1, -1):
    temp = li[i][1]
    tem = [x-y for (x, y) in zip(A, temp)]
    if all(tem[j]>=X for j in range(len(A))):
        #print('minus:', li[i][0])
        ans -= li[i][0]
        A = tem
        continue
    else:
        continue

print(ans)

from collections import defaultdict
N, M, X = list(map(int, input().split()))
li = defaultdict(list)


for i in range(N):
    ca = list(map(int, input().split()))
    li[ca[0]] = ca[1:]
li = sorted(li.items())



su = 0
A = [0]*M
for i in range(len(li)):
    su += int(li[i][0])
    for j in range(M):
        A[j] += int(li[i][1][j])
#print(A)
if any(A[j]<X for j in range(len(A))):
    print('-1')
    exit()
#print(len(li))
#print(su)
ans = su
temp = []
tem = []
for i in range(len(li)-1, -1, -1):
    temp = li[i][1]
    tem = [x-y for (x, y) in zip(A, temp)]
    if all(tem[j]>=X for j in range(len(A))):
        #print('minus:', li[i][0])
        ans -= li[i][0]
        A = tem
        continue
    else:
        continue

print(ans)
'''

#D
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
A = [0] + A
temp = A[1]
ans = 0
for i in range(K-1):
    ans = A[temp]
    temp = A[temp]

print(ans)
    





