Ax, Ay = list(map(int, input().split()))
Bx, By = list(map(int, input().split()))
Cx, Cy = list(map(int, input().split()))
Dx, Dy = list(map(int, input().split()))

if Bx-Ax == 0:
    D_AB = 100100100100
else:
    AB = (By-Ay)/(Bx-Ax)

    yy = By - AB*Bx

    D_AB = AB*Dx + yy

if Cx-Bx == 0:
    D_BC = 100100100100
else:
    BC = (Cy-By)/(Cx-Bx)
    
    yy = Cy - BC*Cx
    D_BC = BC*Dx + yy


if D_AB < Dy and D_BC > Dy:
    print('Yes')
else:
    print('No')


