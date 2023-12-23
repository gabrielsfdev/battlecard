from auxiliar.cartas import Carta
# Adicionando as cartas personalizadas ao novo baralho personalizado
def create_baralho(): #Inicialmente o baralho terá 2 cartas, mudar posteriormente!!!
    nome = input("Adicione o nome da carta: ")
    atk = input("Adicione o valor de atk da carta: ")
    defesa = input("Adicione o ponto de defesa: ")
    supertrunfo = input("É uma carta supertrunfo ? ")
    supertrunfo = True if supertrunfo.lower() == "sim" else False
    return Carta(nome, atk, defesa, supertrunfo)

if __name__ == "__main__":
    teste1 = create_baralho()
    teste1.add_carta()
    print(teste1.ver_baralho())