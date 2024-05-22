#best way
import itertools

s, k = map(str, input().split())
ans = set(list(itertools.permutations(s, len(s))))
ans = sorted(ans)
print(''.join(ans[int(k)-1]))

#answer for my approach
memo = [0]*9
memo[0] = 1
def factorial(k):
    if memo[k] == 0:
        memo[k] = k*factorial(k-1)
    return memo[k]
S,K = input().split()
S = list(S)
K = int(K)
S.sort()

CharKind = []
CharNums = []
tmp = ""
for c in S:
    if c == tmp:
        CharNums[-1]+=1
    else:
        tmp = c
        CharKind.append(c)
        CharNums.append(1)
# 残った文字で作ることが出来るパターン数を求める関数
def patt(l):
    a = factorial(l)
    for i in CharNums:
        a /= factorial(i)
    return a

ans = []
l = len(S)
while l > 0:
    for i in range(len(CharKind)):
        if CharNums[i] == 0:
            continue
        CharNums[i] -= 1
        k = patt(l-1)
        if k >= K:
            ans.append(CharKind[i])
            l -= 1
            break
        CharNums[i] += 1
        K -= k
print(*ans,sep="")

#sbuje's answer
def dfs(now, s, used, strings):
    if False not in used:
        strings.add(now)
        return

    for i in range(len(s)):
        if not used[i]:
            used[i] = True
            dfs(now + s[i], s, used, strings)
            used[i] = False


def main():
    s, k = input().split()
    s = sorted(list(s))
    k = int(k)
    used = [False for _ in range(len(s))]
    strings = set() #st <- snuke

    dfs("", s, used, strings)
    strings = sorted(list(strings))
    print(strings[k - 1])


if __name__ == "__main__":
    main()



