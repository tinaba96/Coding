'''
#A
S = str(input())
T = str(input())
if S == T[:len(T)-1]:
    print('Yes')
else:
    print('No')
#B
A, B, C, K = list(map(int, input().split()))

if A ==

if K <= A:
    print(K)
else:
    val = K
    val -= A
    ans = A
    if val <= B:
        print(ans)
    else:
        val -= B
        print(ans-val)


#ans
#coding :utf-8

A,B,C,K=map(int,input().split())

result=0
t=min(A,K)
result+=t
K-=t
t=min(B,K)
K-=t
t=min(C,K)
result-=t
print(result)



#ans
# B - Easy Linear Programming

a, b, c, k = map(int, input().split())
print(min(k, a, a + a + b - k))

#C
from collections import defaultdict
N, M, X = list(map(int, input().split()))
li = defaultdict(list)

for i in range(N):
    ca = list(map(int, input().split()))
    li[ca[0]] = ca[1:]
li = sorted(li.items())

su = 0
A = [0]*M
for i in range(len(li)):
    su += int(li[i][0])
    for j in range(M):
        A[j] += int(li[i][1][j])
#print(A)
if any(A[j]<X for j in range(len(A))):
    print('-1')
    exit()
#print(len(li))
#print(su)
ans = su
temp = []
tem = []
for i in range(len(li)-1, -1, -1):
    temp = li[i][1]
    tem = [x-y for (x, y) in zip(A, temp)]
    if all(tem[j]>=X for j in range(len(A))):
        #print('minus:', li[i][0])
        ans -= li[i][0]
        A = tem
        continue
    else:
        continue

print(ans)

#ソートして高い方から削っていく方法だと、減らせる一番高い物を減らすより、少し高めのやつを二つ以上減らした方が安くなる可能性があるため、このアルゴリズムだとうまくいかないと考えられる。

#下の方法で探索範囲を広げてもWA(上の理由と同様）。結局全探索しないとACしないと考えられる。
'''
from collections import defaultdict
N, M, X = list(map(int, input().split()))
li = defaultdict(list)

for i in range(N):
    ca = list(map(int, input().split()))
    li[ca[0]] = ca[1:]
li = sorted(li.items())

su = 0
A = [0]*M
for i in range(len(li)):
    su += int(li[i][0])
    for j in range(M):
        A[j] += int(li[i][1][j])
#print(A)
if any(A[j]<X for j in range(len(A))):
    print('-1')
    exit()
#print(len(li))
#print(su)
answer = su
for j in range(len(li)-1, -1, -1):
    ans = su
    temp = []
    tem = []
    for i in range(j, -1, -1):
        temp = li[i][1]
        tem = [x-y for (x, y) in zip(A, temp)]
        if all(tem[j]>=X for j in range(len(A))):
            #print('minus:', li[i][0])
            ans -= li[i][0]
            A = tem
            continue
        else:
            continue
    answer = min(ans, answer)

print(answer)

'''
#ans
N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(N)]

ans = 10 ** 18
for i in range(2 ** N):
    cost = 0
    each_alg = [0 for _ in range(M)]
    for j in range(N):
        if (i >> j) & 1:
            cost += CA[j][0]
            for k in range(M):
                each_alg[k] += CA[j][k+1]
    if min(each_alg) >= X:
        ans = min(ans, cost)

if ans == 10**18:
    print('-1')
else:
    print(ans)



#D
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
A = [0] + A
temp = A[1]
ans = 0
for i in range(K-1):
    ans = A[temp]
    temp = A[temp]

print(ans)
    
#ans
n,k=map(int,input().split())
l=list(map(int,input().split()))

s=1
q=[0]*n
q[0]=1
r=[1]
for i in range(k):
  s=l[s-1]
  if q[s-1]==0:
    q[s-1]+=1
    r.append(s)
    if i==k-1:
      print(s)
  else:
    x=r.index(s)
    mod=len(r)-x
    t=(k-x)%mod
    print(r[x+t])
    break


#snuke1
#include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int,int>;

int main() {
  int n; ll k;
  cin >> n >> k;
  vector<int> a(n);
  rep(i,n) cin >> a[i];

  vector<int> s;
  vector<int> ord(n+1,-1);
  int c = 1, l = 0;
  {
    int v = 1;
    while (ord[v] == -1) {
      ord[v] = s.size();
      s.push_back(v);
      v = a[v-1];
    }
    c = s.size() - ord[v];
    l = ord[v];
  }

  if (k < l) cout << s[k] << endl;
  else {
    k -= l;
    k %= c;
    cout << s[l+k] << endl;
  }
  return 0;
}


#snuke2
#another way　ダブリング
#include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int,int>;

const int D = 60;
const int MAX_N = 200005;
int to[D][MAX_N];

int main() {
  int n; ll k;
  cin >> n >> k;
  rep(i,n) {
    cin >> to[0][i];
    to[0][i]--;
  }
  rep(i,D-1)rep(j,n) {
    to[i+1][j] = to[i][to[i][j]];
  }

  int v = 0;
  for (int i = D-1; i >= 0; --i) {
    ll l = 1ll<<i;
    if (l <= k) {
      v = to[i][v];
      k -= l;
    }
  }
  cout << v+1 << endl;
  return 0;
}

'''
