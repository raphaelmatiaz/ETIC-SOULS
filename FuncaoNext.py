# def para dar "Next" aos textos que vemos no jogo. 

def FancyNext():
    print("|                                                                                                                                                               |")
    print("|                                                                            [ENTER] NEXT ->                                                                    |")
    print("|                                                                                                                                                               |")
    while True:
        opcao = input("|                                                                                                                                                               |").strip()
        if opcao != "":
            print("ERRO: Prime [ENTER] para avançar.")
        else:
            break


def NextDialogue():
    print("|                                                                                                                                                               |")
    while True:
        opcao = input("|                                                                                                                                                               |").strip()
        if opcao != "":
            print("ERRO: Prime [ENTER] para avançar.")
        else:
            break
