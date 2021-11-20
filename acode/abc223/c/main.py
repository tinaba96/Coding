N = int(input())
tot = 0
road = [0 for i in range(N+1)]
t = []
cum = [0 for i in range(N+1)]
for i in range(N):
    a, b= list(map(int, input().split()))
    tot += a/b
    t.append(a/b)
    road[i] = b
    cum[i] = cum[i-1]+a


#print(tot)

time = tot/2
#print(cum)
dis = 0
for i in range(N):
    if time > t[i]:
        time -= t[i]
    elif time == t[i]:
        dis = cum[i]
        break
    else:
        #print('time', time, '  ', 't', t[i])
        #print('c', cum[i-1])
        #print('yes')
        dis = time*road[i]
        #print(road)
        #print('time', time)
        dis += cum[i-1]
        break

print(dis)




# same approach
'''
n = int(input())
doukasen = [tuple(map(int, input().split())) for _ in range(n)]

t_sum = 0
for i in range(n):
    t_sum += doukasen[i][0]/doukasen[i][1]

t_sum /= 2

i = 0
sum = 0
while(True):
    t = doukasen[i][0]/doukasen[i][1]
    if t_sum - t > 0:
        t_sum -= t
        sum += doukasen[i][0]
    else:
        break
    i+=1

sum += t_sum * doukasen[i][1]
print(sum)

'''

