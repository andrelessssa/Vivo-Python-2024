print( 11 + 10 )
print(1.5 + 1 + 0.5)

int() # Converte para inteiro (arredonda pra baixo)
float() # Converte para float (não arredonda)
round() # Arredondamento de um número, com a função round(numero, casas decimais)

# Operadores Aritméticos:
# + Adição
# - Subtração       
# * Multiplicação    
# / Divisão                  
# // Divisão Inteira      
# ** Potência                    
# % Resto da divisão                    

# Exemplos:
num = 10
den = 3

div = num/den # 3.333333333 

float ("a") # Se não for possível converter o que estiver dentro das aspas para float retorna ValueError
"a" / 2 # TypeError, pois o Python não entende como dividir uma string por um valor

# Outras operações:

print(5//2)