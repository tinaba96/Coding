def main():
    from bisect import bisect_left

    n, k = map(int, input().split())
    *p, = (int(c) - 1 for c in input().split())

    lis = []
    cnt = []
    r = [-1] * n
    for i, x in enumerate(p, start=1):
        j = bisect_left(lis, x)
        if j == len(lis):
            lis.append(x)
            cnt.append([x])
        else:
            lis[j] = x
            cnt[j].append(x)
        if len(cnt[j]) == k:
            for xi in cnt.pop(j):
                r[xi] = i
            del lis[j]
    print(*r, sep='\n')


if __name__ == "__main__":
    main()

# using del which is not good time complexity (but AC)
