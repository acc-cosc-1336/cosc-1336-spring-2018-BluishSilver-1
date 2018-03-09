import unittest
from src.midterm.practice import get_km_per_hour, get_shipping_charge, get_total_of_numbers_squared

class Test_Practice(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(1,1)

    def test_get_km_per_hour(self):
        self.assertEqual(32, get_km_per_hour(20, 60))


    def test_get_shipping_charge(self):
        self.assertEqual(2.5, get_shipping_charge(2))


    def test_get_total_of_numbers_squared(num):
        self.assertEqual(5, get_total_of_numbers_squared(30))


    def test_get_quiz_list(self):
        self.assertEqual(listarg, get_quiz_list(['sue', 'grace'])


unittest.main(verbosity=2)
