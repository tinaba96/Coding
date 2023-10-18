# using bit as the status 
from collections import namedtuple
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)
Road = namedtuple('Road', 'city dist')

N, M = list(map(int, input().split()))
d = defaultdict(list)
for _ in range(M):
    A, B, C = list(map(int, input().split()))
    d[A-1].append(Road(B-1, C))
    d[B-1].append(Road(A-1, C))

bit_set = 0
memo = [[0] * 2**N for _ in range(N)]


def bit_set_add(bit, idx):
    return bit | 1 << idx


def bit_set_isin(bit, idx): # 指定したビットが立っているかどうか
    return True if bit & (1 << idx) else False


def dfs(node, cur_set):

    next_set = bit_set_add(cur_set, node) # このノードにたどり着いた時の状態 next_setはわかりにくい？
    if memo[node][next_set] != 0: # メモ化
        return memo[node][next_set]

    _max = 0
    for road in d[node]:
        if bit_set_isin(cur_set, road.city): # すでに訪れたかどうか
            continue
        tmp = dfs(road.city, next_set) + road.dist
        if _max < tmp:
            _max = tmp
    memo[node][next_set] = _max # memo
    return _max


ans = 0
for i in range(N):
    tmp = dfs(i, 0)
    if ans < tmp:
        ans = tmp

print(ans)


# メモ化再帰かな。
# node->N, next_step->2^N, move->total:2M --> overall O(N^3)? or O(N^3+M*N^2)?


