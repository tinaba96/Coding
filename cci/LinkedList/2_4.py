from LinkedList import LinkedList

def partition(ll,x):
  current = ll.tail = ll.head
  print('current:', current)
  print('llinit:', ll)
  print('lltail:', ll.tail)
  print('currentnext:', current.next)

  while current:
    nextNode = current.next
    print('nextNode:' , nextNode)
    current.next = None
    print('ll:',ll)
    if current.value <= x:
      print('head1:', ll.head)
      current.next = ll.head
      ll.head = current 
      print('head2:', ll.head)
    else:
      ll.tail.next = current
      ll.tail = current
    current = nextNode

    if ll.tail.next is not None:
      ll.tail.next = None

ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
partition(ll, ll.head.value)
print(ll)


