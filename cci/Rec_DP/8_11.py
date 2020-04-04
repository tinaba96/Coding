#python2 '/' →python3 '//'　に変更した。
def coins1(cents):
    cnt = 0
    for c in range(cents, -1, -25):
        cnt += coins1_pnd(c) 
    return cnt

def coins1_pnd(cents):
    cnt = 0
    for c in range(cents, -1, -10):
        cnt += (c//5) + 1
    return cnt

#coins2は何をやっているのか理解不能。おそらく計算式を導出した。
def coins2(cents):
    n = cents // 5 
    return int(n*n*n/60.0 + n*n*9/40.0 + n*53/60.0 + 301/240 )

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
