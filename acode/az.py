'''
import math
N=int(input())
cnt=0
for i in range(int(N/2)):
    if (i+1)!=(N-i-1):
atcoderz.py lines 1-6/24 28%...skipping...
'''
import math
N=int(input())
cnt=0
for i in range(int(N/2)):
    if (i+1)!=(N-i-1):
      cnt+=1
print(cnt)
'''

N=int(input())
D=list(map(int,input().split()))

if D[0]!=0:
  print(0)
  exit()
cnt=1
for i in range(N-2):
  a=D.count(i+1)
  b=D.count(i+2)
  if b!=0:
    cnt *= (a**b)
print(cnt)

