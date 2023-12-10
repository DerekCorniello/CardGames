from enum import Enum

class suits(Enum):
    Spade = "Spades"
    Diamond = "Diamonds"
    Club = "Clubs"
    Heart = "Hearts"


class card():

    def __init__(self, suit : suits, faceval: any) -> None:

        self.suit = suit
        self.faceval = faceval
        
        if isinstance(faceval, int):
            if faceval not in (list(range(2,11))):
                raise ValueError(f"Error in card value when initializing value '{faceval}' in card. Integer not between 2 and 10")

        elif isinstance(faceval, str):
            if faceval not in ['A', 'J', 'Q', 'K']:
                raise ValueError(f"Error in card value when initializing value '{faceval}' in card. String not in A, J, Q, K")
        else:
            raise ValueError(f"Error in card value when initializing value '{faceval}' in card. Invalid type.")



    def __str__(self) -> str:
        return str(self.faceval) + " of " + str(self.suit)

class blackjack_card(card):

    def __init__(self, suit : str, value : any) -> None:

        try:
            if 2 <= value <= 10:
                self.play_val = value
                self.faceval = value
        except:

            try:

                if value in ['J', 'Q', 'K']:
                    self.play_val = 10
                    self.faceval = str(value)

                elif value == "A":
                    self.play_val = (1,11)
                    self.faceval = str(value)
    
            except:
                raise ValueError(f"Error in card value when initializing value '{value}' in card.")

        super().__init__(suit, self.faceval)
    
    def __str__(self) -> str:
        if self.play_val == (1,11):
            return str(self.faceval) + " of " + str(self.suit) + ", Value: 1 or 11"
        return str(self.faceval) + " of " + str(self.suit) + ", Value: " + str(self.play_val)

class deck():

    def __init__(self, card_type: any):

        self.cards = []
        for i in range(4):
            t = None
            match i:
                case 0:
                    t = suits.Spade
                case 1:
                    t = suits.Club
                case 2:
                    t = suits.Diamond
                case 3:
                    t = suits.Heart
            
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
                try: 
                    self.cards.append(card_type(t.value, v))
                
                except Exception as e:
                    print(f"An error occurred when adding card to deck: {e}")


 
    def __str__(self) -> str:
        for i in self.cards:
            print(i)
        return ""

def main():
    normal_deck = deck(card)
    bj_deck = deck(blackjack_card)
    
    print(normal_deck)
    print('\n\n\n\n\n\n')
    print(bj_deck)

if __name__ == "__main__":
    main()