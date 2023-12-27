import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from data.cartas_exemplo import custom_deck_p1
import random

class Player:
    def __init__(self, name='', hp=500, hand={}, deck=custom_deck_p1) -> None:
        self.name = name
        self.hp = hp
        self.hand = hand
        self.deck = deck.copy()
        self.deck_to_hand = list(self.deck.items())
        self.round = 1
        self.cards_in_hand()

    def cards_in_hand(self):
        deck = self.deck #Apenas para maior legibilidade do código, não necessário
        hand = self.hand
        index = 1
        if len(hand) == 0:
            deck_to_hand = self.deck_to_hand
            while index <= 5:
                random_num = random.randrange(0, len(deck_to_hand))
                if deck_to_hand[random_num][1]["super_card"] == True: continue
                hand[f"Carta_{index}"] = deck_to_hand[random_num][1]
                deck.pop(deck_to_hand[random_num][0])
                deck_to_hand.pop(random_num)
                index += 1
    
    def take_card_to_deck(self, num_cards):
        if len(self.deck_to_hand) > 0:
            index = 0
            index_card = 1
            deck_to_hand = self.deck_to_hand
            while index_card <= 5:
                if f"Carta_{index_card}" not in self.hand:
                    break
                index_card += 1
            while index < num_cards:
                    random_num = random.randrange(0, len(deck_to_hand))
                    if self.round < 3 and deck_to_hand[random_num][1]["super_card"] == True: continue
                    self.hand[f"Carta_{index_card}"] = deck_to_hand[random_num][1]
                    self.deck.pop(deck_to_hand[random_num][0])
                    deck_to_hand.pop(random_num)
                    index += 1
            index_card = 1
            self.round += 1

    def view_hand(self):
        index = 1
        for x, y in self.hand.items():
            print(f"{x[6:]} - "
            f"Nome: {y['nome']},"
            f" ataque: {y['ataque']},"
            f" defesa: {y['defesa']},"
            f" supercard?: {'Sim' if y['super_card'] == True else 'Não'}")
            index += 1
    
    def attack(self, target_player, card_index_p1, defense_card, card_index_p2):
        attack_card = self.hand[f"Carta_{card_index_p1}"]

        if attack_card["ataque"] > defense_card["defesa"]:
            print("Ataque venceu esta rodada.")
            target_player.hp -= attack_card["ataque"]
        elif defense_card["defesa"] > attack_card["ataque"]:
            print("Defesa ganhou nessa rodada.")
        else:
            print("Houve um empate.")

        self.hand.pop(f"Carta_{card_index_p1}")
        target_player.hand.pop(f"Carta_{card_index_p2}")
        self.take_card_to_deck(1)
        target_player.take_card_to_deck(1)

if __name__ == "__main__":
    pass
