import unittest

import pycard


class TestCard(unittest.TestCase):
    def test_card_creation(self):
        card = pycard.Card("Ace", "Hearts")
        self.assertEqual(card.get_value(), "Ace")
        self.assertEqual(card.get_suit(), "Hearts")

    def test_card_string_representation(self):
        card = pycard.Card("King", "Spades")
        self.assertEqual(str(card), "King of Spades")

    def test_card_string_equality(self):
        card1 = pycard.Card("Ace", "Spades")
        card2 = pycard.Card("Ace", "Spades")
        card3 = pycard.Card("King", "Hearts")

        self.assertEqual(str(card1), str(card2))
        self.assertNotEqual(str(card1), str(card3))

    def test_card_value_equality(self):
        card1 = pycard.Card("8", "Hearts")
        card2 = pycard.Card("8", "Spades")
        card3 = pycard.Card("3", "Hearts")

        self.assertEqual(card1.get_value(), card2.get_value())
        self.assertNotEqual(card1.get_value(), card3.get_value())

    def test_card_suit_equality(self):
        card1 = pycard.Card("King", "Clubs")
        card2 = pycard.Card("4", "Clubs")
        card3 = pycard.Card("King", "Spades")

        self.assertEqual(card1.get_suit(), card2.get_suit())
        self.assertNotEqual(card1.get_suit(), card3.get_suit())


if __name__ == '__main__':
    unittest.main()
