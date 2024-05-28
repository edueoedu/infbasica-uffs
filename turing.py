def resumo():
    mensagem = "Leonard Kleinrock (Nova Iorque, 13 de junho de 1934) é um engenheiro e cientista da computação e professor de ciência da computação da Escola de Engenharia e Ciências Aplicadas da Universidade da Califórnia em Los Angeles (UCLA), que fez diversas contribuições importantes para o campo das redes de computadores, em especial para o lado teórico das redes de computadores e da teoria das filas. Ele também desempenhou um papel importante no desenvolvimento da Arpanet, a precursora da Internet, na UCLA."
    return mensagem


def doutorado():
    mensagem = "O Professor Doutor Kleinrock recebeu o seu grau de doutoramento do Instituto de Tecnologia de Massachusetts, em 1963."
    return mensagem


def contribuicoes():
    mensagem = "O Professor Doutor Kleinrock ganhou maior reconhecimento quando recebeu, em 2007, a Medalha Nacional da Ciência, o mais alto reconhecimento para feitos científicos, atribuída pelo Presidente dos Estados Unidos. Esta Medalha foi concedida pelas contribuições essenciais no que respeita aos fundamentos matemáticos da ciência da computação moderna, à especificação funcional de comutação de pacotes que deu origem à Internet, à orientação de gerações de estudantes e liderança e comercialização de tecnologias que transformaram o mundo."
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
