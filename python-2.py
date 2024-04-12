import os

restaurantes = []

def finalizar_app():
    os.system("clear")
    os.system("cls")
    print("Finalizando o app\n")

def escolher_opcoes():
    print("Programa Expresso\n")
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurante")
    print("3 - Ativar restaurante")
    print("4 - Sair\n")

def opcao_invalida():
    print("Opção inválida\n")
    input("Digite uma tecla para voltar ao menu principal: ")
    main()

def chamar_nome_do_app():
    print("Restaurante Expressao\n")

def cadastrar_novo_restaurante():
    nome_do_restaurante = input("Digite o nome do novo restaurante: ")
    restaurantes.append(nome_do_restaurante)
    print(f"Você cadastrou o restaurante: {nome_do_restaurante}")
    input("Digite uma tecla para voltar para o menu principal:")
    main()
   

def main():
    escolher_opcoes()
    chamar_nome_do_app()
    try:
        opcaodigitada = int(input("Digite a opção desejada: "))
        if opcaodigitada == 1:
            print("Você escolheu cadastrar restaurante\n")
            cadastrar_novo_restaurante()
        elif opcaodigitada == 2:
            print("Você escolheu listar restaurante\n")
        elif opcaodigitada == 3:
            print("Você escolheu ativar restaurante\n")
        elif opcaodigitada == 4:
            print("Você escolheu sair do aplicativo\n")
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

if __name__ == "__main__":
    finalizar_app()
    main()
