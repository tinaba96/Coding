from collections import defaultdict
N, Q = map(int, input().split())
X = [int(input()) for _ in range(Q)]

num_to_idx= defaultdict(int)
idx_to_num= defaultdict(int)

for i in range(N):
    num_to_idx[i+1] = i
    idx_to_num[i] = i+1

for num in X:
    idx = num_to_idx[num]
    if idx != N-1:
        num_r = idx_to_num[idx+1]
        idx_r = num_to_idx[num_r]
        num_to_idx[num], num_to_idx[num_r] = idx_r, idx
        idx_to_num[idx], idx_to_num[idx_r] = num_r, num
    else:
        num_r = idx_to_num[idx-1]
        idx_r = num_to_idx[num_r]
        num_to_idx[num], num_to_idx[num_r] = idx_r, idx
        idx_to_num[idx], idx_to_num[idx_r] = num_r, num

ans = [None]*N
for i in range(1, 1+N):
    ans[num_to_idx[i]] = i
print(*ans)
