import unittest

def powerset(nums, taken=None):
    if taken is None:
        taken = []

    if len(nums) == 0:
        return taken if len(taken) > 0 else [[]]

    take = powerset(nums[1:], [taken + [nums[0]]] if len(taken) == 0 else [taken[0] + [nums[0]]])
    nottake = powerset(nums[1:], taken)

    return nottake + take


class TestPowerSet(unittest.TestCase):

    def test_powerset_two_elements(self):
        self.assertEqual(
            powerset([1, 2]),
            [
                [],
                [2],
                [1],
                [1, 2]
            ]
        )

    def test_powerset_three_elements(self):
        self.assertEqual(
            powerset([1, 2, 3]),
            [
                [],
                [3],
                [2],
                [2, 3],
                [1],
                [1, 3],
                [1, 2],
                [1, 2, 3]
            ]
        )

    def test_powerset_single_element(self):
        self.assertEqual(
            powerset([1]),
            [
                [],
                [1]
            ]
        )

    def test_powerset_multiple_elements(self):
        self.assertEqual(
            powerset([125, 15, 155, 15, 158]),
            [
                [],
                [158],
                [15],
                [15, 158],
                [155],
                [155, 158],
                [155, 15],
                [155, 15, 158],
                [15],
                [15, 158],
                [15, 15],
                [15, 15, 158],
                [15, 155],
                [15, 155, 158],
                [15, 155, 15],
                [15, 155, 15, 158],
                [125],
                [125, 158],
                [125, 15],
                [125, 15, 158],
                [125, 155],
                [125, 155, 158],
                [125, 155, 15],
                [125, 155, 15, 158],
                [125, 15],
                [125, 15, 158],
                [125, 15, 15],
                [125, 15, 15, 158],
                [125, 15, 155],
                [125, 15, 155, 158],
                [125, 15, 155, 15],
                [125, 15, 155, 15, 158]
            ]
        )

    def test_powerset_four_elements(self):
        self.assertEqual(
            powerset([1, 2, 3, 4]),
            [
                [],
                [4],
                [3],
                [3, 4],
                [2],
                [2, 4],
                [2, 3],
                [2, 3, 4],
                [1],
                [1, 4],
                [1, 3],
                [1, 3, 4],
                [1, 2],
                [1, 2, 4],
                [1, 2, 3],
                [1, 2, 3, 4]
            ]
        )



if __name__ == "__main__":
    unittest.main()
