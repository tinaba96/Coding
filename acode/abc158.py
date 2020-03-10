'''
#A
N = str(input())
if N=='AAA' or N=='BBB':
    print('No')
else:
    print('Yes')

#B
N, A, B = list(map(int, input().split()))
su = A + B
ans = (N//su)*A
ext = N%su
if ext <= A:
    ans += ext
else:
    ans += A

print(ans)

#C
import math
A, B = list(map(int, input().split()))
ans1min = A/0.08
ans1max = (A+1)/0.08
ans2min = B/0.1
ans2max = (B+1)/0.1

#print(ans1min)
#print(ans2min)
if ans1min >= ans2min and ans1min < ans2max:
    print(math.ceil(ans1min))
elif ans1min <= ans2min and ans2min < ans1max:
    print(math.ceil(ans2min))
else:
    print('-1')


'''
#D
from collections import deque
Str = str(input())
Q = int(input())
S = deque(list(Str))
#S.append(list(Str))
#上の方法ではダメ
A = 0
B = []
C = []

for i in range(Q):
    a = list(map(str, input().split()))
    if a[0] == '1':
        if A%2==0:
            if len(B)>1:
                S.extendleft(B)
                B = []
            elif len(B) == 1:
                S.extendleft(B)
                B = []
            if len(C) > 0:
                S.extend(C)
                C = []
        else:
            if len(C)>1:
                S.extendleft(C)
                C = []
            elif len(C) == 1:
                S.extendleft(C)
                C = []
            if len(B) > 0:
                S.extend(B)
                B = []
        A += 1
    elif a[1] == '1':
        B.append(a[2])
    else:
        C.append(a[2])

if a[0] != '1':
    if A%2==0:
        if len(B)>1:
            S.extendleft(B)
            B = []
        elif len(B) == 1:
            S.extendleft(B)
            B = []
        if len(C) > 0:
            S.extend(C)
            C = []
    else:
        if len(C)>1:
            S.extendleft(C)
            C = []
        elif len(C) == 1:
            S.extendleft(C)
            C = []
        if len(B) > 0:
            S.extend(B)
            B = []

if A%2 != 0:
    S.reverse()
print(''.join(S))

'''
#Dans

s=str(input())

N=int(input())
cnt=0
f=''
b=''
for i in range(N):
  inp=str(input())
  if len(inp)==1:
    cnt+=1
  else:
    F,c=int(inp[2]),inp[4]
    if F==1:
      if cnt%2==0:
        f=c+f
      else:
        b+=c
    else:
      if cnt%2==0:
        b+=c
      else:
        f=c+f
if cnt%2==0:
  print(f+s+b)
else:
  #リバース処理
  ans=f+s+b
  L=len(ans)
  if L==1:
    print(ans)
  else:
    if L%2==1:
      f=ans[0:L//2]
      s=ans[L//2]
      b=ans[L//2+1:L]
      f_=''.join(list(reversed(b)))
      b_=''.join(list(reversed(f)))
      print(f_+s+b_)
    else:
      f=ans[0:L//2]
      b=ans[L//2:L]
      f_=''.join(list(reversed(b)))
      b_=''.join(list(reversed(f)))
      print(f_+b_)

'''

