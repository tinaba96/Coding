import bisect

n, q = map(int,input().split())

A = list(map(int, input().split()))

K = []
for _ in range(q):
    k = int(input())
    K.append(k)
#C[i]：Aのi番目の要素以下の数において、Aに含まれない正整数の個数を格納した配列Cを用意

C = [0] * n
for i in range(n):
    C[i] = A[i] - i - 1

for i in range(q):
    # if C[n-1] < K[i]:
    #     print(A[n-1] + (K[i] - C[n-1]))
    # else:
    index = bisect.bisect_left(C,K[i])
    if index == 0:
        ans = K[i]
    else:
        ans = A[index-1] +(K[i] - C[index-1])
    print(ans)
