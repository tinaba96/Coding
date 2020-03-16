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
            


#print(Solution.addTwoNumbers(ListNode, ListNode.ListNode2(2, 4, 3), ListNode.ListNode2(5, 6, 4)))
#print(Solution.addTwoNumbers(ListNode, ListNode(2), ListNode(5)))
print(Solution.lengthOfLongestSubstring(None, 'pwwkew'))


