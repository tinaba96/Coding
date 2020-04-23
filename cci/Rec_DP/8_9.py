# Note that parens1 happens to be faster and more space efficient than parens2,
# which is faster than parens3.  The slowest is parens4 only because it is not
# memoized.

def parens1(n):
    parens_of_length = [[""]]
    if n == 0:
        return parens_of_length[0]
    #n組みの括弧
    for length in range(1, n+1):
        print('length:', length)
        parens_of_length.append([])

        for i in range(length):
            for inside in parens_of_length[i]:
                print('inside:', inside)
                for outside in parens_of_length[length-i-1]: #括弧の数をnにするために、insideとoutsideを用意。故にlength-i-1となる。
                    print('outside:', outside)
                    #括弧の内か外または両方のパターンしかない
                    parens_of_length[length].append("(" + inside + ")" + outside)
                    #parens_of_length[length].append(outside + "(" + inside + ")" )
                    #上記もok
                    print('parens_of_length:',parens_of_length)

    return parens_of_length[n]

def parens2(n, open_count=0, close_count=0, memo=None):
    if open_count + close_count == 2*n:
        return [""]
    key = (n - open_count - close_count, open_count)
    if memo is None:
        memo = {}
    elif key in memo:
        return memo[key]
    parens = []
    #右から順に決めていく
    if open_count < n:
        parens += ["(" + end for end in parens2(n, open_count+1, close_count, memo)]
        print('parens1', parens)
    if close_count < open_count:
        parens += [")" + end for end in parens2(n, open_count, close_count+1, memo)]
        print('parens2', parens)
    memo[key] = parens
    print(memo)
    return parens

def parens3(n):
  return parens_memo3(n, 0, 0, {})

def parens_memo3(n, open_count, close_count, memo):
  if open_count + close_count == 2 * n:
    return [""]
  key = (n - open_count - close_count, open_count)
  if key in memo:
    return memo[key]
  parens = []
  if open_count < n:
    for end in parens_memo3(n, open_count + 1, close_count, memo):
      parens.append("(" + end)
  if close_count < open_count:
    for end in parens_memo3(n, open_count, close_count + 1, memo):
      parens.append(")" + end)
  memo[key] = parens
  return parens

#一番分かりやすい
def parens4(n, partial="", open_count=0, close_count=0):
  if open_count + close_count == 2 * n:
    return [partial]
  parens = [] #important
  if open_count < n:
    parens += parens4(n, partial + "(", open_count + 1, close_count)
  if close_count < open_count:
    parens += parens4(n, partial + ")", open_count, close_count + 1)
  #print(parens)
  return parens
  #ボトムアップかな？

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



