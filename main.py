from blackjack_game import *
from data_and_processes import *

DEBUG_FLAG = True

def main():
    if DEBUG_FLAG:
        bj = deck(blackjack_card, False)
        reg = deck(card, False)

        print(bj, reg)

    
        

if __name__ == "__main__":
    main()