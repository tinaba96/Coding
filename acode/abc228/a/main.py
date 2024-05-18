s, t, x = list(map(int, input().split()))

if s <= x and x < t:
    print('Yes')
elif s >= t and (x >= s or t > x):
    print('Yes')
else:
    print('No')




