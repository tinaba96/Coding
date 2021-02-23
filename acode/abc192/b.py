S = str(input())
flag = True

if len(S) == 1 and S[0].isupper():
    print('No')
    exit()


for s in range(0,len(S)-1, 2):
    if S[s].isupper() or S[s+1].islower():
        flag = False


if flag == True:
    print('Yes')
else:
    print('No')

