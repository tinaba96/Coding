S = str(input())
T = str(input())

#print(len(S))

if len(S) > len(T) or S[0] != T[0]:
    print('No')
    exit()

for i in range(len(S)):
    if S[i] != T[i]:
        print('No')
        exit()
print('Yes')



