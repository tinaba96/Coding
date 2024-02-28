Ax, Ay = list(map(int, input().split()))
Bx, By = list(map(int, input().split()))
Cx, Cy = list(map(int, input().split()))
Dx, Dy = list(map(int, input().split()))


def check_inside(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):
    flag = True
    if Bx-Ax == 0:
        AB = 100100100100
    else:
        AB = (By-Ay)/(Bx-Ax)

    if Cx-Bx == 0:
        BC = 100100100100
    else:
        BC = (Cy-By)/(Cx-Bx)

    if Cx-Ax == 0:
        AC = 100100100100
    else:
        AC = (Cy-Ay)/(Cx-Ax)
       
    if Dx-Bx == 0:
        BD = 100100100100
    else:
        BD = (Dy-By)/(Dx-Bx)

    if Dx-Ax == 0:
        AD = 100100100100
    else:
        AD = (Dy-Ay)/(Dx-Ax)


    n = False #notihign

    if AB > BC:
        if AB > BD and BD > BC:
            n = True
        else:
            flag = False
    if BC > AB:
        if BC > BD and BD > AB:
            n = True
        else:
            flag = False


    if AB > AC:
        if AB > AD and AD > AC:
            n = True
        else:
            flag = False
    if AC > AB:
        if AC > AD and AD > AB:
            n = True
        else:
            flag = False

    if flag:
        return False
    else:
        return True

f = False

f = check_inside(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy)
f = check_inside(Bx, By, Cx, Cy, Dx, Dy, Ax, Ay)
f = check_inside(Cx, Cy, Dx, Dy, Ax, Ay, Bx, By)
f = check_inside(Dx, Dy, Ax, Ay, Bx, By, Cx, Cy)


if f:
    print('No')
else:
    print('Yes')

'''
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

'''
