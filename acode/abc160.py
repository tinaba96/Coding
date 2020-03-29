import collections
'''
#A
S = str(input())
if S[2] == S[3] and S[4] == S[5]:
    print('Yes')
else:
    print('No')
#B
X = int(input())

Large = X//500
Small = (X%500)//5

print(Large*1000 + Small*5)


#C
K, N = list(map(int, input().split()))
A = list(map(int, input().split()))

longest = (K-A[-1])+A[0]

for i in range(N-1):
    if longest < A[i+1]-A[i]:
        longest = A[i+1]-A[i]

print(K-longest)

'''
#C
N, X, Y = list(map(int, input().split()))
table = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    for j in range(i, N):
        table[i][j] = j-i
#print(table)

dif = Y-X-1
#print('dif', dif)

for i in range(0, X):
    for j in range(Y-1, N):
        table[i][j] -= dif
#print(table)

for i in range(0, X):
    for j in range(Y-1, 0, -1):
        #print('j',j)
        if table[i][j] < table[i][j-1]-1:
            #print('j-1', j-1)
            table[i][j-1] = 1+table[i][j]

for i in range(Y-1, N):
    for j in range(X-1, N-1):
        #print('j',j)
        if table[j][i] < table[j+1][i]-1:
            #print('j+1', j+1)
            table[j+1][i] = 1+table[j][i]
#print(table)

cnt = collections.Counter(str(table))

for i in range(1, N):
    print(cnt[str(i)])


