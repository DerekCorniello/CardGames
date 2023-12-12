from enum import Enum
from random import randint

# A card dictionary to convert values to string versions of their value
card_dict = {
                "A" : "Ace",
                "K" : "King",
                "Q" : "Queen",
                "J" : "Jack",
                1 : "One",
                2 : "Two",
                3 : "Three",
                4 : "Four",
                5 : "Five",
                6 : "Six",
                7 : "Seven",
                8 : "Eight",
                9 : "Nine",
                10 : "Ten"
            }

# An enumaerable for use in comparing standard card types
class standard_suits(Enum):
        Spade = "spades"
        Club = "clubs"
        Heart = "hearts"
        Diamond ="diamonds"

# The card super class. The card class is a 'standard card' which can be edited in subclasses for each game's usage. 
class card():

    # constructor
    # Inputs: a card's suit, face value, and bool for if a card should be printed with numerals
    def __init__(self, suit : standard_suits, faceval: any, use_num : bool = False) -> None:

        self.suit = suit.value
        self.faceval = faceval
        self.use_num = use_num
        
        # ensure that the face value is a legal value

        if isinstance(faceval, int):
            if faceval not in (list(range(2,11))):
                raise ValueError(f"Error in card value when initializing value '{faceval}' in card. Integer not between 2 and 10")

        elif isinstance(faceval, str):
            if faceval not in ['A', 'J', 'Q', 'K']:
                raise ValueError(f"Error in card value when initializing value '{faceval}' in card. String not in A, J, Q, K")
        else:
            raise ValueError(f"Error in card value when initializing value '{faceval}' in card. Invalid type.")

    def __str__(self) -> str:
        if self.use_num:
            return str(self.faceval)+ " of " + str(self.suit)
        return str(card_dict.get(self.faceval)) + " of " + str(self.suit)

# A card subclass that is used for the game blakjack
class blackjack_card(card):

    def __init__(self, suit : str, value : any, use_num : bool) -> None:

        # Change value based on what the face value is of a card

        if isinstance(value, int):
            if 2 <= value <= 10:
                self.play_val = value
                self.faceval = value

        elif isinstance(value, str):
            if value in ['J', 'Q', 'K']:
                self.play_val = 10
                self.faceval = str(value)

            elif value == "A":
                self.play_val = (1,11)
                self.faceval = str(value)
        else:
            raise ValueError(f"Error in card value when initializing value '{value}' in blackjack card. Type: {type(value)}, type should be {type(int())} or {type(str())}.")

        super().__init__(suit, self.faceval, use_num)
    
    def __str__(self) -> str:
        # Since Ace can be 1/11, handle special case
        if self.play_val == (1,11):
            return super().__str__() +  ", Value: 1 or 11"
        return super().__str__() + ", Value: " + str(self.play_val)

# A collection of cards. Can contain as many or as few as the game requires.
class deck():

    def __init__(self, card_type: any, use_num : bool):

        # Start with an empty deck
        self.cards = []
        self.card_type = card_type
        self.use_num = use_num
        self.restore_deck()

    def __len__(self):
        return len(self.cards)
    
    # Add cards to the deck in order
    def restore_deck(self):

        # Change the amount of cards in a deck
        self.num_decks = 1
        if self.card_type == blackjack_card:
            self.num_decks = 8

        for i in range(self.num_decks):
            # For all four suits...
            for i in range(4):
                t = None
                match i:
                    case 0:
                        t = standard_suits.Spade
                    case 1:
                        t = standard_suits.Club
                    case 2:
                        t = standard_suits.Diamond
                    case 3:
                        t = standard_suits.Heart
                
                # ...create 13 of each value...

                for j in range(1, 14):
                    v = None
                    match j: 
                        case 1:
                            v = 'A'
                        case 11:
                            v = 'J'
                        case 12:
                            v = 'Q'
                        case 13:
                            v = 'K'
                        case _:
                            v = j
                    # ... and append it to deck
                    try: 
                        self.cards.append(self.card_type(t, v, self.use_num))
                    
                    except Exception as e:
                        print(f"An error occurred when adding card to deck: {e}")
    
    # since __str__ must return a string type, print each card individually
    def __str__(self) -> str:
        for i in self.cards:
            print(i)
        return ""
    
    # Because cards are ordered, just drawing a random card from the deck and delete it from
    # the deck will act as "drawing a card"
    def draw(self) -> card:
        if len(self.cards) == 0:
            self.restore_deck()
        return self.cards.pop(randint(0,len(self.cards)-1))

def main():
    bj = deck(blackjack_card, False)
    reg = deck(card, False)
    #print(reg)
    #print(bj)
    print(len(bj))
    print(len(reg))

if __name__ == "__main__":
    main()