class Conta:
    def __init__(self,nro_agencia, saldo=0) :
        self._saldo = saldo        # o _ indica que é privado
        self.nro_agencia = nro_agencia
    def sacar(self, valor):
        self._saldo -= valor

    def depositar(self, valor):
        self._saldo += valor
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"    
    



conta = Conta("0001",100)
conta.depositar(100)
print(conta._saldo) # esse nao é o jeito correto de acessar uma variavel, mas ele permite
print(conta)