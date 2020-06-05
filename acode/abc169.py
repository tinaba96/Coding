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
tmp = (bb)//100
#print(tmp)
#print(a*b)
bef = tmp+t
ans = int(bef+0.5)
print(ans)


A, B = list(map(float, input().split()))
#print(format(A, '.12f'))
#a = float(format(A, '.12f'))
#print(format(B, '.12f'))
#b =float(format(B, '.12f'))
#print(format(a*b, '.12f'))
print(format(int(A)*B, '.12f'))
print(A*B)
print(int((int(A)*int(B*100+0.5))//100))
#999990000000001 9.99 #A, B
#9989900100000010.0 #A*B
#9989900100000009 # print(int((int(A)*int(B*100+0.5))//100))



#上のコードを動かした結果
~/s/g/t/c/acode ❯❯❯ python abc169.py
1001 9.99
9999.990000000000
9999.99
9999
~/s/g/t/c/acode ❯❯❯ python abc169.py
10001 9.99
99909.990000000005
99909.99
99909
~/s/g/t/c/acode ❯❯❯ python abc169.py
100001 9.99
999009.989999999991
999009.99
999009
~/s/g/t/c/acode ❯❯❯ python abc169.py
1000001 9.99
9990009.990000000224
9990009.99
9990009
~/s/g/t/c/acode ❯❯❯ python abc169.py
10000001 9.99
99900009.990000009537
99900009.99000001
99900009
~/s/g/t/c/acode ❯❯❯ python abc169.py
100000001 9.99
999000009.990000009537
999000009.99
999000009
~/s/g/t/c/acode ❯❯❯ python abc169.py
1000000001 9.99
9990000009.989999771118
9990000009.99
9990000009
~/s/g/t/c/acode ❯❯❯ python abc169.py
10000000001 9.99
99900000009.990005493164
99900000009.99
99900000009
~/s/g/t/c/acode ❯❯❯ python abc169.py
100000000001 9.99
999000000009.989990234375
999000000009.99
999000000009
~/s/g/t/c/acode ❯❯❯ python abc169.py
1000000000001 9.99
9990000000009.990234375000
9990000000009.99
9990000000009
~/s/g/t/c/acode ❯❯❯ python abc169.py
10000000000001 9.99
99900000000009.984375000000
99900000000009.98
99900000000009
~/s/g/t/c/acode ❯❯❯ python abc169.py
100000000000001 9.99
999000000000010.000000000000
999000000000010.0
999000000000009
#9.99が二進数でどのように丸めれれているかを調べようとしたがよくわからなかった。
#A*Bの値がなぜそうなるのかも調べようとした。小数点以下の値が増えたり減ったりする意味がよくわからない。毎回丸めされた値が変わることはないよな〜？
#https://note.cman.jp/convert/bit/を参考
#9.99を64bitの2進数に変換し、再び10進数に直すと以下のようになる。
#9.9899999999999999911182158029987476766109466552734375
#これが関係しているはずだが。。。



#下のコードだとAがfloatであることにより誤差が発生してしまう
A, B = list(map(float, input().split()))
print(A*B)
print(int((A*int(B*100+0.5))//100))

#パソコンは二進数で扱うので、少数を表現するのが非常で苦手である。そのため、floatを用いた計算は、注意が必要。
#https://docs.python.org/ja/3/tutorial/floatingpoint.html
#入力を近似値として保持するため、積を求めようとすると、正確な値が得られない。
#故に、単純にfloatとintをかけて、整数に戻しても違う値が出てしまう。よってWA

A, B = list(map(str, input().split()))

a = int(A)
b = int(B[0])
b2 = int(B[2:4])
#print(b)
#print(b2)
#print(b)

b3 = b*100
bb = b3 + b2
tmp = a*bb
#print(a*b)

print(int(tmp//100))



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


#ans
#解説動画に沿っている。
import math
def get_prime(n):
    if n <= 1:
        return []
    prime = [2]
    if n > 2:
        limit = int(math.sqrt(n))
        odd = [i for i in range(3, n + 1, 2)]
        while limit >= odd[0]:
            prime.append(odd[0])
            odd = [j for j in odd if j % odd[0] != 0]
        prime += odd
    return prime

from collections import defaultdict
def prime_factorization(n):
    if n <= 1:
        return {}
    else:
        # print(int(math.sqrt(n)))
        prime = get_prime(int(math.sqrt(n)))
        dct = defaultdict(int)
        for p in prime:
            while n % p == 0:
                dct[p] += 1
                n //= p
        if n != 1:
            dct[n] += 1
        dct = dict(dct)
        return dct

n = int(input())
pf = prime_factorization(n)

Z = []
for k, v in pf.items():
    for i in range(1, v + 1):
        Z.append(k ** i)
Z.sort()
count = 0
for z in Z:
    if n % z == 0: #こうでないといけない
        count += 1
        n //= z
    if n == 1: #これはなくても良い
        break

print(count)




#anotherans
def p_facto(n):
    ret = []
    nc = n
    for i in range(2, nc):
        if i*i > nc:
            break
        if n % i == 0:
            ex = 0
            while n % i == 0:
                ex += 1
                n //= i
            ret.append([i, ex])
    if n != 1:
        ret.append([n, 1])
    return ret


def main(N):
    ans = 0
    for p, e in pf:
        ex = 1
        while e >= ex:
            z = p**ex
            if N % z == 0:
                ans += 1
                N //= z
            else:
                break
            e -= ex
            ex += 1
    print(ans)

#下記でもOK
def main(N):
    ans = 0
    for p, e in pf:
        ex = 1
        while True:
            z = p**ex
            if N % z == 0:
                ans += 1
                N //= z
            else:
                break
            ex += 1
    print(ans)


if __name__ == "__main__":
    N = int(input())
    pf = p_facto(N)
    main(N)




