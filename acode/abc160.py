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

#D
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

'''
#Dans

N, X, Y = list(map(int, input().split()))
ans = [0]*(N-1)
for i in range(N):
    for j in range(i+1, N):
        #XとYはインデックスではない
        ans[min(j-i-1, abs(X-i-1) +  abs(Y-j-1))] += 1
print(*ans)

#Danother
import sys
sys.setrecursionlimit(1000000000)
from collections import Counter
def key(x, y):
    return str(x)+str(y)
def main2():
    # TLE
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1

    M = {}
    for i in range(N):
        for j in range(i, N):
            M[key(i, j)] = j - i
    
    def helper(x, y, from_cost):
        if 0 <= x <= N-1 and 0 <= y <= N-1:
            if M[key(x,y)] > from_cost+1:
                M[key(x,y)] = from_cost + 1
                cost = from_cost + 1

                helper(x-1,y, cost)
                helper(x+1,y, cost)
                helper(x,y-1, cost)
                helper(x,y+1, cost)
        
    helper(X, Y, 0)

    cost_list = Counter(list(M.values()))
    for k in range(N-1):
        print(cost_list[k+1])

from collections import deque
INF = 1e10

#BFSを使った解法main3
#要復習

def main3():
    # official TLE
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    ans = [0 for _ in range(N)]
    for sv in range(N):
        dist = [INF for _ in range(N)]
        q = deque([])

        def push(v, d):
            if dist[v] != INF: return
            dist[v] = d
            q.append(v)

        #頂点svに距離0で到達できる
        push(sv, 0)

        while q:
            sv = q.popleft()
            d = dist[sv]
            if sv > 0:
                push(sv-1, d+1)
            if sv < N-1:
                push(sv+1, d+1)
            if sv == X:
                push(Y, d+1)
            if sv == Y:
                push(X, d+1)

        for d in dist:
            ans[d] += 1
    
    for k in range(1, N):
        print(ans[k] // 2)

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    dist = [0 for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            d = min(abs(X-i)+1+abs(j-Y), abs(i-j), abs(Y-i)+1+abs(j-Y))
            dist[d] += 1
    
    for k in range(1, N):
        print(dist[k])
 

main()


