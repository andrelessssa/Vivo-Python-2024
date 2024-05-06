class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}" 


def mostrarValores(*objs):
    for obj in objs:
        print(obj)       
    
aluno_1 = Estudante("Guilherme",1)
aluno_2 = Estudante("Giovanna", 2)

mostrarValores(aluno_1, aluno_2)

aluno_1.matricula = 3
mostrarValores(aluno_1, aluno_2)

Estudante.escola = "Python"
print(aluno_1)
print(aluno_2)
     