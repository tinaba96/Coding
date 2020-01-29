'''
#A

N, M = list(map(int, input().split()))

if N == M:
  print('Yes')
else:
  print('No')

#B


a,b = list(map(str, input().split()))

A = [a for i in range(int(b))]
B = [b for i in range(int(a))]

if a <= b:
  print(''.join(A))
else:
  print(''.join(B))

#C
N = int(input())
p = list(map(int, input().split()))

cnt = 1
mi = p[0]

for i in range(N):
  if mi > p[i]:
    mi = p[i]
    cnt += 1
print(cnt)  

#D

N = int(input())

cnt = 0

for a in range(10,N):
  na = str(a)
  lea = 10*(len(na)-1)
  for b in range(10,N):
    nb = str(b)
    leb = 10*(len(nb)-1)
    if a%10 == b//leb != 0 and b%10 == a//lea != 0:
      cnt += 1
      print('a:',a, 'b:', b)
      print(8%1)

print(cnt)

'''

#Dansarrange
n = int(input())
b=[[0]*9 for i in range(9)]
count = 0

def get_first(num):
    log = 1
    k=num
    while True:
        if k < 10:
            break
        k = k//10
        log+=1
    #print(k,log)
    return k

for i in range(1,n+1):
    f = get_first(i)
    l   = i%10
    if l==0:
        continue
    b[f-1][l-1] +=1
print(b)

for i in range(9):
    for j in range(9):
        count+=b[i][j]*b[j][i]


print(count)




