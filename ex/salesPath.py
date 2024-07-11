def get_cheapest_cost(rootNode):
  pass # your code goes here

########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None

  def get_cheapest_cost(rootNode):
    #rootNone.numberOfChildren
    # print(rootNode)
    print(rootNode.children)
    n = len(rootNode.children)
    print(n)
    print(rootNode.cost)
    if n:
        return rootNode.cost
    else:
        # initialize minCost to the largest integer
        minCost = 100000000
        for i in range(n):
            temp = get_cheapest_cost(rootNode.children[i])
            print('t')
            print(temp)
            if temp < minCost:
                minCost = temp
    return minCost + rootNode.cost


# debug your code below
root = Node(0)
root.children = [Node(5), Node(3), Node(6)]
root.children[0].children = [Node(4), Node(2)]
root.children[1].children = [Node(0)]
root.children[2].children = [Node(1), Node(5)]


print(Node.get_cheapest_cost(root)) 

'''
 def get_cheapest_cost(rootNode):
   if not rootNode:
     return 0
   minCost = 0xfffff
   stack = [(rootNode,rootNode.cost)]
   while stack:
     node, cost = stack.pop(-1)
     if node.children:
	for child in node.children:
	  stack.append((child, child.cost + cost))
     else:
	minCost = min(cost, minCost)
   return minCost
'''
