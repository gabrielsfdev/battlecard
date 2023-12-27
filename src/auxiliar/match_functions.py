from auxiliar.cartas import Card

def deck_create(deck):
    name = input("Adicione o nome da carta: ")
    atk = int(input("Adicione o valor de atk da carta: "))
    defense = int(input("Adicione o ponto de defesa: "))
    supercard = input("É uma carta supertrunfo ? ")
    supercard = True if supercard.lower() == "sim" else False
    return Card(name, atk, defense, deck, supercard)

def deck_choice():
    while True:
        choice = input("Você prefere utilizar um deck padrão(1) ou criar um deck novo(2) ? ")
        if choice.lower() == "1":
            return "default"
        elif choice.lower() == "2":
            return "customizer"
        else:
            print("Valor inválido, por favor, digite 1 para deck padrão ou 2 para criar um deck novo: ")
