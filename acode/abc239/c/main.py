import math

x1, y1, x2, y2 = list(map(int, input().split()))

def dis(a, b, c, d):
    return math.sqrt((a-c)**2 + (b-d)**2)


if dis(x1, y1, x2, y2) > 2*math.sqrt(5)+1:
    print('No')
    exit()

x_d = abs(x1-x2)
y_d = abs(y1-y2)

xm = min(x1, x2)
ym = min(y1, y2)

for i in range(-3, x_d+3):
    for j in range(-3, y_d+3):
        p_x = xm + i  
        p_y = ym + j

        if dis(p_x, p_y, x1, y1) == math.sqrt(5) and dis(p_x, p_y, x2, y2) == math.sqrt(5):
            print('Yes')
            exit()

print('No')
