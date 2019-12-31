'''
a,b=list(map(int,input().split()))
s=a-2*b
if s<=0:
    print(0)
else:
    print(s)

#2
N=int(input())
d=list(map(int,input().split()))
s=0
for i in range(N):
    for j in range(N-i-1):
        a=d[i]*d[i+j+1]
        s+=a
print(s)

#3
N=int(input())
S=str(input())
a=1
for i in range(N-1):
    if S[i]!=S[i+1]:
        a+=1
print(a)

#D
N = int(input())
L = list(map(int, input().split()))
count = 0
for j in range(len(L)-2):
  for k in range(j+1, len(L)-1):
    for i in range(k+1, len(L)):
      if (L[i] < L[j] + L[k]) and (L[j] < L[k
        count += 1

print(count)


#E
N, M, L = list(map(int, input().split()))
A = []
B = []
C = []
for i in range(M):
  a, b, c = list(map(int, input().split()))
  A.append(a)
  B.append(b)
  C.append(c)
Q = int(input())
S = []
T = []
for i in range(Q):
  s, t = list(map(int, input().split()))
  S.append(s)
  T.append(t)
  
  #double linked list
class Cell:
  def _init_(self, value):
    self.value = x
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def _init_(self):
    self.head = None

  def insert(self, value):
    new = Cell(value)
    tmp = self.head
    if not tmp:
      new.next = new
      new.prev = new
      self.head = new
      return
    while not tmp == self.head:
      tmp = tmp.next
    tmp.prev.next = new
    new.prev = tmp.prev
    new.next = tmp
    tmp.prev = new

  def delete(self, value):
    tmp = self.head
    if not tmp:
      print("[*] List is empty.")
      return
    if tmp.value == value:
      self.head = tmp.next
      tmp = None
      return
    isfound = False
    tmp = tmp.next
    while not tmp == self.head:
      if tmp.value == value:
        isfound == True
        break
      tmp = tmp.next
    if isfound:
      tmp.prev.next = tmp.next
      tmp.next.prev = tmp.prev
      tmp = None
    else:
      print("[*] Data not found")



l = DoublyLinkedList()
l.insert(2)
l.insert(4)
l.insert(21)
l.insert(1)
print(l)


#Eans
import sys
from scipy.sparse.csgraph import floyd_warsha

N, M, L = map(int, input().split())
INF = 10 **9 +1
G = [[float('inf')] * N for i in range(N)]
for i in range(M):
  a, b, c = map(int, input().split())
  a, b = a - 1, b -1
  G[a][b] = c
  G[b][a] = c

#全点間最短距離を計算
G = floyd_warshall(G)

#コストL以下で移動可能な頂点間のコスト1の辺を
E = [[float('inf')] * N for i in range(N)]
for i in range(N):
  for j in range(N):
    if G[i][j] <= L:
      E[i][j] = 1

#全点間最短距離を計算
E = floyd_warshall(E)

#クエリに答えていく
Q = int(input())
for i in range(Q):
  s, t = map(int, input().split())
  s, t = s - 1, t-1
  print(int(E[s][t] - 1) if E[s][t] != float(

'''
#Fans
from collections import Counter

N = int(input())
A = sorted(list(Counter(map(int, input().spli

rest = N
removed = 0
print(A)
for K in range(1, N+1):
  d = K - removed
  print('di',d)
  while A and A[-1] > rest//d:
    rest -= A[-1]
    A.pop()
    removed += 1
    d -= 1
    print('d',d)
    print(A)
  print(rest//d)
