from collections import deque
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
        resRows = 0
        step = 1
        while 1 < len(s):
            resRows[resRowNum] += s[i]

            if (step == 1 and resRowNum == numRows -1) or (step == -1 and resRowNum == 0):
                step = -1*step

            resRowNum += step
            i += 1

        return ''












            
if __name__ == "__main__":
    s = Solution()
    print(s.convert('aacdefcaa', 3))



#print(Solution.addTwoNumbers(ListNode, ListNode.ListNode2(2, 4, 3), ListNode.ListNode2(5, 6, 4)))
#print(Solution.addTwoNumbers(ListNode, ListNode(2), ListNode(5)))
#print(Solution.lengthOfLongestSubstring(None, 'pwwkew'))
#print(Solution.longestPalindrome(Solution,'aacdefcaa'))
#上のは動かない→インスタンスを作る必要あり（name == 'main'のとこ）


