class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = []
        for i in range(len(l1)-1):
            ans[i] += (l1[i] + l2[i])%10
            ans[i+1] += (l1[i] + l2[i])//10
        
        ans[len(l1)-1] += (l1[len(l1-1)] + l2[len(l1)-1])%10


        
