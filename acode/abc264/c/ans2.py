h1,w1 = map(int,input().split())
a_s = []
for _ in range(h1):
    a = list(map(int,input().split()))
    a_s.append(a)

h2,w2 = map(int,input().split())
b_s = []
for _ in range(h2):
    b = list(map(int,input().split()))
    b_s.append(b)



from itertools import combinations
for rows in combinations(list(range(h1)), h2):
    for columns in combinations(list(range(w1)), w2):
        c_s = [[a_s[rows[i]][columns[j]] for j in range(w2)] for i in range(h2)]
        if b_s == c_s:
            print("Yes")
            exit()

print("No")
