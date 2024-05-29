r, c = map(int, input().split())

cd = max(abs(8-r), abs(8-c))

if cd%2 == 0:
    print('white')
elif cd%2 == 1:
    print('black')


