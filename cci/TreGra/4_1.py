import Queue

class Graph():
  def __init__(self):
    self.max_vertices = 6
    self.vertices = [0]*self.max_vertices
    self.count = 0

  def addNode(self, x):
    if self.count < self.max_vertices:
      self.vertices[self.count] = x
      self.count += 1
    else:
      print('graph is full')

  def getNodes(self):
    return self.vertices

class Node:
  def __init__(self, vertex, adjacentLength):
    self.adjacentCount = [0] * adjacentLength

