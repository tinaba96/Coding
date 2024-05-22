#best way
import itertools

#s, k = map(str, input().split())
        
s = '0012()'

for v in itertools.permutations(s, len(s)):
    print(v)

#ans = set(list(itertools.permutations(s, len(s))))
#ans = sorted(ans)
#print(''.join(ans[int(k)-1]))


