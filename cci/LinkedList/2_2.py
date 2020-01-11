from LinkedList import LinkedList

def kth_to_last(ll, k):
 runner = current = ll.head
 for i in range(k):
   if runner == None:
     return None
   runner = runner.next

 while runner:
   runner = runner.next
   current = current.next

 return current

ll = LinkedList()
ll.generate(100, 0, 9) 
print(ll)
kth_to_last(ll, 3)
print(ll)
