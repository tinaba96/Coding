S1 = str(input())
S2 = str(input())

if S1[0] == '#' and S2[0] =='#':
    print('Yes')
    exit()
elif S1[1] == '#' and S2[1] =='#':
    print('Yes')
    exit()
elif S1[0] == '#' and S1[1] == '#':
    print('Yes')
    exit()
elif S2[0] == '#' and S2[1] == '#':
    print('Yes')
    exit()
else:
    print('No')

