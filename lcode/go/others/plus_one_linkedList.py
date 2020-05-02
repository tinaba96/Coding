
#369

'''
Input: [1,2,3]
Output: [1,2,4]
'''

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    def __str__(self):
        while self.next:
            print( '%s' % (self.val))
            self = self.next
        return '%s' % (self.val)


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        sentinel = ListNode(0)
        not_nine = sentinel
        sentinel.next = head
        
        nine = None

        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

        if not_nine == sentinel:
            not_nine.val = 1
        else:
            not_nine.val += 1

        if not_nine.next:
            nine = not_nine.next
            
        while nine:
            nine.val = 0
            nine = nine.next

        return sentinel if sentinel.val else sentinel.next
    
'''
answer

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # sentinel head
        sentinel = ListNode(0)
        sentinel.next = head
        not_nine = sentinel

        # find the rightmost not-nine digit
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

        # increase this rightmost not-nine digit by 1
        not_nine.val += 1
        not_nine = not_nine.next

        # set all the following nines to zeros
        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next

        return sentinel if sentinel.val else sentinel.next
'''


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(7, ListNode(9)))))
    print(s.plusOne(head))


