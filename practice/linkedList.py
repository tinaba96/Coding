class Node:
    def __init__(self):
        self.prev = null
        self.next = null
        self.value = null

# ini
N = Node()
N.prev = N
N.next = N

# insert v after p
def insertNode(v, p): 
    p.next = v
    v.prev = p
    v.next = p.next


# deleting v
def deleteNode(v):
    #

# print linked list as an array
def printLinkedList(N):
    #





