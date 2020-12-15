from unittest import TestCase

from main import solution


class Test(TestCase):
    def test_solution_part_1(self):
        self.assertEqual(solution("testData.txt", 2020), 436)

    def test_solution_part_2(self):
        self.assertEqual(solution("testData.txt", 30000000), 18929178)
