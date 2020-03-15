#1, 7, 9, 13, 14, 20, 21

class Solution:
  def twoSum(nums, target) -> int:
    for i in range(len(nums)):
      second = target - nums[i]
      if second in nums:
        if nums.index(second) != i:
          return [i, nums.index(second)]

  def reverse(x: int) -> int:
        if x > 0:  # handle positive numbers
            a =  int(str(x)[::-1])
        if x <=0:  # handle negative numbers
            a = -1 * int(str(x*-1)[::-1])
        # handle 32 bit overflow
        mina = -2**31
        maxa = 2**31 - 1
        if a not in range(mina, maxa):
            return 0
        else:
            return a

  def isPalindrome(self, x: int) -> bool:
    a = str(x)[::-1]
    #print(a)
    if a == str(x):
      return True
    else:
      return False

  def romanToInt( s: str) -> int:
    table={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
    }

    sum = 0
    for i in range(len(s)):
      if i != (len(s)-1):
        if table[s[i]] <  table[s[i+1]]:
          sum -= table[s[i]]
        else:
          sum += table[s[i]]
      else:
        sum += table[s[i]]
    return sum


  def longestCommonPrefix(strs) -> str:
    same = ""
    flag = True
    if strs == []:
      return ""
    for i in range(len(min(strs, key=len))):
      for j in range(len(strs)):
        if j+1 < len(strs) :
          if strs[j][i] == strs[j+1][i]:
            if flag == True:
              flag = True
            else:
              flag = False
          else:
            flag = False
      if flag == True:
        same += strs[0][i]
    return same

  def isValid(s:str) -> bool:
   if s == "":
    return True
   a = []
   for i in range(len(s)):
     if s[i] == "(" or s[i] == "{" or s[i] == "[":
      a.append(s[i])
     elif s[i] == ")" and a != [] and a[-1] == "(":
       a.pop()
     elif s[i] == "}" and a != [] and a[-1] == "{":
       a.pop()
     elif s[i] == "]" and a != [] and a[-1] == "[":
       a.pop()
     else:
      return False
   if a == []:
     return True
   else:
     return False


  def isValidAns(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This
        # Also makes adding more types of parenthesis e
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stac
                # Otherwise assign a dummy value of '#'
                top_element = stack.pop() if stack else

                # The mapping for the opening bracket i
                # element of the stack don't match, ret
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply pu
                stack.append(char)

        # In the end, if the stack is empty, then we ha
        # The stack won't be empty for cases like ((()
        return not stack

  def mergeTwoLists(l1: ListNode, l2: ListNode) -> List
    if not l1:
     return l2
    if not l2:
     return l1
    if l1.val < l2.val:
     l1.next = self.mergeTwoLists(l1.next, l2)
     return l1
    else:
     l2.next = self.mergeTwoLists(l1, l2.next)
     return l2

#26, 27, 28

class Solution():
    #sorted array
    def removeDuplicates(self, nums: [int]) -> int:
        i = 0
        while i<(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                #print(nums[i], end = "")
                print(nums[i])
                i += 1

    def removeElement(self, nums: [int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
            '''
            for i in range(len(needle)):
                for j in range(len(haystack)):
                    if needle[i] == haystack[j]:
            '''
        else:
            return -1

#Solution.removeDuplicates(None, [1, 1, 2, 3, 3, 3, 3, 4, 4, 5])
#print(Solution.removeElement(None, [1, 1, 2, 3, 3, 3, 3, 4, 4, 5], 4))
print(Solution.strStr(None, "hello", "ll"))


#35, 38

class Solution():


