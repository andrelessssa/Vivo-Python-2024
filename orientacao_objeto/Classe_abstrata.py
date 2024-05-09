from abc import ABC, abstractmethod # importando a classe ABX

class ControleRemoto(ABC):   #Aqui eu falo que é uma extencao de ABC
    @abstractmethod  #Essa função abstrata tem que ser implementada em qualquer classe filha.
    def ligar(self):      # o metodo abstrato nao vai ter um corpo e as classes filhas sao obrigadas a implementar
        pass
    @abstractmethod    
    def desligar(self):
        pass  

    @property
    @abstractmethod
    def marca(self):
        pass      

class ControleTv(ControleRemoto): # agora eu soi obrigado a implementar esses dois metodos
    def ligar(self):
        print("Ligando a TV")
        

    def desligar(self):
        print("Desligando a TV...")



    @property
    def marca(self):
        return "LG"     
    


class ContrleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando Ar Condicionado")

    def desligar(self):
        print("desligando...")  

    @property
    def marca(self):
        return "LG"





controle = ControleTv()
controle.ligar()
controle.desligar()

controle = ContrleArCondicionado()
controle.ligar()
print(controle.marca)