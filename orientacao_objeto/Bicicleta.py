class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): # cria um contrutor
    
        self.cor = cor  # o self é uma referencia prar o objeto é o this do java
        self.modelo = modelo
        self.ano = ano
        self.valor = valor 

    def buzinar(self):  # métodos sao funcaoes dentro da classe
        print("Buzinaaaaaaaa")

    def parar(self):
        print("Parandooooooo")
        print("Bicicleta parada")   

    def correr(self):
        print("Vruuuummmmmmmm")

    # def __str__(self):
    #    return f"Cor da bicicleta: {self.cor}, {self.modelo}"  

    # assim se eu adiciono um atibuto ele vem automatico
    def __str__(self):
        return f"{ self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
print(f"Cor da bicicleta: {b1.cor}")
b1.buzinar()
b1.parar()
b1.correr()

# ou

Bicicleta.buzinar(b1)

print(b1) # chamada para o metodo __str__


