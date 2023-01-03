box = ''

for c in input():
    if c.islower():
        if c in box:
            print('No')
            break
    elif c == ')':
        box = box[:box.rindex('(')]
        continue

    box += c
else:
    print('Yes')


