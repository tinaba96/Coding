N = str(input())

n = []
left = []
right = []

for i in range(len(N)):
    n.append(int(N[i]))
    
nSort = sorted(n, reverse=True)

if len(nSort)%2 == 0:
    left.append(str(nSort[0]))
    right.append(str(nSort[1]))
    for i in range(2, len(nSort)-1, 2):
        l = ''.join(left)
        r = ''.join(right)
        if int(l) >= int(r):
            right.append(str(nSort[i]))
            left.append(str(nSort[i+1]))
        else:
            right.append(str(nSort[i+1]))
            left.append(str(nSort[i]))
        #print(left, ' ', right)

else:
    even = len(nSort)-1
    left.append(str(nSort[0]))
    right.append(str(nSort[1]))
    for i in range(2, even-1, 2):
        l = ''.join(left)
        r = ''.join(right)
        if int(l) >= int(r):
            right.append(str(nSort[i]))
            left.append(str(nSort[i+1]))
        else:
            right.append(str(nSort[i+1]))
            left.append(str(nSort[i]))



    l = ''.join(left)
    r = ''.join(right)
    if int(l) >= int(r):
        right.append(str(nSort[-1]))
    else:
        left.append(str(nSort[-1]))
    
#print(left)
#print(right)
L = ''.join(left)
R = ''.join(right)


print(int(L)*int(R))

# picks up one by one and put it into 'right' and 'left' depending on the size of 'right' and 'left'
# this is not the best way


