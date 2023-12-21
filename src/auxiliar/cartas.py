# ///// Coloque aqui o código referente a criação ou manipulação das cartas //////
# Exemplo abaixo pode ser apagado, alterado ou feito alterações:
baralho = {}
class Carta:
    def __init__(self, nome, atk, defe, supertrunfo=False) -> None:
        self.nome = nome
        self.atk = atk
        self.defe = defe
        self.super_trunfo = supertrunfo

    def add_carta(self):
        baralho[f"Carta_{len(baralho) + 1}"] = {"nome": self.nome, "ataque": self.atk, "defesa": self.defe, "super_trunfo": self.super_trunfo}

    def ver_baralho(self):
        return baralho

    def atacar():
        pass

    def defender():
        pass
