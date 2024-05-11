def dizer_oi(nome):
    return f"Oi {nome}"

def incentivar_aprender(nome):
    return f"oi {nome}, vamos aprender!"

def mensagem_para_guilherme(funcao_mensagem):
    return funcao_mensagem("Guilherme")


print(mensagem_para_guilherme(dizer_oi))
print(mensagem_para_guilherme(incentivar_aprender))

# posso passar uma funcao como retorno da outra
# inner functions sao funcoes internas 

def pai():
    print("Escrevendo da pai() funcao")

    def filho1():
        print("Eu sou a filho1() funcao")

    def filho2():
        print("Eu sou a filho2() funcao")   

    filho1()
    filho2()


pai()

# funcao dentro de funcao

def calcular(operacao):
    def somar(a,b):
        return a + b
    
    def subtrair(a,b):
        return a - b
    
    if operacao == "+":
        return somar
    else:
        return subtrair
    
resultado = calcular("+")(1,3)
print(resultado)
        

#  outro exemplo

def mensagem(nome):
    print("executando mensagem")
    return f"oi {nome}"

def mensagem_longa(nome):
    print ("executando mensagem longa")
    return f"olaa {nome}"

def executar(funcao, nome):
    print("executando executar")
    return funcao(nome)

print(executar(mensagem, "Joao"))
print(executar(mensagem_longa, "Joao"))        


# funcao interna

def principal():
    print("Executando a funcao principal")

    def funcao_interna():
        print("Executando a funcao interna")

    def funcao_2():
        print("executandoa funcao 2")

    funcao_interna()
    funcao_2()

principal()


# inner function

def calculadora(operacao):
    def soma(a, b):
        return a + b
    def subtracao(a,b):
        return a - b
    def mul(a,b):
        return a * b
    def div(a,b):
        return a /b
    
   
