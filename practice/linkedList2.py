class Node:
    def __init__(self, value=''):
        self.prev = None
        self.next = None
        self.value = value

# ini
N = Node()
N.prev = N
N.next = N

# insert v after p
def insertNode(v, p): 
    v.next = p.next
    p.next.prev = v
    p.next = v
    v.prev = p


# deleting v
def deleteNode(v):
    v.prev.next = v.next
    v.next.prev = v.prev

    

# print linked list as an array
def printLinkedList():
    list = []
    v = N.next
    while v != N:
        list.append(v.value)
        v = v.next
    print(list)
    print(v.next.value) # three
    # 一番左のNと一番右のNが連動しているため。（Line10）
    # https://snowtree-injune.com/2018/07/17/post-565/#toc4
    # https://note.com/crefil/n/n7a0d2dec929b

#print(N)
one = Node('one')
two = Node('two')
three = Node('three')

insertNode(one, N)
insertNode(two, N)
insertNode(three, N)


printLinkedList()


