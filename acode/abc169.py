'''

#A
A, B = list(map(int, input().split()))

print(A*B)


#B
N = input()
ans = 1
A = list(map(int, input().split()))

if 0 in A:
    print('0')
    exit()

#for ele in A:
    ans *= ele
    if ans > (10**18):
        print('-1')
        exit()

print(ans)


#C
A, B = list(map(str, input().split()))

a = int(A)
b = int(B[0])
b2 = int(B[2:4])
#print(b)
#print(b2)
#print(b)
if b == 0:
    print(0)
    exit()

t = a*b
#print(t)
#b3 = b*100
bb = a*b2
tmp = bb//100
#print(tmp)
#print(a*b)
bef = tmp+t
ans = str(bef)

print(ans)



#tmp = A * int(B)
#tmptmp = B*100
#tmp2 = A * int((B-tmptmp//100)*100)
#print(int((B-tmptmp//100)*100))
#print(int((tmp + tmp2//100)//1))

#A = int(A)
#print(int(A))
#tmp = A*B*100
#print(int(tmp)//100)
#print(float(A*B))
#print(int(A*B))

'''
#D
N = int(input())
cnt = 0

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
from collections import Counter

arr = prime_factorize(N)
c = Counter(arr)
cnt += len(c)
#print(cnt)
c = c.most_common()
for i in range(len(c)):
    cnt +=  c[i][1]//3

print(cnt)






