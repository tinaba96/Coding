import sys
import collections

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    A = [[int(x) for x in input().split()] for _ in range(2 * N - 1)]

    q = []
    x = [x for x in range(2 * N - 1, -1, -1)]
    q.append([x, 0])

    ans = 0
    while q:
        a, b = q.pop()
        if len(a) == 2:
            ans = max(ans, b ^ A[a[1]][a[0] - a[1] - 1])
            continue

        # 一番小さい数を選ぶ
        x = a.pop()
        # 一番小さい数の相方を全探索
        for i, next in enumerate(a):
            q.append([a[:i] + a[i + 1:], A[x][next - x - 1] ^ b])

    print(ans)


if __name__ == '__main__':
    main()


