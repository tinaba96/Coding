def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]
  return arr

class heap():
  def __init__(self, arr):
   self.list = []
   for num in arr:
    self.insert(num)

  def percolate_up(self):
    index = len(self.list)-1
    while index != 0 and self.list[index] < self.list[(index-1)//2]:
      self.list = swap(self.list, index, (index-1)//2)
      index = (index-1)//2

  def insert(self, item):
   self.list.append(item)
   self.percolate_up()

  def percolate_down(self):
   if len(self.list) == 2:
     if self.list[0] > self.list[1]:
       self.list = swap(self.list, 0, 1)
    
   index = 0

   while (2*index + 2 <= len(self.list) - 1):
     child_left_index = 2*index + 1
     child_right_index = 2*index + 2
     child_left = self.list[child_left_index]
     child_right  = self.list[child_right_index]

    if self.list[index] > min(child_left, child_right):
      if child_left < child_right:
        swap(self.list, index, child_left_index)
        index = child_left_index
      else:
        self.list = swap(self.list, index, child_right_index)
        index = child_right_index

  def pop_min(self():

