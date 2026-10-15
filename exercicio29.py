numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Começa considerando o primeiro como maior
maior = numero1

# Compara com o segundo
if numero2 > maior:
    maior = numero2

# Compara com o terceiro
if numero3 > maior:
    maior = numero3

# Saída
print("O maior é", maior)