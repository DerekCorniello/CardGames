from data_and_processes import *

class bj_hand(hand):
    def __init__(self) -> None:
        super().__init__()


class bj_table(table):
    def __init__(self) -> None:
        super().__init__()
        self.deck = deck(blackjack_card)

def run():
    pass