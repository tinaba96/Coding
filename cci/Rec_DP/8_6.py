def towers_of_hanoi(tower1, tower2, tower3, n=None):
    if n is None:
        n = len(tower1.discs)
    if n == 0:
        return
    #A タワー1からの動作
    towers_of_hanoi(tower1, tower3, tower2, n-1)
    #B
    disc = tower1.discs.pop()
    tower3.discs.append(disc)
    #C タワー2とタワー3の間での動作
    towers_of_hanoi(tower2, tower1, tower3, n-1)

    '''
    A：一番下のディスクを除いたn-1枚全てをtower1からtower2に移す。
    B：これで、tower1の一番下にあるディスクを動かすことができる。故に、このデイスクをtower3に動かす。
    C：この時、一番大きいデイスクはtower3にある。よって、tower2にあるn-1枚ノイディスクをtower3に移動させる。
    完了
    '''

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

#参考
#https://qiita.com/ka201504/items/e46d6c9bde13e61b3331
