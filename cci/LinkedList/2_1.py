
from LinkedList import LinkedList

def remove_dups(ll):
  if ll.head is None:
    return

  current = ll.head
  seen = set([current.value])
  while current.next:
    if current.next.value in seen:
      current.next = current.next.next
    else:
      seen.add(current.next.value)
      current = current.next
  return ll
'''
ll = LinkedList()
ll.generate(100, 0, 9) 
print(ll)
remove_dups(ll)
print(ll)
'''

def remove_dups_followup(ll):
  if ll.head is None:
    return
  #currentとrunner
  current = ll.head
  while current:
    runner = current
    while runner.next:
      if runner.next.value == current.value:
        runner.next = runner.next.next
        #print(runner.next)
#next.nextがない場合はNoneを返していると思われる
      else:
        runner = runner.next
      #print('runner', runner)
    current = current.next
    #print('current:', current)
  return ll.head
#runnerとcurrentが見ている連結リストは同じ

ll = LinkedList([1,1,3,4,2,1,6,7,8])
#ll = LinkedList()
#ll.generate(100, 0, 9) 
#print(ll)
remove_dups_followup(ll)
print(ll)
#print('tail',ll.tail)
