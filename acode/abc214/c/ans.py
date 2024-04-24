n = int(int(input()))
S = list(map(int,input().split()))
T = list(map(int,input().split()))

ans = [0] * n

for i in range(n * 2) :
  a = i % n
  
  T[a] = min(T[a] , T[a-1] + S[a-1])
  
for i in T :
  print(i)



