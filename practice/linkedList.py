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
    v = N.next
    while v != N:
        print(v.value)
        v = v.next

#print(N)
one = Node('one')
two = Node('two')
insertNode(one, N)
insertNode(two, one)


printLinkedList()


