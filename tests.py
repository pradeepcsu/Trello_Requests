"""Positive and negative unit test cases."""
import pathlib
import unittest
from main import TrelloRequests  # pylint: disable=wrong-import-position

REPO_ROOT = pathlib.Path(__file__).parent


class TrelloTestCases(unittest.TestCase):
    """
    Unit Test Cases for testing word process
    """

    def test_add_board(self):
        """Verify adding a board"""
        ## given
        # word = 'myword'
        # requestCheck = TrelloRequests()

        ## exercise
        # requestCheck.process_word(word)

        ## verify
        # self.assertEqual(len(requestCheck.words), 1)
        # self.assertEqual(requestCheck.words[0], 'myword')
        # self.assertEqual(requestCheck.word_length, 6)

    def test_add_card(self):
        """Verify adding a card"""
        ## given
        # word = '12345'
        # requestCheck = TrelloRequests()

        ## exercise
        # requestCheck.process_word(word)

        ## verify
        # self.assertEqual(len(requestCheck.words), 1)
        # self.assertEqual(requestCheck.words[0], '12345')
        # self.assertEqual(requestCheck.word_length, 5)


if __name__ == '__main__':
    unittest.main()
