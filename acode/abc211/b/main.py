arr = ['H', '2B', '3B', 'HR']

flag = True

tmp =[]

for i in range(4):
    s = str(input())
    tmp.append(s)



for e in arr:
    if e not in tmp:
        print('No')
        exit()



print('Yes')

