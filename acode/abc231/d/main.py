import collections

N, M = list(map(int, input().split()))

arr = []

for m in range(M):
    A, B = list(map(int, input().split()))
    arr.append(A)
    arr.append(B)

c = collections.Counter(arr)
#print(c)

if M == 0: 
    print('Yes')
    exit()

if max(c.values()) >= 3:
#if 3 in c.values():
    print('No')
    exit()
elif 1 not in c.values():
    print('No')
    exit()

print('Yes')



