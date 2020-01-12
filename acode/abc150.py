'''
K, X = map(int, input().split())

ans = 500 * K
if X > ans:
  print('No')
else: 
  print('Yes')

#B
N = int(input())
S = str(input())

cnt = 0

for i in range(0,len(S)-2):
  if S[i]  == 'A' and  S[i+1] == 'B' and S[i+2] == 'C':
   cnt += 1


print(cnt)

#C
import math


N = int(input())
P = map(int, input().split())
Q = map(int, input().split())

cntp = 1
cntq = 1
for i in range(N-1):
  if P[i]<P[i+1]:
    cntp += 0
  else:
    cnpt += math.factorial(N-i-1)


for i in range(N-1):
  if Q[i]<Q[i+1]:
    cntq += 0
  else:
    cntq += math.factorial(N-i-1)

print(abs(cntp -cntq))

#Cans

def fact(a)
  ret = 1
  for i in range(2, a+1)
    ret *= i
  return ret

def count(a, lst):
  cnt = 0
  for atr in lst:
    if atr < a:
      cnt += 1
  return cnt

N = int(input())
Ps = list(map(int, input().split()))
Qs = list(map(int, input().split()))

a = 1
temp = 0
cntP = 1
for i in range(N):
  if N-1-i != 0:
    cntP = cntP + fact(N-1-i) * count(Ps[i], Ps[i+1:])


cntQ = 1
for i in range(N):
  if N-1-i != 0:
    cntQ = cntQ + fact(N-1-i) * count(Qs[i], Qs[i+1:])
print(abs(cntP-cntQ))

#another

import itertools
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

def count_junretsu(retsu):
	# 大きさNの順列を辞書順に作成し、順番にP,Qと比較する
	for i,l in enumerate(itertools.permutations(range(1,N+1))):
		if retsu == list(l):
			return(i+1)

a = count_junretsu(P)
b = count_junretsu(Q)
print(abs(a-b))




#D
N, M = map(int, input().split())
a = list(map(int, input().split()))

A = max(a)
ans = [float]

for i in range(M//A):
  x = 10*A*(i+0.5)
  if x < M:
    ans.append(x)

for i in range(len(a)):
  for ele in ans:
    if ele%a[i] == 5:
      continue
    else:
      ans.pop(ele)    

print (ans)

'''

#Dans

import math
n,m=map(int, input().split())
a=list(map(int, input().split()))
b=[]
s=math.floor(math.log2(max(a)))
buf=0
for i in range(n): #aは偶数なので、1/2した値の配列を作った
    b.append(int(a[i]//2))

for i in range(s+1): #2のi乗ですべての数が割れるかどうか
    for j in b:
        if j%(2**i)==0:
            buf+=1
        else:
            continue
    if buf==n:
        buf=0
        continue
    else:
        break

def lcm(x,y): #最小公倍数を求める関数の定義
    return (x*y)//math.gcd(x,y)

if buf!=0 and buf!=n: #偶奇が入り混じってるとき
    print(0)
elif n==1: #配列の要素が1つしかないとき
    d=int(m//b[0])
    print(int((d+1)//2))
else:
    c=[lcm(b[0],b[1])] #以下のサイクルで求めた最小公倍数を入れる配列
    for i in range(1,n-1):
        x=lcm(c[i-1],b[i+1])
        c.append(x)
        if x<m:
            continue
        else:
            break
    d=int(m//c[len(c)-1]) #最後の値(c[len(c)-1])が配列bの最小公倍数
    ans=int((d+1)//2)
    print(ans)
    





