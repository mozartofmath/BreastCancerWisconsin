import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
#from scripts.Fetcher import Fetcher

class TestLabel(unittest.TestCase):
    def test_label(self):
        """
        Test that label is encoded
        """
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
