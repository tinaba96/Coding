A, B, C, D = list(map(int, input().split()))

if A < C:
    print('Takahashi')
elif C < A:
    print('Aoki')
else:
    if B <= D:
        print('Takahashi')
    else:
        print('Aoki')






