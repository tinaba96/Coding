def run(n, k, _in):

    limit = (k*k) // 2 + 1

    ng = -1
    ok = 10**9 + 1

    # 今回の制約が N <= 800
    s = [[0 for i in range(n+1)] for j in range(n+1)]

    while ((ng + 1) < ok):
        exist = False
        mid = (ng + ok) // 2
        for i in range(n):
            # 二次元累積和
            for j in range(n):
                s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j]
                if _in[i][j] > mid:
                    s[i+1][j+1] += 1
        for i in range(n-k+1):
            for j in range(n-k+1):
                if (s[i+k][j+k] + s[i][j] - s[i][j+k] - s[i+k][j] < limit):
                    exist = True
        # 二分探索
        if exist:
            ok = mid
        else:
            ng = mid
    print(ok)

if __name__=="__main__":
    n,k = map(int, input().split())
    _in = []
    for _ in range(n):
        _in.append(list(map(int, input().split())))
    run(n, k, _in)

