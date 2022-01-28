N = int(input())
A = list(map(int, input().split()))



import collections

c = collections.Counter(A)

#print(c)

for i in range(1, N+1):
    if c[i] != 4:
        print(i)
        exit()
