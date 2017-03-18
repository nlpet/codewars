"""
Poker Hand Ranking

Gives a winner between two hands and calculates probability for each
hand to make a winning hand

WIP
"""
from collections import Counter
import re


def PokerHandsRanker(object):
    def __init__(self):
        self.deck = [
            'A', '2', '3', '4', '5', '6', '7', '8', '9',
            '10', 'J', 'Q', 'K', 'A']
        self.suits = {'h', 'c', 'd', 's'}

    def parse_hand(hand):
        hand = re.findall(r'(\d{1,2}|[JQKA])([hcds])', hand)
        if len(hand) != 5:
            raise Exception('Invalid poker hand, e.g 2h 5d Jd Qh As')
        return zip(*hand)

    def rank_hand(cards, suits):
        cards_counter = Counter(cards)
        suits_counter = Counter(suits)
        suits_most_common = suits_counter.most_common(1)[0][1]
        cards_most_common = cards_counter.most_common(1)[0][1]

        if suits_most_common == 1:
            pass  # no flush
        elif cards_most_common == 5:
            pass  # flush
