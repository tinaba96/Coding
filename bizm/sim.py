nb_sim = 50
M = 100
N = 10000
sim = []
all = [100000 for i in range(M)]
for j in range(nb_sim):
cnt = 0
for i in range(N):
give = random
get = random
if all[give] &gt;= 130:
all[give] -= 130
all[get] += 130

for money in all:
if money == 0:
cnt += 1

sim.append(cnt)

print(sum(sim)/50)
