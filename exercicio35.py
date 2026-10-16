numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, * ou /): ")

# Verifica qual operação será feita
if operador == "+":
    resultado = numero1 + numero2
    print("Resultado:", resultado)

elif operador == "-":
    resultado = numero1 - numero2
    print("Resultado:", resultado)

elif operador == "*":
    resultado = numero1 * numero2
    print("Resultado:", resultado)

elif operador == "/":
    if numero2 == 0:
        print("Erro: divisão por zero")
    else:
        resultado = numero1 / numero2
        print("Resultado:", resultado)

else:
    print("Operador inválido")