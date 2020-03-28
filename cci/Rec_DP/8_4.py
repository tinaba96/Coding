def power_set(set0):
    ps = {frozenset()}
    for ele in set0:
        addition = set()
        for sub in ps:
            addition.add(sub.union(ele))
        ps = ps.union(addition)
    return ps


import unittest

class Test(unittest.TestCase):
  def test_power_set(self):
    s = {'a', 'b', 'c', 'd'}
    ps = power_set(s)
    self.assertEqual(len(ps), 16)
    subsets = [set(), {'a'}, {'b'}, {'c'}, {'d'},
        {'a', 'b'}, {'a', 'c'}, {'a', 'd'}, {'b', 'c'}, {'b', 'd'}, {'c', 'd'},
        {'a', 'b', 'c'}, {'a', 'b', 'd'}, {'a', 'c', 'd'}, {'b', 'c', 'd'}, s]
    self.assertEqual(ps, set([frozenset(s) for s in subsets]))

if __name__ == "__main__":
  unittest.main()



