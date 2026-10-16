idade = int(input("Digite a idade: "))

# Verifica a situação eleitoral
if idade < 16:
    print("Não pode votar")
elif idade < 18:
    print("Voto facultativo")
elif idade <= 70:
    print("Voto obrigatório")
else:
    print("Voto facultativo")