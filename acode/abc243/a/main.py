V, A, B, C = list(map(int, input().split()))

su = A+B+C

amari = V%su
if amari < A:
    print('F')
elif A<=amari<A+B:
    print('M')
else:
    print('T')



