def parens1(n):
    parens_of_length = [[""]]
    if n == 0:
        return parens_of_length[0]
    for length in range(1, n+1):
        parens_of_length.append([])
        for i in range(length):
            for inside in parens_of_length[i]:
                for outside in parens_of_length[length-i-1]:
                    parens_of_length[length].append("(" + inside + ")" + outside)
    return parens_of_length[n]




import unittest

class Test(unittest.TestCase):
  def test_parens1(self):
    self.assertEqual(parens1(1), ["()"])
    self.assertEqual(parens1(2), ["()()", "(())"])
    self.assertEqual(parens1(3), ["()()()", "()(())", "(())()", "(()())",
        "((()))"])
  



if __name__ == "__main__":
  unittest.main()



