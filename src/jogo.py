# //////// Aqui entrará o código principal do jogo /////////
from auxiliar.jogador import Player
menu = None
partida = 1

print(f"\t    S u p e r  T r u n f o\n\t\tDeck Pokemon\n\
    \t     release Lucas Diego\nSeja Bem-vindo  ao jogo Super Trunfo,\nO super trunfo é um jogo de RPG de cartas\
    \nEssa versão do game é Tematico pokemon, \ncriado por Lucas Diego, para começar o jogo\nprecisamos de algumas informações...")

inicio = input("Deseja iniciar? (Sim ou não): ")
inicio = inicio.lower()
if inicio == "sim":
    quantidade_jogadores = int(
        input("Insira a quantidade de jogadores (De 2 ou 4 jogadores): "))
    nivel_dificuldade = input("Insira o nivel de dificuldade (Facil/normal/dificil): ")
    if nivel_dificuldade.lower() == "facil":
        vida = 120
    if nivel_dificuldade.lower() == "normal":
        vida = 100
    if nivel_dificuldade.lower() == "dificil":
        vida = 80

    if quantidade_jogadores == 2:
        quantidade_carta = 7
        print("Nessa partida cada jogador irá iniciar com 7 cartas")
        nome_player01 = input("Digite o nome do jogador 01: ")
        nome_player02 = input("Digite o nome do jogador 02: ")

    if quantidade_jogadores == 4:
        quantidade_carta = 5
        print("Nessa partida cada jogador irá iniciar com 7 cartas")
        nome_player01 = input("Digite o nome do jogador 01: ")
        nome_player02 = input("Digite o nome do jogador 02: ")
        nome_player03 = input("Digite o nome do jogador 03: ")
        nome_player04 = input("Digite o nome do jogador 04: ")

    contador_distribuidor = 0

    cartas_p1 = []
    cartas_p2 = []
    cartas_p3 = []
    cartas_p4 = []

    
    # Fazer uma logica para distribuição de cartas
    p1 = Player(nome_player01, vida, quantidade_carta, cartas_p1)
    p2 = Player(nome_player02, vida, quantidade_carta, cartas_p2)
    p3 = Player(nome_player03, vida, quantidade_carta, cartas_p3)
    p4 = Player(nome_player04, vida, quantidade_carta, cartas_p4)
        
    # Menu do Jogo

    while partida != 404:
        if partida == None:
            partida = 1
        else:
            partida += 1

        print(f"Round {partida}")
        for i in quantidade_jogadores:
            if i == 1:
                nome = p1.nome
                numero_cartas = p1.numero_cartas
                vida = p1.vida
                cartas = p1.cartas
            if i == 2:
                nome = p2.nome
                numero_cartas = p2.numero_cartas
                vida = p2.vida
                cartas = p2.cartas
            if i == 3:
                nome = p3.nome
                numero_cartas = p3.numero_cartas
                vida = p3.vida
                cartas = p3.cartas
            if i == 4:
                nome = p4.nome
                numero_cartas = p4.numero_cartas
                vida = p4.vida
                cartas = p4.cartas
            
            print(f"Vez do player {nome}")
            
            while menu != 0:
                opcao = input("Menu Player")
                if opcao.lower() == "Listar cartas":
                    print(f"suas cartas são: {cartas}")
                if opcao.lower() == "numero de cartas":
                    print(numero_cartas)