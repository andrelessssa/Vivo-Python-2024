class Construtor:
    def __init__(self, nome, cor, acordado=True):
        print("inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instancia da classe...")    

    def falar(self):
        print("Falandooooo")

        


c1 = Construtor("champpie", "amarelo",)
c1.falar()