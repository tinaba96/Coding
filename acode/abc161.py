'''

#A
X, Y, Z = list(map(int, input().split()))

X, Y, Z = Z, X, Y 

print(X, Y, Z)

#Aans
X, Y, Z = list(map(int, input().split()))
print(Z, X, Y)

#B
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
all_A = sum(A)
#商の計算をしたくなければ、移行して積にすれば良い
comp = (1/(4*M))*all_A
A.sort(reverse=True)
i = 0
ans = 0
#print(A)
while (i <= M-1):
    if A[i] >= comp:
        ans += 1
    i += 1
#print(M)
#print(ans)
if ans == M:
    print('Yes')
else:
    print('No')

#Bans
def readInts():
  return list(map(int, input().split()))

n,m = readInts()
a = readInts()
s = sum(a)
cnt = 0
for i in range(n):
  if a[i]*4*m >= s:
    cnt += 1
if cnt >= m: print("Yes")
else: print("No")


#C
N, K = list(map(int, input().split()))

val = N%K 
while True:
    bef = val
    val = abs(bef-K)
    if abs(val) >= abs(bef):
        break

print(abs(bef))

#Cans
N, K = map(int,input().split())
r = N%K
a = min(r, K-r)
print(a)


'''
#D
K = int(input())
'''
num = len(str(K))

if K <= 9:
    print(K)
else:
#一つ前の桁までの個数
    if num == 2:
        prev = 9
    elif num == 3:
        prev = 26
    prev = 26
    val = 35
    if num >= 4:
        for i in range(1, num-2):
            val += (prev-(3*i))*3+(6*i)
            prev = (prev-(3*i))*3+(6*i)
    print(val)
'''
def ok(n):
    st = str(n)
    flag = True
    for i in range(len(st)-1):
        if st[i]+2 <= st[i+1] or s[i]-2 >= st[i+1]:
            flag = False
    return flag




arr = []
i = 0
while True:
    if ok(i):
        arr.append(i)
        i =+ 1
    if i == K:
        break


print(arr[-1])


'''
#Dans

k = int(input())
ans = [1,2,3,4,5,6,7,8,9]
now = 0
for i in ans:
  #K番目で止めて方が良いと思う。
  if now == 100000:
    break
  x = int(str(i)[-1])
  for j in range(max(0,x-1),min(x+2,10)):
    mini_ans = i * 10 + j
    ans.append(mini_ans)
    now += 1
print(ans[k-1])

'''



