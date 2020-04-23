'''
#8?6.py
def towers_of_hanoi(tower1, tower2, tower3, n = None):
    if n == None:
        n = len(tower1.discs)
    if n == 0:
        return 
    
    
    tower3.append(tower1.pop())
    tower2.append(tower1.pop())
    tower2.append(tower3.pop())

class Tower(object):
    def __init__(self, name, discs=None):
        self.name = name
        if discs:
            self.discs = discs
        else:
            self.discs = []

    def __str__(self):
        return self.name

import unittest

class Test(unittest.TestCase):
  def test_towers_of_hanoi(self):
    tower1 = Tower("Tower1", ["6", "5", "4", "3", "2", "1"])
    tower2 = Tower("Tower2")
    tower3 = Tower("Tower3")
    towers_of_hanoi(tower1, tower2, tower3)
    self.assertEqual(tower1.discs, [])
    self.assertEqual(tower2.discs, [])
    self.assertEqual(tower3.discs, ["6", "5", "4", "3", "2", "1"])

if __name__ == "__main__":
  unittest.main()
'''  
#8.9
def parens4(n, partial="", open_count=0, close_count=0):
    if n == 0:
        open_count = 1
        close_count = 1
        print([partial])
        return [partial]
    if open_count < n:
        parens4(n-1, partial + '(', open_count+1, close_count)
    if close_count < open_count:
        parens4(n-1, partial + ')', open_count, close_count+1)
    return partial


import unittest

class Test(unittest.TestCase):
  '''
  def test_parens1(self):
    #self.assertEqual(parens1(1), ["()"])
    #self.assertEqual(parens1(2), ["()()", "(())"])
    self.assertEqual(parens1(3), ["()()()", "()(())", "(())()", "(()())", "((()))"])
    #self.assertEqual(parens1(3), ["()()()", "(())()", "()(())", "(()())", "((()))"])
  
  def test_parens2(self):
      #self.assertEqual(parens2(1), ["()"])
      self.assertEqual(parens2(2), ["(())", "()()"])
      #self.assertEqual(parens2(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])
      #self.assertEqual(set(parens1(7)), set(parens2(7)))

  def test_parens3(self):
    self.assertEqual(parens3(1), ["()"])
    self.assertEqual(parens3(2), ["(())", "()()"])
    self.assertEqual(parens3(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])
    #self.assertEqual(set(parens1(7)), set(parens3(7)))
  '''

  def test_parens4(self):
    #self.assertEqual(parens4(1), ["()"])
    #self.assertEqual(parens4(2), ["(())", "()()"])
    self.assertEqual(parens4(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])
    #self.assertEqual(set(parens1(7)), set(parens4(7)))

if __name__ == "__main__":
  unittest.main()





#8.11
def coins(cents):
    ans = 0
    for 
    ans += coins(cents-25)
    return ans


def coins1_pnd(cents):
    ans = 0
    for 

    return ans

import unittest
class Test(unittest.TestCase):
    def test_coins1(self):
      self.assertEqual(coins1(0), 1)
      self.assertEqual(coins1(1), 1)
      self.assertEqual(coins1(4), 1)
      self.assertEqual(coins1(5), 2)
      self.assertEqual(coins1(15), 6)
      self.assertEqual(coins1(17), 6)
      self.assertEqual(coins1(20), 9)
      self.assertEqual(coins1(25), 13)
      self.assertEqual(coins1(52), 49)
    
    def test_coins2(self):
        for c in range(1000):
            self.assertEqual(coins1(c), coins2(c))
        self.assertEqual(coins2(1000000), 133342333510001)
    
if __name__ == "__main__":
  unittest.main()










