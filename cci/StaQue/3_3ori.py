import sys


class MultiStack:
  def __init__(self, stacksize):
    self.numstacks = 1
    self.array = [0]*(stacksize*self.numstacks)
    self.sizes = [0]*self.numstacks
    self.stacksize = stacksize

  def Push(self, item):
    if self.IsFull(stacknum):
      #raise Exception('stack is full')
      self.numstacks += 1
      stacknum += 1
      print('True')
    print('self.size', self.sizes)
    self.sizes[stacknum] += 1
    self.array[self.IndexOfTop(stacknum)] = item

  def Pop(self, stacknum):
    if self.IsEmpty(stacknum):
      #raise Exception('stack is empty')
      self.numstacks -= 1
      stacknum -= 1
    value = self.array[self.IndexOfTop(stacknum)]
    self.array[self.IndexOfTop(stacknum)] = 0
    self.sizes[stacknum] -= 1
    return value



  def IsEmpty(self, stacknum):
    return self.sizes[stacknum] == 0 

  def IsFull(self, stacknum):
    return self.sizes[stacknum] == self.stacksize

  def IndexOfTop(self,stacknum):
    offset = stacknum * self.stacksize
    return offset + self.sizes[stacknum] - 1


'''
  def Peek(self, stacknum):
    if self.IsEmpty(stacknum):
      raise Exception('stack is empty')
    return self.array[self.IndexOfTop(stacknum)] 

  def Min(self, stacknum):
    return self.minvals[self.IndexOfTop(stacknum)]

''' 

def StackMin():
    newstack = MultiStack(3)
    newstack.Push(5)
    newstack.Push(6)
    newstack.Push(2)
    newstack.Push(7)
    newstack.Push(1)
    newstack.Push(3)
    newstack.Push(1)
    newstack.Push(4)
    newstack.Push(44)
    newstack.Push(2)
    print(newstack.array)
    print(newstack.sizes)
StackMin()


