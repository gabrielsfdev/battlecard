import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from data.cartas_exemplo import custom_deck_p1, custom_deck_p2
class Card:
    def __init__(self, name, atk, defense, deck, supertrunfo=False) -> None:
        self.name = name
        self.atk = atk
        self.defense = defense
        self.super_trunfo = supertrunfo
        self.index_name = ""
        self.deck = deck
        self.add_card()
    
    def add_card(self):
        self.index_name = f"Carta_{len(self.deck)}"
        self.deck[self.index_name] = {
                                                        "nome": self.name, 
                                                        "ataque": self.atk, 
                                                        "defesa": self.defense, 
                                                        "super_trunfo": self.super_trunfo
                                                        }
        

    def atack():
        pass

    def defend():
        pass

if __name__ == "__main__":
    pass
