'''
#A
N = str(input())

if N == 'ABC':
    print('ARC')
else:
    print('ABC')
#B
N, K = list(map(int, input().split()))
arr = []
for i in range(K):
    C = int(input())
    A = list(map(int, input().split()))
    for ele in A:
        if ele not in arr:
            arr.append(ele)

print(N-len(arr))

#C
from collections import defaultdict 
N, M = list(map(int, input().split()))
H = list(map(int, input().split()))
ans = N
tog = defaultdict(list)
arr = set()
cnt = 0

for i in range(M):
    a, b = list(map(int, input().split()))
    tog[a].append(H[b-1])
    tog[b].append(H[a-1])
    '
    if str(a) not in arr:
        ans -= 1
        arr.add(str(H[a-1]))
    if str(b) not in arr:
        ans -= 1
        arr.add(str(H[b-1]))
    '
#print(tog)
    
for ele in tog:
    #print(tog[ele])
    #print(max(tog[ele]))
    if H[ele-1] > max(tog[ele]):
        #print('ok')
        cnt += 1

#print(len(tog))
t = N - len(tog)
#print(t)
#print(len(arr))
#print(len(tog)+N-cnt)
print(cnt+t)
'''

#D
X = int(input())

for A in range(100):
    for B in range(-50, 50):
        if A**5-B**5 == X:
            print(A, B)
            exit()




