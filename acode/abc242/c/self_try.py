import sys

sys.setrecursionlimit(10**6)

N = int(input())

cnt = 0

mp = [[-1 for i in range(10)] for j in range(10000000)]

# 残りrで最後がdのとき、残りの埋め方
def memo(r, d):

    if n != 1 and n != 9:
        val += memo(r-1, d-1)
        val += memo(r-1, d)
        val += memo(r-1, d+1)
    elif n == 1:
        val += memo(r-1, d)
        val += memo(r-1, d+1)
    elif n == 9:
        val += memo(r-1, d-1)
        val += memo(r-1, d)

ans = 0

for i in range(1, 10):
    memo(0, i, i)


print(cnt)

# i think it is possible to do it from left to right like what i tried in main.py

