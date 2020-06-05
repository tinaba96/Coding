#1   1056
class Solution:
    def confusingNumber(self, N: int) -> bool:
        str_num = str(N)
        if "2" in str_num or "3" in str_num or "4" in str_num or  "5" in str_num or  "7" in str_num:
            return False
        elif '9' in str_num or '6' in str_num:
            is_6_9_opp = True
            for i in range(len(str_num)):
                if str_num[i] == '6' and str_num[-i-1] != '9':
                    is_6_9_opp = False
                #if str_num[i] == '6' and str_num[-i-1] == '9':
                  #  is_6_9_opp = True
            if is_6_9_opp == True:
                return False
            else:
                return True
            return True
        else:
            return True

#ans

from copy import deepcopy

class Solution:
    def confusingNumber(self, n: int) -> bool:
        hmap = {'0': '0',
                '1': '1',
                '8': '8',
                '6': '9',
                '9': '6'}

        value = [c for c in str(n)]
        org = deepcopy(value)

        # Checking if value contains other elements
        for i, c in enumerate(value):
            if c not in list(hmap.keys()):
                return False

        # Applying rotation rules
        for i, c in enumerate(reversed(value)):
                value[i] = hmap.get(c)

        org = ''.join(c for c in org)
        value = ''.join(c for c in value)

        if value and value != org: #条件が成り立たない場合は、記述しなくてもFalseになる。
            return True

#anotherans

class Solution:
    def confusingNumber(self, N: int) -> bool:
        copy = N
        rev = 0

        while copy > 0:
            copy, digit = divmod(copy, 10)
            if digit == 6:
                digit = 9
            elif digit == 9:
                digit = 6
            elif digit in (2,3,4,5,7): # invalid when turned 180 degrees
                return False
            rev = rev * 10 + digit

        return True if rev != N else False

#anotherans
class Solution:
    def confusingNumber(self, N: int) -> bool:
        
        rotate = {
            "0":"0",
            "1":"1",
            "2":"x",
            "3":"x",
            "4":"x",
            "5":"x",
            "6":"9",
            "7":"x",
            "8":"8",
            "9":"6"
        }
        
        dgts = list(map(lambda d: rotate[d], str(N)))
        conf = ''.join(dgts)[::-1]
        
        return conf != str(N) and conf.isdigit()

#anotherans
class Solution:
    def confusingNumber(self, N: int) -> bool:
        s1 = str(N)
        r = ""
        for i in s1:
            if i == '2' or i == '3' or i == '4' or i == '5' or i =='7':
                return False
            if i == '6':
                r += '9'
            elif i =='9':
                r += '6'
            else:
                r += i
        if s1 != r[::-1]:
            return True
        else:
            return False


#2  1055
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        cnt = 0
        word_len = len(source)
        while word_len > 0:
            is_not_in_target = True
            for i in range(len(source)-word_len+1):
                if source[i:word_len] in target:
                    cnt += 1
                    target = target.replace(source[i:word_len], '')
                    is_not_in_target = False
                if len(target) == 0:
                    return cnt
            if is_not_in_target:
                word_len -= 1

        return -1


#ans
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        i, minimum = 0, 1
        
        for c in target:
            
			# Get leftmost char after previously matched index
            i = source.find(c, i)

			# If not found
            if i == -1:
                
				# Get leftmost char from begining of string and increase number of concatenated string
                i = source.find(c)
                minimum += 1
                
				# if not found, then target can't be formed. Return -1
                if i == -1:
                    return i
                
            i += 1
                
            
                
        return minimum
#0(N*M)


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
		# First, iterate through the source to find the characters that follows the current one.
		# If there are more than for a certain following character, consider the first one.
		# Running time O(len(source)); space O(len(source) X 26) = O(len(source))
        dic = {}
        for i in range(len(source))[::-1]:
            c = source[i]
            dic[i] = {} if i + 1 not in dic else dic[i + 1].copy()
            dic[i][c] = i + 1
        # For source = 'abba' the table looks like this:
		# {3: {'a': 4}, 2: {'a': 4, 'b': 3}, 1: {'a': 4, 'b': 2}, 0: {'a': 1, 'b': 2}}

        result = 0
        ind = 0
		# Then, iterate throught the target characters
		# Running time O(len(target))
        for char in target:
			# dic[0] contains all characters in the source
            if char not in dic[0]: return -1

			# If 'ind' points to the last character of the source or the current character does not exist in the
			# possible set of characters indicated by 'ind', this means a new subsequence has started
            if ind == len(source) or char not in dic[ind]:
                ind = 0
                result += 1

			# Update the index
            ind = dic[ind][char]

		# After the last increment (two lines above), at least one valid character has been observed
        return result + 1

#O(N+M)
#space 0(M)

:::python
def shortestWay(self, source: str, target: str) -> int:
    inverted_index = collections.defaultdict(list)
    for i, ch in enumerate(source):
        inverted_index[ch].append(i)

    loop_cnt = 1
    i = -1
    for ch in target:
        if ch not in inverted_index:
            return -1
        offset_list_for_ch = inverted_index[ch]
        # bisect_left(A, x) returns the smallest index j s.t. A[j] >= x. If no such index j exists, it returns len(A).
        j = bisect.bisect_left(offset_list_for_ch, i)
        if j == len(offset_list_for_ch):
            loop_cnt += 1
            i = offset_list_for_ch[0] + 1
        else:
            i = offset_list_for_ch[j] + 1

    return loop_cnt

#O(M+N*logM)
#space O(M)



