def resumo():
    mensagem = ""
    return mensagem


def doutorado():
    mensagem = ""
    return mensagem


def contribuicoes():
    mensagem = ""
    return mensagem


def artigos():
    mensagem = "1 - Packet switching in radio channels: Part I-carrier sense multiple-access modes and their throughput-delay characteristics
                2-A brief history of the Internet 
                3-Queueing system
                4-Virtual cut-through: A new computer communication switching technique
                5-Packet switching in a multiaccess broadcast channel: Performance evaluation"
    return mensagem


def citacoes():
    mensagem = " 1- O compuador é o maior inimigo do pensamento critico
                 2- Nunca, nunca aceite um emprego, não importa quão alto seja o salário (se você o odeia). Nunca caia nessa armadilha.
                 3- Se você receber um chamado para acordar, pode ir para um canto, chorar e ser derrotado, ou pode fazer algo a respeito e se esforçar "
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
