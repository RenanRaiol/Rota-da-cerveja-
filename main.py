from biblioteca_usuarios import BibliotecaUsuarios

def main():
    biblioteca = BibliotecaUsuarios()

    while True:
        print("\n1. Cadastrar usuário")
        print("2. Fazer login")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite seu nome: ")
            senha = input("Digite sua senha: ")
            biblioteca.cadastrar_usuario(nome, senha)
        elif escolha == '2':
            nome = input("Digite seu nome: ")
            senha = input("Digite sua senha: ")
            biblioteca.fazer_login(nome, senha)
        elif escolha == '3':
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
