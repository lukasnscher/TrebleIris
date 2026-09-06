# test_trebleiris.py
"""
Tests for TrebleIris module.
"""

import unittest
from trebleiris import TrebleIris

class TestTrebleIris(unittest.TestCase):
    """Test cases for TrebleIris class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TrebleIris()
        self.assertIsInstance(instance, TrebleIris)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TrebleIris()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
