import itertools
N = int(input())

def check(string):
    cnt = 0
    if string[0] == ')':
        return False
    for j in string:
        #print(stack)
        if j == '(':
            cnt += 1
        else:
            if cnt > 0:
                cnt -= 1
            else:
                return False
    if cnt == 0:
        return True
    else:
        return False


if N%2 == 1:
    print()
    exit()

s = []

for i in range(0, N, 2):
    s.append('(')
    s.append(')')


ans = set(list(itertools.permutations(s, len(s))))
ans = sorted(ans)

for a in ans:
    if check(a):
        print(''.join(a))



#itertools.permutations(s, len(s))はめちゃくちゃ遅い？



