N = int(input())
S = str(input())

cnt = 0
big = 10**9 + 7

for a in range(N):
    if S[a] == "a":
        for t in range(a, N):
            if S[t] == "t":
                for c in range(t, N):
                    if S[c] == "c":
                        for o in range(c, N):
                            if S[o] == "o":
                                for d in range(o, N):
                                    if S[d] == "d":
                                        for e in range(d, N):
                                            if S[e] == "e":
                                                for r in range(e, N):
                                                    if S[r] == "r":
                                                        cnt += 1
                                                        cnt %= big

print(cnt)

