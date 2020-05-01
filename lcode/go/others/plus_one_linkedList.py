
#369

'''
Input: [1,2,3]
Output: [1,2,4]
'''

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        not_nine = sentinel

        while not_nine.next != 9:
            not_nine = not_nine.next
            if not not_nine.next:
                break
            nine = not_nine.next

        if not_nine == sentinel:
            not_nine.val = 1
        else:
            not_nine.val += 1


        while nine:
            nine.val = 0
            nine = nine.next




        return sentinel if sentinel.val else head



