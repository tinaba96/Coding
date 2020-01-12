'''
def f(s):
  lst = s.split()
  return lst[0], int(lst[1])

N = int(input())
S = []
T = []
for i in range(N):
  s, t = f(input())
  S.append(s)
  T.append(t)

X = str(input())

if X in S:
  index = S.index(X)
else:
  print(o)

sum = 0
for i in range(index+1, N):
  sum += int(T[i])

print(sum)


#print('S',S)
#print('T',T)


#B
N = int(input())
x = list(map(int, input().split()))

def build(location):
  return x[N-1] - x[N - 2 - location]

length = 0

longest = x[N-1] = x[0]

for i in range(N-2):
  longest += build(i)

print(longest)



#Bans理解不能
#import collections as c
ip = lambda : map(int, input().split())
# ##############
N = int(input())
l = list(ip())
d = []
for i in range(N-1):
    d.append(l[i+1]-l[i])

ans = 0
mod = int(1e9+7)
c=0
l=1
for i in range(N-1):
    c = ((i+1)*c + l)%mod
    print(c)
    ans = ((i+1)*ans + c*d[i])%mod
    l = l*(i+1)%mod
print(ans)

'''
#anotherRevised
#1/(i+1)に変更したが、最後の階乗をかける段階でオーバーフロー
#原因不明→Nが小さくてもout of range→オーバーフローではない？しかし、階乗の掛け算なくすとエラーでない。
N = int(input())
X = list(map(int, input().split()))
MOD = 10 ** 9 + 7

def prepare(n, MOD):

    # 1! - n! の計算
    f = 1
    factorials = [1]  # 0!の分
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    # n!^-1 の計算
    '''
    inv = pow(f, MOD-2 , MOD)
    print('MOD-2', MOD-2)
    print('f', f)
    print('inv', inv)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    '''
    return factorials, #invs

###
#factが階乗
#rfactが階乗の逆数
fact = prepare(N, MOD)
#fact, rfact = prepare(N, MOD)
print('fact',fact)
#print('rfact',rfact)
ret = 0
inv = 0
#invが期待値
#diffが距離
for i in range(N-1):
    diff = X[i+1] - X[i]
    inv += 1/(i+1)
    #inv += fact[i] * rfact[i+1]
    print('inv', inv)
    ret += diff * inv
    ret %= MOD
    print('ret', ret)
print(ret*fact[N-1]%MOD)
#rfactの部分理解したい→%modの部分も理解できるはず

'''
#another

N = int(input())
X = list(map(int, input().split()))
MOD = 10 ** 9 + 7

def prepare(n, MOD):
 
    # 1! - n! の計算
    f = 1
    factorials = [1]  # 0!の分
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    # n!^-1 の計算
    inv = pow(f, MOD - 2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
     
    return factorials, invs

fact, rfact = prepare(N, MOD)

ret = 0
inv = 0
for i in range(N-1):
    diff = X[i+1] - X[i]
    inv += fact[i] * rfact[i+1]
    ret += diff * inv
    ret %= MOD

print(ret*fact[N-1]%MOD)

'''
