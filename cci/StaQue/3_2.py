import sys

class MultiStack:
  def __init__(self, stacksize):
  self.numstacks = 1
  self.array = [0]*(stacksize*self.numstacks)
  self.sizes = [0]*self.numstacks
  self.stacksize = stacksize
  self.minvals = [sys.maxint]*(stacksize*self.numstacks)

  def Push(self, item, stacknum):
    if self.IsFull(stacknum):
      raise Exception('stack is full')
    self.sizes[stacknum] += 1
    if self.IsEmpty(stacknum):
      self.minvals[self.IndexOfTop(stacknum)] = item
    else: 
      self.minvals[self.IndexOfTop(stacknum)] = min(item, self.minvals[self.IndexOfTop(stacknum) -1])
    self.array[self.IndexOfTop(stacknum)] = item

  def Pop(self, stacknum):
    if self.IsEmpty(stacknum):
      raise Exception('stack is empty')
    value = self.array[self.IndexOfTop(stacknum)]
    self.array[self.IndexOfTop(stacknum)] = 0
    self.sizes[stacknum] -= 1
    return value



