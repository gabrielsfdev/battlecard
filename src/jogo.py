from auxiliar.cartas import Card
from auxiliar.jogador import Player
from data.cartas_exemplo import custom_deck_p1, custom_deck_p2, default_deck
import os
import time #Apenas para ficar mais interessante para o usuário

# Adicionando as cartas personalizadas ao novo baralho personalizado
def deck_create(deck):
    nome = input("Adicione o nome da carta: ")
    atk = int(input("Adicione o valor de atk da carta: "))
    defesa = int(input("Adicione o ponto de defesa: "))
    supertrunfo = input("É uma carta supertrunfo ? ")
    supertrunfo = True if supertrunfo.lower() == "sim" else False
    return Card(nome, atk, defesa, deck, supertrunfo)

def match(deck=custom_deck_p1, deck2=custom_deck_p2):
    os.system('cls' if os.name == 'nt' else 'clear') #Limpa o terminal
    deck_player1 = [] #Salvando o deck para uma possivel feature de editar dados
    deck_player2 = []
    index = 1
    print("Bem vindo(a) ao grande BattleCard.")
    
    if deck == custom_deck_p1:
        print("Primeiro, adicione as cartas que irão jogar.")
        time.sleep(1.5)
        # deck_player1 = [deck_create(deck) for _ in range(10)]
        # deck_player2 = [deck_create(deck2) for _ in range(10)]
        while len(deck_player1) < 10 and len(deck_player2) < 10: #Confecção do deck
            os.system('cls' if os.name == 'nt' else 'clear') #Limpa o terminal/adição
            print(f"Adicione a carta {index}/10 para o Player1")
            card1 = deck_create(deck)
            deck_player1.append(card1)
            print(f"Adicione a carta {index}/10 para o Player2")
            card2 = deck_create(deck2)
            deck_player2.append(card2)
            index += 1
        player1 = Player(hand={}, deck=deck)
        [deck_player1.append(card) for card in (player1.hand).values()]
        player2 = Player(hand={}, deck=deck2)
        [deck_player2.append(card) for card in (player2.hand).values()]
        print("Ótimo, cartas adicionadas. Vamos entrar na partida.")
    else:
        player2 = Player(hand={}, deck=deck)
        [deck_player1.append(card) for card in (player2.hand).values()]
        player1 = Player(hand={}, deck=deck)
        [deck_player2.append(card) for card in (player1.hand).values()]
    print("Vamos começar com o Player1")
    time.sleep(1.5) #Apenas para efeitos visuais.
    who_plays = 1
    
    while player2.hp > 0 and player1.hp > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        if who_plays == 1:
            player1.view_hand()
            choose_p1 = int(input("Vez de Player1. Escolha o índice da carta com que deseja atacar: "))
            player2.view_hand()
            choose_p2 = int(input("Escolha o índice da carta com que deseja defender: "))
            defense_card = player2.hand[f"Carta_{choose_p2}"]
            player1.attack(player2, choose_p1, defense_card, choose_p2)
            player1.hand = dict(sorted(player1.hand.items()))
            player2.hand = dict(sorted(player2.hand.items()))
        else:
            player2.view_hand()
            choose_p2 = int(input("Vez de Player2. Escolha o índice da carta com que deseja atacar: "))
            player1.view_hand()
            choose_p1 = int(input("Escolha o índice da carta com que deseja defender: "))
            defense_card = player1.hand[f"Carta_{choose_p1}"]
            player2.attack(player1, choose_p2, defense_card, choose_p1)
            player1.hand = dict(sorted(player1.hand.items()))
            player2.hand = dict(sorted(player2.hand.items()))

        who_plays = 3 - who_plays

        time.sleep(1.5)
        print("Próxima rodada...")
        time.sleep(1)





if __name__ == "__main__":   
    print(match(deck=custom_deck_p1))
