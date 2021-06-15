A, B, C = list(map(int, input().split()))

'''
f = A**C
s = B**C

if f > s:
    print(">")
elif f < s:
    print("<")
else:
    print('=')
'''

#print('f :', f)
#print('s :', s)

d = {}
ans = 1

def cal(x, y):
    if y not in d:
        if y == 1:
            d[y] = x
        elif y%2==0:
            d[y] = cal(x,y/2)**2
    return d[y]

print('D: ', d)
f = cal(A, C)
s = cal(B, C)

print('f :', f)
print('s :', s)
