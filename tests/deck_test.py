import unittest
import pycard


class TestDeck(unittest.TestCase):
    def test_deck_len(self):
        deck = pycard.Deck()
        deck_length = 52*2

        self.assertEqual(deck_length, len(deck.get_cards()))

    def test_draw_card(self):
        deck = pycard.Deck(num_decks=1)
        drawn_card = deck.draw_card()

        self.assertIsInstance(drawn_card, pycard.Card)
        self.assertNotIn(drawn_card, deck.get_cards())

    def test_deal_cards(self):
        deck = pycard.Deck()
        player1 = pycard.Player(name="Player 1")
        player2 = pycard.Player(name="Player 2")
        players = [player1, player2]

        deck.deal_cards(num_cards=2, players=players)

        for player in players:
            self.assertEqual(len(player.get_hand()), 2)

        remaining_cards = deck.get_cards()
        expected_remaining = len(deck.get_cards()) - (len(players) * 2)
        self.assertEqual(len(remaining_cards), expected_remaining)

    def test_invalid_create_deck(self):
        with self.assertRaises(ValueError):
            pycard.Deck(num_decks=-1)

    def test_invalid_draw_card(self):
        deck = pycard.Deck()
        for _ in range(len(deck.get_cards())):
            deck.draw_card()
        with self.assertRaises(IndexError):
            deck.draw_card()


if __name__ == '__main__':
    unittest.main()
