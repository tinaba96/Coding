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

  def isPalindrome(x: int) -> bool:
    a = str(x)[::-1]
    print(a)
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
