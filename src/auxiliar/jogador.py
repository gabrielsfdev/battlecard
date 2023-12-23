import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from data.cartas_exemplo import custom_deck

import random

class Player:
    def __init__(self, hp=1000, hand={}, deck=custom_deck) -> None:
        self.hp = hp
        self.hand = hand
        self.deck = deck.copy()

    def cards_in_hand(self):
        deck = self.deck #Apenas para maior legibilidade do código, não necessário
        hand = self.hand
        index = 1
        if len(hand) == 0:
            deck_to_hand = list(deck.items())
            while index <= 5:
                random_num = random.randrange(0, len(deck_to_hand))
                hand[f"Carta_{index}"] = deck_to_hand[random_num][1]
                
                deck.pop(deck_to_hand[random_num][0])
                deck_to_hand.pop(random_num)
                # hand.append(deck[random_num])
                index += 1

    def hp_decrease():
        pass

if __name__ == "__main__":
    from cartas import Carta
    carta1 = Carta("Carta1", 25, 52)
    carta1.add_carta()
    carta2 = Carta("Carta2", 225, 522)
    carta2.add_carta()
    carta3 = Carta("Carta3", 225, 522)
    carta3.add_carta()
    carta4 = Carta("Carta4", 225, 522)
    carta4.add_carta()
    carta5 = Carta("Carta5", 225, 522)
    carta5.add_carta()
    jogador1 = Player(deck=custom_deck)
    jogador1.cards_in_hand()
    print(jogador1.hand)


