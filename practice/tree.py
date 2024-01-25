class Node:
    def __init__(self, value = -1):
        self.left = None
        self.right = None
        self.value = value

def preorder(Node):
    if Node != None:
        print(Node.value)
        preorder(Node.left)
        preorder(Node.right)


def inorder(Node):
    if Node != None:
        inorder(Node.left)
        print(Node.value)
        inorder(Node.right)


def postorder(Node):
    if Node != None:
        postorder(Node.left)
        postorder(Node.right)
        print(Node.value)



Root = Node(10)
Child1 = Node(30)
Child2 = Node(40)
Gchild1 = Node(300)
Gchild2 = Node(400)
Root.right = Child2
Root.left = Child1
Child1.right = Gchild2
Child1.left = Gchild1


#preorder(Root)
#inorder(Root)
postorder(Root)
        

#print(Root.left.left.value)
#print(Child1.left.value)

