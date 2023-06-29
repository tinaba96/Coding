# video editorial

S = str(input())

listN = list(S)

for i in range(3, len(S)):
    listN[i] = '0'

print(''.join(listN))
     

