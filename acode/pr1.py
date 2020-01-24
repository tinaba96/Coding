'''
a=int(input());
b=list(map(int,input().s
s=input()

sum = a+b[0]+b[1];
print(sum, s)

# -*- coding: utf-8 -*-
# 整数の入力
a = int(input())
# スペース区切りの整数の
b, c = map(int, input().
# 文字列の入力
s = input()
# 出力
print("{} {}".format(a+b

1.py lines 1-18/194 8%...skipping...
'''
a=int(input());
b=list(map(int,input().s
s=input()

sum = a+b[0]+b[1];
print(sum, s)

# -*- coding: utf-8 -*-
# 整数の入力
a = int(input())
# スペース区切りの整数の
b, c = map(int, input().
# 文字列の入力
s = input()
# 出力
print("{} {}".format(a+b


a, b = map(int, input().
p = a*b;

if p%2 == 0:
    print("Even")
else:
    print("Odd")

.py lines 1-27/194 11%...skipping...
'''
a=int(input());
b=list(map(int,input().s
s=input()

sum = a+b[0]+b[1];
print(sum, s)

# -*- coding: utf-8 -*-
# 整数の入力
a = int(input())
# スペース区切りの整数の
b, c = map(int, input().
# 文字列の入力
s = input()
# 出力
print("{} {}".format(a+b


a, b = map(int, input().
p = a*b;

if p%2 == 0:
    print("Even")
else:
    print("Odd")

s=str(input())
cnt=0;
if int(s[-1])==1:
    cnt += 1
.py lines 1-31/194 13%
'''
a=int(input());
b=list(map(int,input().split()));
s=input()

sum = a+b[0]+b[1];
print(sum, s)

# -*- coding: utf-8 -*-
# 整数の入力
a = int(input())
# スペース区切りの整数の入力
b, c = map(int, input().split())
# 文字列の入力
s = input()
# 出力
print("{} {}".format(a+b+c, s))


a, b = map(int, input().split());
p = a*b;

if p%2 == 0:
    print("Even")
else:
    print("Odd")

s=str(input())
cnt=0;
if int(s[-1])==1:
    cnt += 1
if int(s[-2])==1:
    cnt += 1
if int(s[-3])==1:
    cnt += 1

print(cnt)

str=input()
N=int(str)
a=list(map(int, input().split()))
cnt=0
flag=False
while True:
    for i in range(N):
        if a[i]%2==0:
            a[i]=a[i]/2
        else:
            flag=True
            break
    if flag:
        break
    cnt+=1
print(cnt)

A=int(input())
B=int(input())
C=int(input())
X=int(input())
cnt=0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            x=500*a+100*b+50*c
            if X==x:
                cnt+=1
print(cnt)

N, A, B=list(map(int,input().split()))
cnt=0
all = 0
for n in range(N):
    a=str(n+1)
    l=len(str(n+1))
    sum = 0
    for i in range(l):
        sum = sum + int(a[-(i+1)])
    if A <= sum and sum <= B:
        all = all + (n+1)
print(all)

N=int(input())
a=list(map(int,input().split()))
A=0
B=0
while len(a)!=0:
    A=A+max(a)
    a.remove(max(a))
    if len(a)!=0:
        B=B+max(a)
        a.remove(max(a))

sum=A-B
print(sum)

N=int(input())
a=[]
for i in range(N):
    a.append(int(input()))
A=list(set(a))
print(len(A))


N,Y=map(int, input().split())
x=0
y=0
z=0
for x in range(N+1):
    for y in range(N+1):
        z=N-x-y
        if z>=0 and Y==10000*x+5000*y+10
            print(x,y,z)
            exit()
print(-1,-1,-1)

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pdb
import sys
F = sys.stdin

a = list(map(int,F.readline().rstrip().s
N = int(a[0])
Y = int(a[1] / 1000)

sen = int(Y % 5)
ans = [-1, -1, -1]
# pdb.set_trace()

if sen > N :
    print(*ans)
    sys.exit()
for i in range(sen, N+1, 5):
    nokorimaisu = int(N - i)
    nokorikingaku = int(Y - i)
    for j in range(nokorimaisu + 1):
        k = nokorimaisu - j
        if j*5 + k*10 == nokorikingaku:
            ans = [k, j ,i]
print(*ans)

S=input()
Sr=S.replace("eraser","").replace("erase
if Sr=='':
    print('YES')
else:
    print('NO')
'''

N=int(input())
t=[]
x=[]
y=[]
t.append(0)
x.append(0)
y.append(0)
for i in range(N):
    a=list(map(int,input().split()))
    t.append(a[0])
    x.append(a[1])
    y.append(a[2])
flag=True
for i in range(N):
    if flag==True:
        if (t[i+1]-t[i])>=(x[i+1]-x[i]+y
            #print(t[i+1]-t[i])
            flag=True
        elif (t[i+1]-t[i])>=(x[i+1]-x[i]
            #print(t[i+1]-t[i])
            flag=True
        else:
            #print(x[i+1]-x[i]+y[i+1]-y[
            #print(t[i+1]-t[i])
            flag=False
    else:
        break
if flag==False:
    print('No')
else:
    print('Yes')

'''
#others
t, x, y = 0, 0, 0
for i in range(int(input())):
    next_t, next_x, next_y = map(int, in
    diff = abs(x - next_x) + abs(y - nex
    if diff > (next_t - t) or (diff - (n
        print("No")
        exit(0)
    t, x, y, = next_t, next_x, next_y
print("Yes")
'''
