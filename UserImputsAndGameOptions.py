# IMPORTS

import MainMenuAndCharCreation
import Classes


#  2.2 def para observar aos arredores. Decidi adicionar esta def para que, unicamente através de texto, o jogador tenha
#a sensação de explorar aquilo que está à sua volta.

def ObservarArredores():
    print("|                                                                                                                                                               |")
    print("|                                                                    [ENTER] OBSERVAR ARREDORES                                                                 |")
    print("|                                                                                                                                                               |")
    while True:
        opcao = input("|                                                                                                                                                               |")
        if opcao == "":
            break



# 2.3 def Usar Abilidade

def UsarAbilidade():
    print("                                                                                                          ")
    print("                                         HABILIDADES                                                      ")
    print("                                      DO " + Classes.PlayerCharacter.Classe +                         "[X]")
    print("                                                                                                          ")
    print("      Habilidades:                                                                                        ")
    for habilidade in Classes.PlayerCharacter.Classe:
        for i in range('A', 'B', 'C', 'D'):
            print("[" + i + "]" + Classes.PlayerCharacter.Habilidades[i])
        print("                                                                                                          ")
        while True:
            opcao = input("A sua escolha: ").strip()
            if opcao not in ['A', 'B', 'C', 'D', 'X']:
                print("ERRO: Escolha uma opção válida.")
            else:
                if opcao == 'X':
                    print(" ")
                    print("SAIR DO JOGO?")
                    print("[A] SIM         [B] Não")
                    opcao = input("A sua escolha: ").strip()
                    while True:
                        opcao = input("A sua escolha: ").strip()
                        if opcao not in ['A', 'B']:
                            print("ERRO: Escolha uma opção válida.")
                        else:
                            if opcao == 'A':
                                MainMenuAndCharCreation.MainMenu()
                                break
                            if opcao == 'B':
                                UsarAbilidade()
                                break
                if opcao == 'A':
                    Classes.PlayerCharacter.Habilidade1()
                elif opcao == 'B':
                    Classes.PlayerCharacter.Habilidade2()
                elif opcao == 'C':
                    Classes.PlayerCharacter.Habilidade3()
                elif opcao == 'D':
                    Classes.PlayerCharacter.Habilidade4()

