import unittest
from unittest.mock import patch
import random
from sourse.computer import computer_pon

class TestComputerPon(unittest.TestCase):
    @patch('random.choice')
    def test_computer_pon(self, mock_choice):
        mock_choice.return_value = "グー"
        result = computer_pon()
        self.assertEqual(result, "グー")
    
    @patch('random.choice')
    def test_c_pon_Caesar(self, mock_choice):
        mock_choice.return_value = "チョキ"
        result = computer_pon()
        self.assertEqual(result, "チョキ")
        
    @patch('random.choice')
    def test_c_pon_paper(self, mock_choice):
        mock_choice.return_value = "パー"
        result = computer_pon()
        self.assertEqual(result, "パー")

if __name__ == '__main__':
    unittest.main()
