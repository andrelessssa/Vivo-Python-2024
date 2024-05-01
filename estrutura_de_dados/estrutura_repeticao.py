a = int(input("Digite um numero: "))
print("o numero é ",a)

texto = input("informe um texto")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")

for numero in range (0,51,5):
    print(numero)

