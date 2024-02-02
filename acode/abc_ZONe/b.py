N, D, H = list(map(int, input().split()))
ma = 0
ans = 0.0000000
for n in range(N):
    d, h = list(map(int , input().split()))
    '''
    if ma <= h/d:
        tmph = h
        tmpd = d
         '''
    tmp = (D*h-d*H)/(D-d)
    #ans = (D*tmph-tmpd*H)/(D-tmpd)
    ans = max(ans, tmp)

#print('h', tmph)
#print('d', tmpd)


#print(max(ans, 0.0000))
print(ans)





