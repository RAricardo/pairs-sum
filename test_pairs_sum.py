import unittest
from pairs_sum import pairs_sum

class TestPairsSum(unittest.TestCase):
    def test_basic_case(self):
        array = [2, 4, 3, 1, 0, 5, 7, 6]
        target_sum = 6
        result = pairs_sum(array, target_sum)
        expected = [[4, 2], [5, 1], [6, 0]]
        self.assertEqual(result, expected)

    def test_empty_array(self):
        array = []
        target_sum = 5
        result = pairs_sum(array, target_sum)
        expected = []
        self.assertEqual(result, expected)

    def test_no_pairs(self):
        array = [1, 2, 3, 4, 5]
        target_sum = 10
        result = pairs_sum(array, target_sum)
        expected = []
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        array = [-1, -2, 3, 4, 5, -4]
        target_sum = 0
        result = pairs_sum(array, target_sum)
        expected = [[-4, 4]]
        self.assertEqual(result, expected)

    def test_single_element_array(self):
        array = [5]
        target_sum = 5
        result = pairs_sum(array, target_sum)
        expected = []
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        array = [1000, 2000, 3000, 4000, 6000, -1000]
        target_sum = 5000
        result = pairs_sum(array, target_sum)
        expected = [[3000,2000],[4000, 1000],[-1000,6000]]
        self.assertEqual(result, expected)

    def test_negative_target_sum(self):
        array = [1, 2, 3, 4, 5, -2, -6]
        target_sum = -1
        result = pairs_sum(array, target_sum)
        expected = [[-2,1],[-6,5]]
        self.assertEqual(result, expected)

    def test_target_sum_negative_numbers(self):
        array = [-1, -2, -3, -4, -5]
        target_sum = -3
        result = pairs_sum(array, target_sum)
        expected = [[-2, -1]]
        self.assertEqual(result, expected)

    def test_target_sum_positive_numbers(self):
        array = [1, 2, 3, 4, 5]
        target_sum = 8
        result = pairs_sum(array, target_sum)
        expected = [[5, 3]]
        self.assertEqual(result, expected)

    def test_large_negative_input(self):
        array = list(range(-1000, 0))
        target_sum = -1999
        result = pairs_sum(array, target_sum)
        expected = [[-999, -1000]]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
