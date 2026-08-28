# test_cresturn.py
"""
Tests for CrestUrn module.
"""

import unittest
from cresturn import CrestUrn

class TestCrestUrn(unittest.TestCase):
    """Test cases for CrestUrn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CrestUrn()
        self.assertIsInstance(instance, CrestUrn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CrestUrn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
