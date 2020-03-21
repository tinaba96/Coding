from collections import deque
from typing import List

'''
class List:
    def __init__(self, x):
        x = [x]
'''

#2
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        #上の「x:（この部分）」は関係ない？
        self.val = x
        self.next = None
    '''
    def ListNode2(x, y, z):
        ListNode(x).val = x
        ListNode(y).val = y
        ListNode(z).val = z
        ListNode(x).next = ListNode(y)
        ListNode(y).next = ListNode(z)
    '''

'''
#If those two are arrays
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = [0]*len(l1)
        print(len(l1))
        for i in range(len(l1)-1):
            ans[i] += (l1[i] + l2[i])%10
            ans[i+1] += (l1[i] + l2[i])//10
        
        ans[len(l1)-1] += l1[len(l1)-1] + l2[len(l1)-1]
        ans[len(l1)-1] %= 10

        return ans

print(Solution.addTwoNumbers(None, [2,4,3], [5,6,4]))

'''

class Solution:
    #def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l1.next.next.next = ListNode(1)

        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        l2.next.next.next = ListNode(1)


        dummyHead = ListNode(0)
        current = dummyHead
        #dumyheadがない場合、ここで最初のノードを記述する必要がある。
                
        carry = 0
        print(l1.val)

        while(l1 is not None or l2 is not None):

            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0

            total = carry + x + y
            carry = int(total/10)
            #carry = total//10

            print('A')

            current.next = ListNode(total%10)
            current = current.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry>0 :
            current.next = ListNode(carry)
        print(current.val) #1+1
        return dummyHead.next

    #3
    def lengthOfLongestSubstring(self, s:str) -> int:
        arr = []
        ans = len(arr)
        for ele in s:
            #print(ele)
            #print('ele',ele)
            if ele not in arr:
                arr.append(ele)
            else:
                ans = max(ans, len(arr))
                #print(s[s.index(ele)-len(arr)-1]) 
                p = arr.index(ele)
                del arr[0:p+1]
                arr.append(ele)
                #print(arr)

                '''
                if s[s.index(ele)-len(arr)-1] not in arr:
                    ans = max(ans, len(arr)+1)
                else:
                    #arr.append(ele)
                    ans = max(ans, len(arr))
                '''
                #print(ans)
            ans = max(ans, len(arr))

        return ans
        #解説：https://dev.classmethod.jp/etc/longest-substring-without-repeating-characters/

    #5
    '''
    def longestPalindrome(self, s:str) -> str:
        ans = ""
        #print(len(ans))
        for j in range(len(s)):
            for i in range(1, len(s)+1):
                if s[j:i] == Solution.reverse(s[j:i]):
                    if len(ans) < len(s[j:i]):
                        #print(ans)
                        ans = s[j:i]
        return ans

    def reverse(s:str):
        r  = []
        for i in range(1, len(s)+1):
            r.append(s[-i])
        r = ''.join(r)
        return r
    '''
    def longestPalindrome(self, s):
        largestPalindrome = ''
        for i in range(len(s)):
            palindromeOdd = self.largestPalindromeIndex(s, i, i)
            palindromeEven = self.largestPalindromeIndex(s, i, i+1)

            largerPalindrome = palindromeOdd if len(palindromeOdd) > len(palindromeEven) else palindromeEven
            largestPalindrome = largestPalindrome if len(largestPalindrome) >= len(largerPalindrome) else largerPalindrome
        return  largestPalindrome

            
    def largestPalindromeIndex(self, s, left, right):
        leftIndex = 0
        rightIndex = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                leftIndex = left
                rightIndex = right
            else:
                break
            left -= 1
            right += 1
        return s[leftIndex:rightIndex+1]

    '''
    def convert(self, s:str, numRows: int) -> str:
        for i in range(numRows):
            arr[i] = []
        for i in range(numRows):
            for j in range(len(arr)):
                arr[i] = 
    '''
    def convert(self, s:str, numRows: int) -> str:
        if len(s) == 0: return ''
        if numRows <= 0: return ''
        elif numRows == 1: return s
        
        resRows = ['']*numRows

        i = 0
        resRowNum = 0
        step = 1
        while i < len(s):
            resRows[resRowNum] += s[i]
            #print(resRows[resRowNum])
            if (step == 1 and resRowNum == numRows -1) or (step == -1 and resRowNum == 0):
                step = -1*step

            resRowNum += step
            i += 1

        return ''.join(resRows)
    #11
    def mymaxArea(self, height: List[int]) -> int:
        area = 0
        ans = 0
        for i in range(len(height)//2+1):
            area = (len(height)-1-i)*height[i]
            ans = max(ans, area)
        for i in range(len(height)//2+1, len(height)):
            area = i*height[i]
            ans = max(ans, area)
        return ans

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        ans = 0
        while left < right:
            if height[left] < height[right]:
                area = height[left]*(right-left)
                left  = left + 1
            else:
                area = height[right]*(right - left)
                right = right - 1
            ans = max(ans, area)
        return ans
    '''
    Initially we consider the area constituting the exterior most lines. Now, to maximize the area, we need to consider the area between the lines of larger lengths. If we try to move the pointer at the longer line inwards, we won't gain any increase in area, since it is limited by the shorter line. But moving the shorter line's pointer could turn out to be beneficial, as per the same argument, despite the reduction in the width. This is done since a relatively longer line obtained by moving the shorter line's pointer might overcome the reduction in area caused by the width reduction.
    '''

    #17
    '''
    def myletterCombinations(self, digits:str) -> List[str]:
        table = {}
        final = []
        table['2']  = 'abc'
        table['3'] = 'def'
        table['4'] = 'ghi'
        table['5'] = 'jkl'
        table['6'] = 'mno'
        table['7'] = 'pqrs'
        table['8'] = 'tuv'
        table['9'] = 'wxyz'

        ans = []*(len(table[digits[0]])*len(table[digits[1]]))
        
        if '0' not in digits:
            for j in range(len(table[digits[0]])):
                for i in range(len(table[digits[1]])):
                    ans.append(table[digits[0]][j])
            for k in range(len(table[digits[1]])):
                for l in range(0, len(table[digits[0]])*len(table[digits[1]]), len(table[digits[1]])):
                    ans[k+l] += table[digits[1]][k]
        return ans
    '''
    def letterCombinations(self, digits:str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                ans.append(combination)
            else:
                for letter in phone[next_digits[0]]:
                        backtrack(combination + letter, next_digits[1:])

        ans = []
        if digits:
            backtrack('', digits)
        return ans

    def removeNthFromEnd(self, head:ListNode, n:int) -> ListNode:
        current = head
        cnt = 0

        if not head.next:
            return None
        else:
            while current:
                current = current.next
                cnt += 1

            current = head
            for i in range(cnt-n-1):
                current = current.next

            if cnt == n:
                head = head.next
            else:
                delete = current.next
                current.next = delete.next

            return head
    #22
    def mygenrateParenthesis(self, n:int) -> List[int]:
        ans = []
        if n == 0:
            return None
        elif n == 1:
            return '()'
        else:
            for i in range(n):
                left = '('
                left += ')'
                 
    def generateParenthesisBruteForce(self, n) -> List[int]:
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append(''.join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()
                #上を要チェック
                #結構難しい
                #To generate all sequences, we use a recursion. All sequences of length n is just '(' plus all sequences of length n-1, and then ')' plus all sequences of length n-1.

        def valid(A):
            bal = 0
            for c in A:
                if c == '(' : bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans

    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2*N:
                ans.append(S)
                return
            #print(S)
            if left < N :
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)
        backtrack()
        return ans

    #31
    def mynextPermutation(self, nums: List[int]) -> None:

        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]

            left = mergesort(left)
            right = mergesort(right)

            return merge(left, right)
        
        def merge(left, right):
            merged = []
            l_i, r_i = 0, 0

            while l_i < len(left) and r_i < len(right):
                if left[l_i] <= right[r_i]:
                    merged.append(left[l_i])
                    l_i += 1
                else:
                    merged.append(right[r_i])
                    r_i += 1

            if l_i < len(left):
                merged.extend(left[l_i:])
            if r_i < len(right):
                merged.extend(right[r_i:])
            return merged

        #print(mergesort([2,3,5,4,1]))
        baf = []
        nothing = True
        for i in reversed(range(1, len(nums))):
            baf.append(nums[i])
            if nums[i] > nums[i-1]:
                baf.append(nums[i-1])
                baf = list(baf)
                print(baf)
                baf = mergesort(baf)
                print(baf)
                change = baf[baf.index(nums[i-1])+1] 
                print(change)
                nums[len(nums)-len(baf)+1+baf.index(change)], nums[i-1] = nums[i-1], nums[len(nums)-len(baf)+1+baf.index(change)]
                nums[i:] = mergesort(nums[i:])
                #print(nums)
                nothing = False
                break
        if nothing == True:
            #nums = mergesort(nums)
            change = True
            while change:
                change = False
                for i in range(len(nums)-1):
                    if nums[i] > nums[i+1]:
                        nums[i], nums[i+1] = nums[i+1], nums[i]
                        change = True

        print(nums)
        
    def nextPermutation(self, nums: List[int]) -> None:
        k = -1
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i+1]:
                k = i
                break
            i -= 1

        if k == -1:
            nums.reverse()
            return

        l = k + 1
        i = len(nums) - 1
        while i > k+1:
            if nums[k] < nums[i]:
                l = i
                break
            i -= 1

        nums[k], nums[l] = nums[l], nums[k]

        nums[k+1:] = reversed(nums[k+1:])

    #34
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        if target in nums:
            while target != nums[left] or target != nums[right]:
                mid = (left+right)//2
                if nums[mid] > target:
                    right = mid
                elif nums[mid] == target:
                    if target != nums[left]:
                        left += 1
                    if target != nums[right]:
                        right -= 1
                else:
                    if left == mid and target != nums[left]:
                        left += 1
                    elif target != nums[left]:
                        left = mid
                    if target != nums[right]:
                        right -= 1
            return [left, right]
        else:
            return [-1, -1]

    #49
    def groupAnagrams(self, strs: List[int]) -> List[List[str]]]:

 



if __name__ == "__main__":
    s = Solution()
    #print(s.convert('PAYPALISHIRING', 3))
    #print(s.maxArea([1, 2, 4, 5, 8, 6, 2, 5, 4, 8, 3, 7]))
    #print(s.letterCombinations('29'))
    #print(s.removeNthFromEndl([1, 2, 3, 4, 5], 2))
    #リストノードの指定がうまくできない
    #print(s.generateParenthesis(3))
    #print(s.nextPermutation([4,2,3,5,4]))
    print(s.searchRange([4,4,4,4,4],4))



#print(Solution.addTwoNumbers(ListNode, ListNode.ListNode2(2, 4, 3), ListNode.ListNode2(5, 6, 4)))
#print(Solution.addTwoNumbers(ListNode, ListNode(2), ListNode(5)))
#print(Solution.lengthOfLongestSubstring(None, 'pwwkew'))
#print(Solution.longestPalindrome(Solution,'aacdefcaa'))
#上のは動かない→インスタンスを作る必要あり（name == 'main'のとこ）


