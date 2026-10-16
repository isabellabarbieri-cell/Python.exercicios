idade = int(input("Digite a idade: "))
estudante = input("É estudante? (s/n): ")

# Define o tipo de ingresso
if idade < 6:
    tipo_ingresso = "Gratuito"
    valor = 0
elif idade <= 17 or idade >= 60 or estudante == "s":
    tipo_ingresso = "Meia-entrada"
    valor = 20
else:
    tipo_ingresso = "Inteira"
    valor = 40

# Se for gratuito, não pede pagamento
if valor == 0:
    print("Gratuito — R$ 0.0")
else:
    # Entrada da forma de pagamento
    print("1 - PIX")
    print("2 - Débito")
    print("3 - Crédito")

    pagamento = int(input("Digite a forma de pagamento: "))

    # Aplica a alteração no valor
    if pagamento == 1:
        forma_pagamento = "PIX"
        valor = valor * 0.95
    elif pagamento == 2:
        forma_pagamento = "Débito"
    elif pagamento == 3:
        forma_pagamento = "Crédito"
        valor = valor * 1.05
    else:
        print("Forma de pagamento inválida")
        exit()

    # Mostra o resumo
    print(tipo_ingresso, "—", forma_pagamento, "— R$", valor)