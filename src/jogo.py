#==================I M P O R T A Ç Õ E S==========================

import random

from data.cartas import Deck_Lucas

from auxiliar.jogador import Player

#=================V A R I A V E I S  U T E I S=====================

menu = None
partida = None
quantidade_jogadores = 2

#===================C O D I G O  P R I N C I P A L==================

print(f"\t    S u p e r  T r u n f o\n\t\tDeck Pokemon\n\
    \t     release Lucas Diego\nSeja Bem-vindo  ao jogo Super Trunfo,\nO super trunfo é um jogo de RPG de cartas\
    \nEssa versão do game é Tematico pokemon, \ncriado por Lucas Diego, para começar o jogo\nprecisamos de algumas informações...")

inicio = input("Deseja iniciar? (Sim ou não): ")
inicio = inicio.lower()


if inicio == "sim":
    nivel_dificuldade = input(
        "Insira o nivel de dificuldade (Facil/normal/dificil): ")
    if nivel_dificuldade.lower() == "facil":
        vida = 120
    if nivel_dificuldade.lower() == "normal":
        vida = 100
    if nivel_dificuldade.lower() == "dificil":
        vida = 80

    quantidade_carta = 7
    print("Nessa partida cada jogador irá iniciar com 7 cartas")
    nome_player01 = input("Digite o nome do jogador 01: ")
    nome_player02 = input("Digite o nome do jogador 02: ")

    contador_distribuidor = 0

    cartas_p1 = []
    cartas_p2 = []

    while len(cartas_p1) < 7: 
        cartas_p1.append(random.choice(list(Deck_Lucas.keys())))
    while len(cartas_p2) < 7:
        cartas_p2.append(random.choice(list(Deck_Lucas.keys())))

    p1 = Player(nome_player01, vida, quantidade_carta, cartas_p1)
    p2 = Player(nome_player02, vida, quantidade_carta, cartas_p2)

    # Menu do Jogo

    while partida != 404:
        if partida == None:
            partida = 1
        else:
            partida += 1

        print(f"Round {partida}")
        for i in range(1,2):
            if i == 1:
                nome = p1.nome
                numero_cartas = p1.numero_cartas
                vida = p1.vida
                cartas = p1.cartas

                print(f"Vez do player {nome}")

                while menu != 0:
                    print("Menu Player")
                    opcao = input("Dentre as seguintes opções, decida oque quer fazer:\nListar cartas; Numero de cartas; Visualizar a vida; jogar; pular partida")
                    if opcao.lower() == "Listar cartas":
                        print(f"suas cartas são: {cartas}")
                    if opcao.lower() == "numero de cartas":
                        print(numero_cartas)
                    if opcao.lower() == "Visualizar a vida":
                        print(f"Sua vida no momento é {vida}")
                    if opcao.lower() == "Jogar":
                        carta_jogada = input("Insira Qual das suas cartas, você deseja jogar: ")
                        menu = 0
                    if opcao.lower() == "pular partida":
                        carta_jogada = input(f"Jogador {nome}, pulou a partida!")
                        menu = 0
                carta_player01 = Deck_Lucas[carta_jogada]
            if i == 2:
                nome = p2.nome
                numero_cartas = p2.numero_cartas
                vida = p2.vida
                cartas = p2.cartas

                print(f"Vez do player {nome}")

                while menu != 0:
                    print("Menu Player")
                    opcao = input("Dentre as seguintes opções, decida oque quer fazer:\nListar cartas; Numero de cartas; Visualizar a vida; jogar; pular partida")
                    if opcao.lower() == "Listar cartas":
                        print(f"suas cartas são: {cartas}")
                    if opcao.lower() == "numero de cartas":
                        print(numero_cartas)
                    if opcao.lower() == "Visualizar a vida":
                        print(f"Sua vida no momento é {vida}")
                    if opcao.lower() == "Jogar":
                        carta_jogada = input("Insira Qual das suas cartas, você deseja jogar: ")
                        menu = 0
                    if opcao.lower() == "pular partida":
                        carta_jogada = input(f"Jogador {nome}, pulou a partida!")
                        menu = 0
                carta_player02 = Deck_Lucas[carta_jogada]
 
            # Adicionar logica de combate entre as cartas
