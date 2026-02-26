# test_datavibe.py
"""
Tests for DataVibe module.
"""

import unittest
from datavibe import DataVibe

class TestDataVibe(unittest.TestCase):
    """Test cases for DataVibe class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataVibe()
        self.assertIsInstance(instance, DataVibe)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataVibe()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
