'''
N=int(input())
cnt=0
for i in range(N):
    if (i+1)%2!=0:
        cnt+=1
print(cnt/N)


N,K=list(map(int,input().split()))
h=list(map(int,input().split()))
cnt=0
for i in range(N):
    if h[i]>=K:
        cnt+=1
print(cnt)



#Go to school
import time
N=int(input())
a=list(map(int,input().split()))
o=[]
start = time.time()
for i in range(N):
    o.append(a.index(i+1)+1)
process_time = time.time() - start
print(process_time)
print(*o)

'''
#巨大なinputを用意できれば上の自分のコードと下のothersの計算時間を比べる
#自分のが遅い理由→index?
#others
import time
N = int(input())
A = list(map(int, input().split()))
B = list(range(1,N+1))
ab = []
start = time.time()
for i in range(N):
    ab.append([A[i], B[i]])
ab.sort()
process_time = time.time() - start
print(process_time)
for i in range(N):
    print(ab[i][1], end = " ")
print()


'''
#others
def solve(string):
    n, *a = map(int, string.split())
    ans = [0] * n
    for i, _a in enumerate(a, 1):
        ans[_a - 1] = str(i)
    return " ".join(ans)

if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))


＃内包表記→余り変わらない
N=int(input())
a=list(map(int,input().split()))
o=[]
[o.append(a.index(i+1)+1) for i in range(N)]
print(*o)

 #myans→未完成
A,B=list(map(int,input().split()))
import math
C=math.gcd(A,B)
print(C)
a=[]
for i in range(C):
    if C%i==0:
        a.append(i)


#others
from fractions import gcd

def solve(string):
    a, b = map(int, string.split())
    g = gcd(a, b)
    ans = 1 if g % 2 else 2
    while g % 2 == 0:
        g //= 2
    for i in range(3, int(g**0.5) + 1, 2):
        if g % i == 0:
            ans += 1
        while g % i == 0:
            g //= i
    return str(ans + 1) if g > 1 else str(ans)

if __name__ == '__main__':
    print(solve(input()))

#others
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

a, b = map(int, input().split())

a_set = set(prime_factorize(a))
b_set = set(prime_factorize(b))
cd = list(a_set & b_set)
print(cd)
print(len(cd)+1)
'''
