N = int(input())
S = str(input())

for i in range(len(S)):
    if S[i] == '1':
        if i % 2 == 0:
            print('Takahashi')
        else:
            print('Aoki')
        exit()


