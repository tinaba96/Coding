N = int(input())
T = str(input())

x = 0
y = 0

flag = 'e'

for i in range(len(T)):
    if T[i] == 'S':
        if flag == 'e':
            x += 1
        elif flag == 's':
            y -= 1
        elif flag == 'w':
            x -= 1
        else:
            y += 1
    else:
        if flag == 'e':
            flag = 's'
        elif flag == 's':
            flag = 'w'
        elif flag == 'w':
            flag = 'n'
        else:
            flag = 'e'

print(x, y)

