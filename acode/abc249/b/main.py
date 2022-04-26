N = str(input())

if N.islower() or N.isupper():
    print('No')
    exit()


m = set()

for i in range(len(N)):
    if N[i] not in m:
        m.add(N[i])
    else:
        print('No')
        exit()


print('Yes')




