import collections
import math

S = str(input())

cnt = collections.Counter(S)

#print(cnt)

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

tmp = combinations_count(4, 2)

#print(tmp)
ans = math.factorial(cnt["o"])*combinations_count(4, cnt["o"])

ans *= cnt["o"]

ans += combinations_count(4, 4-cnt["o"]+1)*(cnt["o"]-1)*cnt["?"]


print(ans)

# this approach needs many if branches and takes much time to code

