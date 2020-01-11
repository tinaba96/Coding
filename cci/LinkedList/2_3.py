from LinkedList import LinkedList
'''
def delete_middle_node(node):
  node.value = node.next.value
  node.next = node.next.next

ll = LinkedList()
ll.add_multiple([1,2,3,4])
middle_node = ll.add(5)
ll.add_multiple([7,8,9])
'''

def delete_middle_node(ll):
  current = ll.head
  for i in range(len(ll)//2-1):
    current = current.next
  current.next = current.next.next

ll = LinkedList([1,2,3,4,5,6,7,8,9])
#ll.generate(100, 0, 9)

print(ll)
delete_middle_node(ll)
print(ll)
