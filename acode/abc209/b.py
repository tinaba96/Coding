N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

t = N // 2

if X >= sum(A)-t:
    print('Yes')
else:
    print('No')

