'''


def count(str1, str2, A, B):
	cnt = 0
	rom_ins = []
	remove = 0
	insert = 0
	str1_len = A
	str2_len = B
	for i in range(B):
		diff_rem_ins = insert - remove 
		if i > A + diff_rem_ins:
			cnt += B - A - diff_rem_ins #insert
			break
		if str1[i] != str2[i]:
		    if i+1 <= A-1 + diff_rem_ins: #実際の配列の大きさは変わらないため、この方法はダメ。
		        if str1[i+1] == str2[i]:
		            cnt += 1 # remove
		            remove += 1
		    if str1[i] == str2[i+1]:
		        cnt += 1
		        insert += 1
		    elif  ([str2[i], str1[i]]) in rom_ins:
		        cnt -= 1
		    else:
		        cnt += 2 # remove & Insert
		        rom_ins.append([str1[i], str2[i]]) # ( [remove, insert] )
		if (i==B-1) and (A+diff_rem_ins > B):
		    cnt += A + diff_rem_ins - B  # remove
		    break
		
	return cnt


T = int(input())
for i in range(T):
    A, B = list(map(int, input().split()))
    str1, str2 = list(map(str, input().split()))
    print(count(str1, str2, A, B))

#上の方法は、replaceをswapと勘違いしてしまったため、より複雑になり,うまく実装できなかった。



#ans
def lcs(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[None]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            #print(dp)
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]


def min_num_edit(str1, str2):
    ll = lcs(str1, str2)

    if len(str1) <= len(str2):
        return len(str2) - ll
    else:
        return len(str2) - ll + len(str1) - len(str2)



str1 = "sunday"
str2 = "saturday"
print(min_num_edit(str1, str2))

'''
#another


def solve(s1, s2, i, j, cache):
    if (i, j) in cache:
        return cache[(i, j)]
    if i == len(s1) or j == len(s2):
        return abs((len(s1) - i) - (len(s2) -j))
    if s1[i] == s2[j]:
        r = solve(s1, s2, i+1, j+1, cache)
    else:
        a = solve(s1, s2, i+1, j, cache)
        b = solve(s1, s2, i, j+1, cache)
        c = solve(s1, s2, i+1, j+1, cache)
        r = min(a, b, c) + 1

    cache[(i, j)] = r
    return r

def main():
    for _ in range(int(input().strip())):
        input()
        s1, s2 = [x for x in input().strip().split()]
        cache = {}
        print(solve(s1, s2, 0, 0, cache))

main()




