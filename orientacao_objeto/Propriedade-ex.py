class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"    

    @property
    def nome(self):
        return f'{self._nome}'
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento



pessoa = Pessoa("Andre", 1984)
print(f"Nome: {pessoa.nome}")
print(f"Idade da pessoa: {pessoa.idade}")

