from collections import deque

N, X = map(int, input().split())
S = input()

X = deque(f'{X:b}')

for s in S:
    if s == 'U':
        X.pop()
    elif s == 'L':
        X.append('0')
    else:
        X.append('1')

print(int(''.join(X), 2))
