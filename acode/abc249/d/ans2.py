def d_index_trio():
    from collections import Counter
    N = int(input())
    A = [int(_) for _ in input().split()]

    cnt = Counter(A)
    m = max(A)
    ans = 0
    for q in range(1, m + 1):
        for r in range(1, (m // q) + 1):
            p = q * r
            ans += cnt[p] * cnt[q] * cnt[r]
    return ans

print(d_index_trio())
