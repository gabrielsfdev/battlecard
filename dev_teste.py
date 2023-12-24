import random
default_deck = {
    'Carta2': {'nome': 'Robô de Aço', 'ataque': 85, 'defesa': 75, 'super_trunfo': False},
    'Carta5': {'nome': 'Fênix Ressurgente', 'ataque': 89, 'defesa': 79, 'super_trunfo': False},
    'Carta1': {'nome': 'Dragão Flamejante', 'ataque': 90, 'defesa': 80, 'super_trunfo': False},
    'Carta3': {'nome': 'Nave Espacial', 'ataque': 88, 'defesa': 78, 'super_trunfo': False},
    'Carta4': {'nome': 'Monstro do Abismo', 'ataque': 92, 'defesa': 82, 'super_trunfo': False},
    
    # 'Carta6': {'nome': 'Máquina do Tempo', 'ataque': 86, 'defesa': 76, 'super_trunfo': False},
    # 'Carta7': {'nome': 'Alumni', 'ataque': 99, 'defesa': 99, 'super_trunfo': False},
    # 'Carta8': {'nome': 'Trovão Divino', 'ataque': 87, 'defesa': 77, 'super_trunfo': False},
    # 'Carta9': {'nome': 'Muralha Intransponível', 'ataque': 91, 'defesa': 81, 'super_trunfo': False},
    # 'Carta10': {'nome': 'Vortex Cósmico', 'ataque': 93, 'defesa': 83, 'super_trunfo': False},
    # 'Carta11': {'nome': 'Lobisomem Lunar', 'ataque': 84, 'defesa': 74, 'super_trunfo': False},
    # 'Carta12': {'nome': 'Sirene Encantadora', 'ataque': 82, 'defesa': 92, 'super_trunfo': False},
    # 'Carta13': {'nome': 'Terremoto Devastador', 'ataque': 96, 'defesa': 94, 'super_trunfo': False},
    # 'Carta14': {'nome': 'Cavaleiro da Justiça', 'ataque': 88, 'defesa': 78, 'super_trunfo': False},
    # 'Carta15': {'nome': 'Fada Protetora', 'ataque': 81, 'defesa': 91, 'super_trunfo': False},
    # 'Carta16': {'nome': 'Ninja Sombrio', 'ataque': 94, 'defesa': 84, 'super_trunfo': False},
    # 'Carta17': {'nome': 'Foguete Intergaláctico', 'ataque': 92, 'defesa': 85, 'super_trunfo': False},
    # 'Carta18': {'nome': 'Pirata dos Sete Mares', 'ataque': 83, 'defesa': 93, 'super_trunfo': False},
    # 'Carta19': {'nome': 'Kenji', 'ataque': 00, 'defesa': 00, 'super_trunfo': True},
    # 'Carta20': {'nome': 'Marcotti', 'ataque': 00, 'defesa': 00, 'super_trunfo': True},
}
# ind = 0
# while ind < 50:
#     print(random.randrange(1, 20))
#     ind += 1
'''
class Teste:
    def __init__(self, deck={}) -> None:
        self.deck = deck

    def add_deck(self):
        num = random.randrange(0, (len(default_deck)))
        (self.deck)[f"Carta{num}"] = default_deck.pop(f"Carta{num}")

jogador = Teste()
jogador.add_deck()
jogador.add_deck()
jogador.add_deck()

print(jogador.deck)
print("DECK COMPLETO\n", default_deck)
'''
teste = "Carta_16"
print(int(teste[6:]))
# print( dict(sorted(default_deck.items())) )

# como acessar um dict de dict por index ? por exemplo:
# exemplo = { dict1:{item1: 1, item2: 2}, dict2:{item1: 1, item2: 2}, dict3:{item1: 1, item2: 2} }
# queria obter dict2:{item1: 1, item2: 2} com algo parecido com exemplo[1]