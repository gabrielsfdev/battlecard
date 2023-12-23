import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from data.cartas_exemplo import custom_deck
class Carta:
    def __init__(self, nome, atk, defe, supertrunfo=False) -> None:
        self.nome = nome
        self.atk = atk
        self.defe = defe
        self.super_trunfo = supertrunfo

    def add_carta(self):
        custom_deck[f"Carta_{len(custom_deck) + 1}"] = {
                                                        "nome": self.nome, 
                                                        "ataque": self.atk, 
                                                        "defesa": self.defe, 
                                                        "super_trunfo": self.super_trunfo
                                                        }

    def ver_baralho(self):
        return custom_deck

    def atacar():
        pass

    def defender():
        pass

if __name__ == "__main__":
    carta1 = Carta("Teste", 25, 52)
    carta1.add_carta()
    print(carta1.ver_baralho())
