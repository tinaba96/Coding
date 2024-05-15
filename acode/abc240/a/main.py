
a, b = list(map(int, input().split()))


if abs(a-b) == 1:
    print('Yes')
elif a == 10 and b == 1:
    print('Yes')
elif b ==10 and a ==1:
    print('Yes')
else:
    print('No')



