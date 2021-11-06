def main():
    import sys
    sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline

    N, Q = map(int, input().split(" "))
    next = [-1] * (N + 1)
    prev = [-1] * (N + 1)

    for _ in range(Q):
        i = list(map(int, input().split(" ")))

        query = i[0]
        if query == 1:
            x, y = i[1:]
            next[x] = y
            prev[y] = x
        elif query == 2:
            x, y = i[1:]
            next[x] = -1
            prev[y] = -1
        else:
            x = i[1]
            cur = x

            while cur != -1:
                tmp = cur
                cur = prev[cur]

            cur = tmp
            ans = []
            while cur != -1:
                ans.append(cur)
                cur = next[cur]

            print(len(ans), *ans)


if __name__ == '__main__':
    main()
