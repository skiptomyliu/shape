

import unittest
from grid import Grid

import profile
import cProfile


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid("/Users/dean/Desktop/og/bo_lr.jpg", pix_multi=.016, diamond=True, colorful=True)
       
    def tearDown(self):
        pass

    def test_n_pass(self):
        n=1
        self.grid.n_pass(n)
        self.grid.save("./out.JPEG")

    # def test_occupy(self):
    #     x,y = (10,10)
    #     self.grid.occupy(x,y)
    #     result = self.grid.is_occupied(x,y)
    #     self.assertTrue(result)

    # # Test vertical expansion
    # def test_is_occupied(self):
    #     x,y = (10,10)
    #     result = self.grid.is_occupied(x,y)
    #     self.assertFalse(result)
    #     self.grid.occupy(x,y)
    #     result = self.grid.is_occupied(x,y)
    #     self.assertTrue(result)


if __name__ == '__main__':
    cProfile.run("unittest.main()", 'test.profile')
    # unittest.main()
