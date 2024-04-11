import os 

def Main():
    chama_nome_app()
    lista_opcoes()

def Sair():
    os.system("cls")
    print("Finalizando aplicação\n")

def chama_nome_app():
    print("Programa Expresso")

def lista_opcoes():
    print("1- Cadastrar Restaurante")
    print("2- Listar Restaurante")
    print("3- Ativar Restaurante")
    print("4- Sair")

if __name__=="__main__":
    Main()
    OPCAO_DIGITADA = int(input("Selecione uma opção: "))

if (OPCAO_DIGITADA == 1):
    print("Você escolheu a opção cadastrar restaurante")
elif(OPCAO_DIGITADA == 2):
    print("Você escolheu a opção Listar restaurante")
elif(OPCAO_DIGITADA == 3):
    print("Você escolheu a opção Ativar restaurante")
elif(OPCAO_DIGITADA == 4):
    Sair()