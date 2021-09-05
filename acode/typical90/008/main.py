from collections import defaultdict

N = int(input())
S = str(input())

flag = "a"
m = defaultdict(int)

for n in range(N):
    #print(S[n])
    if flag == "a" and S[n] == "a":
        m["a"] += 1
    if flag == "a" and S[n] != "a":
        flag = "t"

    if flag == "t" and S[n] == "t":
        m["t"] += 1
    if flag == "t" and S[n] != "t":
        flag = "c"

    if flag == "c" and S[n] == "c":
        m["c"] += 1
    if flag == "c" and S[n] != "c":
        flag = "o"

    if flag == "o" and S[n] == "o":
        m["o"] += 1
    if flag == "o" and S[n] != "o":
        flag = "d"

    if flag == "d" and S[n] == "d":
        m["d"] += 1
    if flag == "d" and S[n] != "d":
        flag = "e"

    if flag == "e" and S[n] == "e":
        m["e"] += 1
    if flag == "e" and S[n] != "e":
        flag = "r"

    if flag == "r" and S[n] == "r":
        m["r"] += 1
    if flag == "r" and S[n] != "r":
        flag = "f"

print(m)

