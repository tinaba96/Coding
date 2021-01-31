A, B, C = list(map(int, input().split()))

if C == 1:
    if A >= B:
        print('Takahashi')
    else:
        print('Aoki')
else:
    if A <= B:
        print('Aoki')
    else:
        print('Takahashi')




