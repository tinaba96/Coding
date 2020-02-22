'''
#A
A, B, C = list(map(int, input().split()))


if (A == B or B == C or A == C):
  if A == B and B == C and C == A:
    print('No')
  else:
    print('Yes')
else:
  print('No')

#B
N = int(input())
A = list(map(int, input().split()))
flag = 'ap'
for i in range(N):
  if A[i]%2 == 0:
    if A[i]%3 == 0 or A[i]%5 == 0:
      continue
    else:
      flag = 'den'

if flag == 'ap':
  print('APPROVED')
else:
  print('DENIED')

#C
N = int(input())
A = []
B = []
asort = []
for i in range(N):
  A.append(str(input()))
asort = list(set(A))
asort.sort()

for i in range(len(asort)):
  B.append(A.count(asort[i]))
#print(B)
#print(max(B))
ma = max(B)
#print(B.index(ma))
if not N:
  print(0)
while ma in B:
  print(A[B.index(ma)])
  B[B.index(ma)] = 0
  #print(B)

#Cans
n = int(input())
dict1 = {}

for _ in range(n):
    s = input()
    if s in dict1:
        dict1[s] += 1
    else:
        dict1[s] = 1

dict_sorted = sorted(list(dict1.items()), key = lambda x: x[0])
dict_sorted.sort(key = lambda x: x[1], reverse = True)

max1 = dict_sorted[0][1]
#print(dict1)
#print(dict_sorted)

for i in range(len(dict_sorted)):
    if dict_sorted[i][1] == max1:
        print(dict_sorted[i][0])
    else:
        break

#D
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
#print(N)
#case = (N(N-1))/2
com = []
cnt = 0
maxval = A[-1]
if K >= case:
  for i in range(N):
    com.append
  com = 


for i in range(N):
  for j in range(i+1, N):
    com.append(A[i]*A[j])

com.sort()
#print(com)
print(com[K-1])
'''
#Dans
def d_pairs():
    # 参考: https://maspypy.com/atcoder-参加感想-2019-02-16abc-155
    import numpy as np
    N, K = [int(i) for i in input().split()]
    A = np.array([int(i) for i in input().split()], np.int64)

    A = np.sort(A)
    zero = A[A == 0]
    positive = A[A > 0]
    negative = A[A < 0]

    def f(c):
        """数列 A から 2 要素を選んで積を取ったとき、c 以下となるようなペアの選び方"""
        count_pair = 0

        # a (数列の要素) == 0 かつ c >= 0 なら、a * x <= c となる x は数列の任意の要素
        if c >= 0:
            count_pair += len(zero) * N
        # a > 0 の場合
        count_pair += np.searchsorted(A, c // positive, side='right').sum()
        # a < 0 の場合 (全体から引くようにすると、見通しがよい)
        count_pair += (N - np.searchsorted(A, (c + 1) // negative, side='right')).sum()
        #ans: count_pair += (N - np.searchsorted(A, (-c - 1) // (-negative), side='right')).sum()
        #print('tyy:', 7//-3)
        #print(A)
        #print((N - np.searchsorted(A, (-c - 1) // (-negative), side='right')))
        # 添字の順序に制約があることを反映する
        count_pair -= np.count_nonzero(A * A <= c)  # 「添字が同じ要素を 2 度選んだ場合」を引く
        return count_pair // 2
    #print('f10:', f(10))
    # 数列から要素を 2 個選んで積を取ったとき、制約からあり得る値の範囲
    lower, upper = -10 ** 18, 10 ** 18
    while upper - lower > 1:
        x = (lower + upper) // 2
        if f(x) >= K:
            upper = x
        else:
            lower = x
    return upper

print(d_pairs())



