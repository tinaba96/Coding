import bisect

N, Q = list(map(int, input().split()))

A = list(map(int, input().split()))

for i in range(Q):
    ok = 10**18 + 10**6
    ng = 0
    k = int(input())
    while(ok-ng > 1):
        m = (ok+ng)//2
        d = bisect.bisect_right(A, m)
        nth = m - d
        if nth >= k:
            ok = m
        else:
            ng = m

    print(ok) 


'''
import sys

#Library Info(ACL for Python/Pypy) -> https://github.com/not522/ac-library-python

def input():
    return sys.stdin.readline().rstrip()

from bisect import bisect_right

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    def solve(K):
        return K - bisect_right(a,K)
    def query(K):
        l = 0 # < K
        r = int(1e18 + 1e6)
        while r - l > 1:
            med = (r + l) // 2
            if solve(med) < K:
                l = med
            else:
                r = med
        return r

    Q = [int(input()) for i in range(q)]
    for v in Q:
        print(query(v))

    return 0


if __name__ == "__main__":
    main()


'''


