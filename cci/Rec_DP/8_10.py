
def paint_fill(image, c, r, color):
    if c < 0 or r < 0 or len(image) <= r or len(image[r]) <= c:
        return
    old_color = image[r][c]
    if old_color == color:
        return
    paint_fill_color(image, c, r, color, old_color)

def paint_fill_color(image, c, r, new_color, old_color):
    if image[r][c] != old_color:
        return 
    image[r][c] = new_color
    if r > 0:
        paint_fill_color(image, c, r-1, new_color, old_color)
    if r < len(image) - 1:
        paint_fill_color(image, c, r+1, new_color, old_color)
    if c > 0:
        paint_fill_color(image, c-1, r, new_color, old_color)
    if c < len(image[r]) - 1:
        paint_fill_color(image, c+1, r, new_color, old_color)





import unittest

class Test(unittest.TestCase):
  def test_paint_fill(self):
    image1 = [[10, 10, 10, 10, 10, 10, 10, 40],
              [30, 20, 20, 10, 10, 40, 40, 40],
              [10, 10, 20, 20, 10, 10, 10, 10],
              [10, 10, 30, 20, 20, 20, 20, 10],
              [40, 40, 10, 10, 10, 10, 10, 10]]
    image2 = [[30, 30, 30, 30, 30, 30, 30, 40],
              [30, 20, 20, 30, 30, 40, 40, 40],
              [10, 10, 20, 20, 30, 30, 30, 30],
              [10, 10, 30, 20, 20, 20, 20, 30],
              [40, 40, 30, 30, 30, 30, 30, 30]]
    image3 = [[30, 30, 30, 30, 30, 30, 30, 40],
              [30, 20, 20, 30, 30, 40, 40, 40],
              [30, 30, 20, 20, 30, 30, 30, 30],
              [30, 30, 30, 20, 20, 20, 20, 30],
              [40, 40, 30, 30, 30, 30, 30, 30]]
    paint_fill(image1, 3, 1, 30)
    self.assertEqual(image1, image2)
    paint_fill(image1, 3, 1, 10)
    paint_fill(image1, 3, 1, 30)
    self.assertEqual(image1, image3)

if __name__ == "__main__":
  unittest.main()

