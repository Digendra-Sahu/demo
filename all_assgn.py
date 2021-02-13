from assign_1pyth import *
from assign_2pyth import *
from assign_3pyth import *

import pytest

from feb10 import *
import unittest


class case_check(unittest.TestCase):
    def test_vol(self):
        self.assertEqual(27, vol(3))
        self.assertEqual(125, vol(5))
        self.assertEqual(216, vol(6))
        
print(prime_all(2,99))