nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
frequencia = float(input("Digite a frequência (%): "))

# Calcula a média
media = (nota1 + nota2) / 2

# Verifica a frequência e a média
if frequencia < 75:
    print("Reprovado por falta")
elif media < 7:
    print("Reprovado por nota")
else:
    print("Aprovado")