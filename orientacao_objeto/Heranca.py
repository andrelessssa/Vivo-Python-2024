class Veiculo:
    def __init__(self,cor, placa,numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligarMotor(self):
        print("Ligando Motor...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"    



    

class Motocicleta(Veiculo) :

    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa,numero_rodas, carregado):
        self.carregado = carregado

        super().__init__(cor, placa, numero_rodas)

    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

    

moto = Motocicleta("preta", "abc-1983",2)
moto.ligarMotor()

carro = Carro("branco", "cde-4567", 4)
carro.ligarMotor()

caminhao = Caminhao("azul", "fgh-3749", 8,False)
caminhao.ligarMotor()
caminhao.esta_carregado()


print(moto)
print(carro)
print(caminhao)