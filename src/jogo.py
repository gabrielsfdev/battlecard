# ==================I M P O R T A Ç Õ E S==========================

import random

from data.cartas import Deck_Lucas

from auxiliar.jogador import Player

# =================V A R I A V E I S  U T E I S=====================

menu1 = None
menu2 = None
partida = None
quantidade_jogadores = 2
quantidade_carta = 7
cartas_p1 = []
cartas_p2 = []

# ===================C O D I G O  P R I N C I P A L==================

# Introdução:

print(f"\t    S u p e r  T r u n f o\n\t\tDeck Pokemon\n\
    \t     release Lucas Diego\nSeja Bem-vindo  ao jogo Super Trunfo,\nO super trunfo é um jogo de RPG de cartas\
    \nEssa versão do game é Tematico pokemon, \ncriado por Lucas Diego, para começar o jogo\nprecisamos de algumas informações...")

# Iniciar o jogo?
inicio = input("Deseja iniciar? (Sim ou não): ")
inicio = inicio.lower()

# inserindo a dificuldade / vida de acordo com a dificuldade
if inicio == "sim":
    nivel_dificuldade = input(
        "Insira o nivel de dificuldade (Facil/normal/dificil): ")
    if nivel_dificuldade.lower() == "facil":
        vida = 120
    if nivel_dificuldade.lower() == "normal":
        vida = 100
    if nivel_dificuldade.lower() == "dificil":
        vida = 80

# Inserindo os nomes dos jogadores:
    print("Nessa partida cada jogador irá iniciar com 7 cartas")
    nome_player01 = input("Digite o nome do jogador 01: ")
    nome_player02 = input("Digite o nome do jogador 02: ")

# distribuindo cartas:
    while len(cartas_p1) < 7:
        cartas_p1.append(random.choice(list(Deck_Lucas.keys())))
    while len(cartas_p2) < 7:
        cartas_p2.append(random.choice(list(Deck_Lucas.keys())))

# Definindo o nome, vida, quantidade de cartas e as cartas de cada jogador
    p1 = Player(nome_player01, vida, quantidade_carta, cartas_p1)
    p2 = Player(nome_player02, vida, quantidade_carta, cartas_p2)
    vidap1 = p1.vida
    vidap2 = p2.vida

# Menu de opções do jogo.
    while partida != 404:
        if partida == None:
            partida = 1
        else:
            partida += 1

        print(f"Round {partida}")

        for i in range(1, 3):

            if i == 1:
                nome = p1.nome
                numero_cartas = p1.numero_cartas
                vidap1atual = vidap1
                cartas = p1.cartas

                print(f"Vez do player {nome}")

                while menu1 != 0:
                    print("Menu Player")

                    opcao = input(
                        "Dentre as seguintes opções, decida oque quer fazer:\nListar cartas; Numero de cartas; Visualizar a vida;\njogar; pular partida. Insira a sua ação: ")

                    if opcao.lower() == "listar cartas":
                        print(f"suas cartas são: {cartas_p1}")
                    elif opcao.lower() == "numero de cartas":
                        print(numero_cartas)
                    elif opcao.lower() == "visualizar a vida":
                        print(f"Sua vida no momento é {vidap1atual}")
                    elif opcao.lower() == "jogar":
                        carta_jogada1 = input(
                            "Insira Qual das suas cartas, você deseja jogar: ")
                        menu1 = 0
                    elif opcao.lower() == "pular partida":
                        pulando = input(f"Jogador {nome}, pulou a partida!")
                        menu1 = 0
                carta_player01 = Deck_Lucas[carta_jogada1]

            if i == 2:

                nome = p2.nome
                numero_cartas = p2.numero_cartas
                vidap2atual = vidap2
                cartas = p2.cartas

                print(f"Vez do player {nome}")

                while menu2 != 0:

                    print("Menu Player")

                    opcao = input(
                        "Dentre as seguintes opções, decida oque quer fazer:\nListar cartas; Numero de cartas; Visualizar a vida;\njogar; pular partida. Insira a sua ação: ")

                    if opcao.lower() == "listar cartas":
                        print(f"suas cartas são: {cartas_p2}")
                    elif opcao.lower() == "numero de cartas":
                        print(numero_cartas)
                    elif opcao.lower() == "visualizar a vida":
                        print(f"Sua vida no momento é {vidap2atual}")
                    elif opcao.lower() == "jogar":
                        carta_jogada2 = input(
                            "Insira Qual das suas cartas, você deseja jogar: ")
                        menu2 = 0
                    elif opcao.lower() == "pular partida":
                        pulando = input(f"Jogador {nome}, pulou a partida!")
                        menu2 = 0

                carta_player02 = Deck_Lucas[carta_jogada2]

# logica de combate entre as cartas.
        ataque_player01 = carta_player01.get(
            "ataque") - carta_player02.get("defesa")
        ataque_player02 = carta_player02.get(
            "ataque") - carta_player01.get("defesa")
        if ataque_player01 > 0:
            vidap1 -= ataque_player02
        if ataque_player02 > 0:
            vidap2 -= ataque_player01

# Removendo cartas usadas na rodada
        cartas_p1.remove(carta_player01)
        cartas_p2.remove(carta_player02)

        if ataque_player01 > ataque_player02:
            print(f"Player {nome_player01} ganhou o round")
        if ataque_player02 > ataque_player01:
            print(f"Player {nome_player02} ganhou o round")

# Logica para determinar se o jogo acabou ou não.
        if len(cartas_p1) == 0:
            if vidap1 > vidap2:
                print(f"O player {nome_player01}, ganhou o jogo!")
            if vidap2 > vidap1:
                print(f"O player {nome_player02}, ganhou o jogo!")
            partida = 404

        elif vidap1 == 0:
            print(f"O player {nome_player02}, ganhou o jogo!")
            partida = 404

        elif vidap2 == 0:
            print(f"O player {nome_player01}, ganhou o jogo!")
            partida = 404
        else:
            continue
