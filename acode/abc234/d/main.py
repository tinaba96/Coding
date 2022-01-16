import bisect

N, K = list(map(int, input().split()))
P = list(map(int, input().split()))

S = P[:K]
S.sort()
#print(S)
a = S[0]

print(a)

for i in range(K, N):
    index = bisect.bisect_left(S, P[i]) # 2 最も左(前)の挿入箇所が返ってきている
    S.insert(index, P[i])
    if a >= P[i]:
        print(S[-K])
    else:
        print(S[-K])
    # print(S)
        
# O(N(logN+N))  this is too long

#solutions
'''
平衡二分探索木
segtree
priority quque
線形（ならし）
'''





