import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

class Card:
    def __init__(self, name, atk, defense, deck, supercard=False) -> None:
        self.name = name
        self.atk = atk
        self.defense = defense
        self.super_card = supercard
        self.index_name = ""
        self.deck = deck
        self.add_card()
    
    def add_card(self):
        self.index_name = f"Carta_{len(self.deck)}"
        self.deck[self.index_name] = {
                                    "nome": self.name, 
                                    "ataque": self.atk, 
                                    "defesa": self.defense, 
                                    "super_card": self.super_card
                                    }
        

    def atack():
        pass

    def defend():
        pass

if __name__ == "__main__":
    pass
