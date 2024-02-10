usuarios = {}
print('BEM VINDO  ROTA DA CERVEJA')


def cadastrar_usuario():
    email = input("Digite seu email")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    usuarios[nome] = senha
    print("Usuário cadastrado com sucesso!")


def fazer_login():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    if email in usuarios and usuarios[email] == senha:
        print("Login bem-sucedido!")
    else:
        print("Nome de usuário ou senha incorretos.")


def main():
    while True:
        print("\n1. Cadastrar usuário")
        print("2. Fazer login")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_usuario()
        elif escolha == '2':
            fazer_login()
        elif escolha == '3':
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
