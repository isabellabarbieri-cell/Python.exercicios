jogador1 = input("Jogador 1: ")
jogador2 = input("Jogador 2: ")

# Verifica se as jogadas são válidas
if (jogador1 not in ["pedra", "papel", "tesoura"] or
    jogador2 not in ["pedra", "papel", "tesoura"]):
    print("Jogada inválida")

elif jogador1 == jogador2:
    print("Empate!")

elif ((jogador1 == "pedra" and jogador2 == "tesoura") or
      (jogador1 == "tesoura" and jogador2 == "papel") or
      (jogador1 == "papel" and jogador2 == "pedra")):
    print("Jogador 1 venceu!")

else:
    print("Jogador 2 venceu!")