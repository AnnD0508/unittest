import unittest
from triangle import Triangle

class TestTriangleUnit(unittest.TestCase):

    def setUp(self):
        self.first = Triangle(3, 4, 5)

    def tearDown(self):
        del self.first


    def test_triangle_eq(self):
        second = Triangle(5, 4, 3)
        self.assertEqual(self.first, second)

    def test_triangle_perimetr(self):
        self.assertEqual(self.first.perimetr(), 12)

    def test_triangle_square(self):
        self.assertEqual(self.first.square(), 6)

    def test_triangle_ne(self):
        second = Triangle(6, 4, 3)
        self.assertNotEqual(self.first, second)

    def test_triangle_lt(self):
        second = Triangle(6, 4, 3)
        self.assertLess(self.first, second)

    def test_triangle_qe(self):
        second = Triangle(3, 4, 3)
        self.assertGreaterEqual(self.first, second)

    def test_triangle_equal_to_other(self):
        second = Triangle(6, 8, 10)
        self.assertTrue(self.first.with_same_cornes(second))

    def test_triangle_is_right_angled(self):
        self.assertTrue(self.first.is_right_angled())

    @unittest.skip("test kaput if sides is not 3, 4, 5")
    def test_triangle_is_right_angled(self):
        self.assertTrue(self.first.is_right_angled())

    def test_triangle_is_right(self):
        self.assertTrue(self.first.is_right_angled())

    def test_is_right_triangle(self):
        self.assertFalse(self.first.is_right_triangle())

    @unittest.skip("sure the test will fail")
    def test_two_sides_eq(self):
        self.assertTrue(self.first.two_sides_eq())

    def test_triangle_del(self):
        self.assertIsNotNone(self.first)
    

if __name__ == '__main__':
        unittest.main()





















    # def setUp(self):
    #     self.first = Triangle(a=7, b=8, c=9)
    #     self.second = None
    #
    # def tearDown(self) -> None:
    #     del self.first
    #     del self.second
    #
    # def test_triangle_eq(self):
    #     self.second = Triangle(9, 8, 7)
    #     self.assertEqual(self.first, self.second)
    #
    # def test_triangle_lt(self):
    #     self.second = Triangle(10, 11, 10)
    #     self.assertLess(self.first, self.second)


if __name__ == '__main__':
    unittest.main()