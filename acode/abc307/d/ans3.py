def inp():
  ret = list(map(int, input().split()))
  return ret
  
from collections import deque
  
N = int(input())
s = input()

cnt = 0
que = deque([])

for i in range(N):
  que.append(s[i])
  
  if s[i] == '(':
    cnt += 1
    
  if s[i] == ')' and cnt > 0:
    while que[-1] != '(':
      que.pop()
      
    que.pop()
    cnt -= 1
    
for i in range(len(que)):
  print(que[i], end="")
  #print(que[0], end="")
  #que.popleft()
