
usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

# Verifica o usuário
if usuario == "aluno":

    # Verifica a senha
    if senha == "1234":
        print("Login realizado com sucesso!")
    else:
        print("Senha incorreta")

else:
    print("Usuário não encontrado")