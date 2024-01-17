# =======================================================================================================================================*/

# IMPORTS

import Classes
import os
import LoadingScreen as LoadingScreen




# MENU PRINCIPAL DO JOGO + MENU DE CRIAÇÃO DE PERSONAGin + INICIAR O JOGO

# Terminal Cleaner
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')



# GAME MAIN MENU


def MainMenu():
    clear_terminal()
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                               ▄████████     ███      ▄█   ▄████████         ▄████████  ▄██████▄  ███    █▄   ▄█          ▄████████|                           |")
    print("|                              ███    ███ ▀█████████▄ ███  ███    ███        ███    ███ ███    ███ ███    ███ ███         ███    ███                            |")
    print("|                              ███    █▀     ▀███▀▀██ ███▌ ███    █▀         ███    █▀  ███    ███ ███    ███ ███         ███    █▀                             |")
    print("|                             ▄███▄▄▄         ███   ▀ ███▌ ███               ███        ███    ███ ███    ███ ███         ███                                   |")
    print("|                            ▀▀███▀▀▀         ███     ███▌ ███             ▀███████████ ███    ███ ███    ███ ███       ▀███████████                            |")
    print("|                              ███    █▄      ███     ███  ███    █▄                ███ ███    ███ ███    ███ ███                ███                            |")
    print("|                              ███    ███     ███     ███  ███    ███         ▄█    ███ ███    ███ ███    ███ ███▌    ▄    ▄█    ███                            |")
    print("|                              ██████████    ▄████▀   █▀   ████████▀        ▄████████▀   ▀██████▀  ████████▀  █████▄▄██  ▄████████▀                             |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                         ┏┓   ┏┓┳┳┳┏┳┓                ┳┓   ┏┓┏┳┓┏┓┳┓┏┳┓                                                        |")
    print("|                                                    -~-  ┣┫   ┃┃┃┃┃ ┃  -~-       -~-  ┣┫   ┗┓ ┃ ┣┫┣┫ ┃  -~-                                                    |")
    print("|                                                         ┛┗•  ┗┻┗┛┻ ┻                 ┻┛•  ┗┛ ┻ ┛┗┛┗ ┻                                                         |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    while True:
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao != 'A' and opcao != 'B':
            print("ERRO: Escolha uma opção válida.")
        else:
            if opcao == 'A':
                quit()
        if opcao == 'B':
            CharacterCreation()





# ALTERAR CLASSE

def AlterarClasse():
    clear_terminal()
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                         ┏┓┓ ┏┓┏┓┏┓┏┓┏┓                                                                        |")
    print("| ---------------------------------------------------------------------~- ┃ ┃ ┣┫┗┓┗┓┣ ┗┓ -~---------------------------------------------------------------- [X] |")
    print("|                                                                         ┗┛┗┛┛┗┗┛┗┛┗┛┗┛                                                                        |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                   ■-----------------------------------------------------------------------------------------------------------------------■                   |")
    print("|                                                                                                                                                               |")
    print("|                          [A] Soldado     =========>         Um Soldado radiante, vestido em armadura de ferro inabalável.                                     |")
    print("|                                                             Efetivo em combate aproximado.                                                                    |")
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                          [B] Bandido     =========>         Um bandido sombrio que prospera na escuridão. Furtivo, o combate                                  |")
    print("|                                                             não é o seu forte, mas vitória não é sinónimo de afronto direto.                                  |")
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                          [C] Ermita      =========>         Um humano solitário que sobrevive na floresta isolada com a simples                               |")
    print("|                                                             força dos punhos. Possivelmente louco, devido aos anos de solidão.                                |")
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                          [D] Arqueiro    =========>         Um Arqueiro de precisão letal. Combatente intimidante em duelos                                   |")
    print("|                                                             à distância, mas capaz de se defender ao corpo-a-corpo.                                           |")
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                          [E] Alquimista  =========>         Um Alquimista que domina as artes místicas. Um mestre das poções e                                |")
    print("|                                                             preparações arcanas. Particularmente culto e informado.                                           |")
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                          [F] Mendigo     =========>        Um Mendigo sem nome. Uma alma destituída pela vida, sem nada a perder.                             |")
    print("|                                                            Fraco e frágil, por vezes desejante de nunca ter existido.                                         |")
    print("|                                                                                                                                                               |")
    print("|                    ■-----------------------------------------------------------------------------------------------------------------------■                  |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    while True:
        opcao = input("Escolha uma Classe: ")

        if opcao == 'X':
                Classes.PlayerCharacter.Genero = "Imput Required"
                Classes.PlayerCharacter.Classe = "Imput Required"
                Classes.PlayerCharacter.Nome = "Imput Required"
                MainMenu()
                break
        
        if opcao == 'A':
            Classes.PlayerCharacter.DisplayClasseName = 'Soldado'
            Classes.PlayerCharacter.Classe = Classes.Soldado
            Classes.PlayerCharacter.Barulho = True
            print("Classe Soldado escolhida com sucesso")
            break

        if opcao == 'B':
            Classes.PlayerCharacter.DisplayClasseName = 'Bandido'
            Classes.PlayerCharacter.Classe = Classes.Bandido
            Classes.PlayerCharacter.Barulho = False
            print("Classe Bandido escolhida com sucesso")
            break

        if opcao == 'C':
            Classes.PlayerCharacter.DisplayClasseName = 'Ermita'
            Classes.PlayerCharacter.Classe = Classes.Ermita
            Classes.PlayerCharacter.Barulho = True
            print("Classe Ermita escolhida com sucesso")
            break

        if opcao == 'D':
            Classes.PlayerCharacter.DisplayClasseName = 'Arqueiro'
            Classes.PlayerCharacter.Classe = Classes.Arqueiro
            Classes.PlayerCharacter.Barulho = False
            print("Classe Arqueiro escolhida com sucesso")
            break

        if opcao == 'E':
            Classes.PlayerCharacter.DisplayClasseName = 'Alquimista'
            Classes.PlayerCharacter.Classe = Classes.Alquimista
            Classes.PlayerCharacter.Barulho = True
            print("Classe Alquimista escolhida com sucesso")
            break

        if opcao == 'F':
            Classes.PlayerCharacter.DisplayClasseName = 'Mendigo'
            Classes.PlayerCharacter.Classe = Classes.Mendigo
            Classes.PlayerCharacter.Barulho = False
            print("Classe Mendigo escolhida com sucesso")
            break
        
        else:
            print("ERRO: Escolha uma classe válida.")
        
    clear_terminal()
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                         ┏┓┏┓┏┓┏┓┓ ┓┏┏┓                                                                        |")
    print("| ---------------------------------------------------------------------~- ┣ ┗┓┃ ┃┃┃ ┣┫┣┫ -~---------------------------------------------------------------- [X] |")
    print("|                                                                         ┗┛┗┛┗┛┗┛┗┛┛┗┛┗                                                                        |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                    -~- ESCOLHA UMA OPÇÃO -~-                                                                  |")
    print("|                                                                                                                                                               |")
    print("|                                                      > [A] Alterar Classe <          > [B] Escolher Nome <                                                    |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")

    while True:
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == 'X':
            Classes.PlayerCharacter.Genero = "Imput Required"
            Classes.PlayerCharacter.Classe = "Imput Required"
            Classes.PlayerCharacter.Nome = "Imput Required"
            MainMenu()
            break

        if opcao == 'A':
            AlterarClasse()
            break

        if opcao == 'B':
            EscolherNome()
            break
        
        else:
            print("ERRO: Escolha uma opção válida.")


        
# ALTERAR CLASSE 2

def AlterarClasse2():
    clear_terminal()
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                         ┏┓┓ ┏┓┏┓┏┓┏┓┏┓                                                                        |")
    print("| ---------------------------------------------------------------------~- ┃ ┃ ┣┫┗┓┗┓┣ ┗┓ -~---------------------------------------------------------------- [X] |")
    print("|                                                                         ┗┛┗┛┛┗┗┛┗┛┗┛┗┛                                                                        |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                   ■-----------------------------------------------------------------------------------------------------------------------■                   |")
    print("|                                                                                                                                                               |")
    print("|                          [A] Soldado     =========>         Um Soldado radiante, vestido em armadura de ferro inabalável.                                     |")
    print("|                                                             Efetivo em combate aproximado.                                                                    |")
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                          [B] Bandido     =========>         Um bandido sombrio que prospera na escuridão. Furtivo, o combate                                  |")
    print("|                                                             não é o seu forte, mas vitória não é sinónimo de afronto direto.                                  |")
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                          [C] Ermita      =========>         Um humano solitário que sobrevive na floresta isolada com a simples                               |")
    print("|                                                             força dos punhos. Possivelmente louco, devido aos anos de solidão.                                |")
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                          [D] Arqueiro    =========>         Um Arqueiro de precisão letal. Combatente intimidante em duelos                                   |")
    print("|                                                             à distância, mas capaz de se defender ao corpo-a-corpo.                                           |")
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                          [E] Alquimista  =========>         Um Alquimista que domina as artes místicas. Um mestre das poções e                                |")
    print("|                                                             preparações arcanas. Particularmente culto e informado.                                           |")
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                          [F] Mendigo     =========>        Um Mendigo sem nome. Uma alma destituída pela vida, sem nada a perder.                             |")
    print("|                                                            Fraco e frágil, por vezes desejante de nunca ter existido.                                         |")
    print("|                                                                                                                                                               |")
    print("|                    ■-----------------------------------------------------------------------------------------------------------------------■                  |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    while True:
        opcao = input("Escolha uma Classe: ")

        if opcao == 'X':
                Classes.PlayerCharacter.Genero = "Imput Required"
                Classes.PlayerCharacter.Classe = "Imput Required"
                Classes.PlayerCharacter.Nome = "Imput Required"
                MainMenu()
                break
        
        if opcao == 'A':
            Classes.PlayerCharacter.DisplayClasseName = 'Soldado'
            Classes.PlayerCharacter.Classe = Classes.Soldado
            Classes.PlayerCharacter.Barulho = True
            print("Classe Soldado escolhida com sucesso")
            JogadorIndeciso()
            break

        if opcao == 'B':
            Classes.PlayerCharacter.DisplayClasseName = 'Bandido'
            Classes.PlayerCharacter.Classe = Classes.Bandido
            Classes.PlayerCharacter.Barulho = False
            print("Classe Bandido escolhida com sucesso")
            JogadorIndeciso()
            break

        if opcao == 'C':
            Classes.PlayerCharacter.DisplayClasseName = 'Ermita'
            Classes.PlayerCharacter.Classe = Classes.Ermita
            Classes.PlayerCharacter.Barulho = True
            print("Classe Ermita escolhida com sucesso")
            JogadorIndeciso()
            break

        if opcao == 'D':
            Classes.PlayerCharacter.DisplayClasseName = 'Arqueiro'
            Classes.PlayerCharacter.Classe = Classes.Arqueiro
            Classes.PlayerCharacter.Barulho = False
            print("Classe Arqueiro escolhida com sucesso")
            JogadorIndeciso()
            break

        if opcao == 'E':
            Classes.PlayerCharacter.DisplayClasseName = 'Alquimista'
            Classes.PlayerCharacter.Classe = Classes.Alquimista
            Classes.PlayerCharacter.Barulho = True
            print("Classe Alquimista escolhida com sucesso")
            JogadorIndeciso()
            break

        if opcao == 'F':
            Classes.PlayerCharacter.DisplayClasseName = 'Mendigo'
            Classes.PlayerCharacter.Classe = Classes.Mendigo
            Classes.PlayerCharacter.Barulho = False
            print("Classe Mendigo escolhida com sucesso")
            JogadorIndeciso()
            break
        
        else:
            print("ERRO: Escolha uma classe válida.")




# ESCOLHER CLASSE

def EscolherClasse():
    clear_terminal()
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                         ┏┓┓ ┏┓┏┓┏┓┏┓┏┓                                                                        |")
    print("| ---------------------------------------------------------------------~- ┃ ┃ ┣┫┗┓┗┓┣ ┗┓ -~---------------------------------------------------------------- [X] |")
    print("|                                                                         ┗┛┗┛┛┗┗┛┗┛┗┛┗┛                                                                        |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                   ■-----------------------------------------------------------------------------------------------------------------------■                   |")
    print("|                                                                                                                                                               |")
    print("|                          [A] Soldado     =========>         Um Soldado radiante, vestido em armadura de ferro inabalável.                                     |")
    print("|                                                             Efetivo em combate aproximado.                                                                    |")
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                          [B] Bandido     =========>         Um bandido sombrio que prospera na escuridão. Furtivo, o combate                                  |")
    print("|                                                             não é o seu forte, mas vitória não é sinónimo de afronto direto.                                  |")
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                          [C] Ermita      =========>         Um humano solitário que sobrevive na floresta isolada com a simples                               |")
    print("|                                                             força dos punhos. Possivelmente louco, devido aos anos de solidão.                                |")
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                          [D] Arqueiro    =========>         Um Arqueiro de precisão letal. Combatente intimidante em duelos                                   |")
    print("|                                                             à distância, mas capaz de se defender ao corpo-a-corpo.                                           |")
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                          [E] Alquimista  =========>         Um Alquimista que domina as artes místicas. Um mestre das poções e                                |")
    print("|                                                             preparações arcanas. Particularmente culto e informado.                                           |")
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                          [F] Mendigo     =========>        Um Mendigo sem nome. Uma alma destituída pela vida, sem nada a perder.                             |")
    print("|                                                            Fraco e frágil, por vezes desejante de nunca ter existido.                                         |")
    print("|                                                                                                                                                               |")
    print("|                    ■-----------------------------------------------------------------------------------------------------------------------■                  |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    while True:
        opcao = input("Escolha uma Classe: ")
        
        if opcao == 'X':
            Classes.PlayerCharacter.Genero = "Imput Required"
            Classes.PlayerCharacter.Classe = "Imput Required"
            Classes.PlayerCharacter.Nome = "Imput Required"
            EscolherGenero = False
            MainMenu()
            break

        if opcao == 'A':
            Classes.PlayerCharacter.DisplayClasseName = 'Soldado'
            Classes.PlayerCharacter.Classe = Classes.Soldado
            Classes.PlayerCharacter.Barulho = True
            print("Classe Soldado escolhida com sucesso")
            break

        if opcao == 'B':
            Classes.PlayerCharacter.DisplayClasseName = 'Bandido'
            Classes.PlayerCharacter.Classe = Classes.Bandido
            Classes.PlayerCharacter.Barulho = False
            print("Classe Bandido escolhida com sucesso")
            break

        if opcao == 'C':
            Classes.PlayerCharacter.DisplayClasseName = 'Ermita'
            Classes.PlayerCharacter.Classe = Classes.Ermita
            Classes.PlayerCharacter.Barulho = True
            print("Classe Ermita escolhida com sucesso")
            break

        if opcao == 'D':
            Classes.PlayerCharacter.DisplayClasseName = 'Arqueiro'
            Classes.PlayerCharacter.Classe = Classes.Arqueiro
            Classes.PlayerCharacter.Barulho = False
            print("Classe Arqueiro escolhida com sucesso")
            break

        if opcao == 'E':
            Classes.PlayerCharacter.DisplayClasseName = 'Alquimista'
            Classes.PlayerCharacter.Classe = Classes.Alquimista
            Classes.PlayerCharacter.Barulho = True
            print("Classe Alquimista escolhida com sucesso")
            break

        if opcao == 'F':
            Classes.PlayerCharacter.DisplayClasseName = 'Mendigo'
            Classes.PlayerCharacter.Classe = Classes.Mendigo
            Classes.PlayerCharacter.Barulho = False
            print("Classe Mendigo escolhida com sucesso")
            break
        
        else:
            print("ERRO: Escolha uma classe válida.")
           
    clear_terminal()
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                         ┏┓┏┓┏┓┏┓┓ ┓┏┏┓                                                                        |")
    print("| ---------------------------------------------------------------------~- ┣ ┗┓┃ ┃┃┃ ┣┫┣┫ -~---------------------------------------------------------------- [X] |")
    print("|                                                                         ┗┛┗┛┗┛┗┛┗┛┛┗┛┗                                                                        |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                    -~- ESCOLHA UMA OPÇÃO -~-                                                                  |")
    print("|                                                                                                                                                               |")
    print("|                                                      > [A] Alterar Classe <          > [B] Escolher Nome <                                                    |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    
    while True:
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == 'X':
            Classes.PlayerCharacter.Genero = "Imput Required"
            Classes.PlayerCharacter.Classe = "Imput Required"
            Classes.PlayerCharacter.Nome = "Imput Required"
            MainMenu()
            break

        if opcao == 'A':
            AlterarClasse()
            break

        if opcao == 'B':
            EscolherNome()
            break

        else:
            print("ERRO: Escolha uma opção válida.")











# CHARACTER CREATION

    
def CharacterCreation():
    clear_terminal()
    print("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                ┏┓┳┓┳┏┓┳┓  ┏┓┏┓┳┓┏┓┏┓┳┓┏┓┏┓┏┓┳┳┓                                                               |")
    print("| ------------------------------------------------------------~- ┃-┣┫┃┣┫┣┫  ┃┃┣-┣┫┗┓┃┃┃┃┣┫┃┓┣-┃┃┃ -~----------------------------------------------------------- |")
    print("|                                                                ┗┛┛┗┻┛┗┛┗  ┣┛┗┛┛┗┗┛┗┛┛┗┛┗┗┛┗┛┛-┗                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")

    EscolherGenero()



# ESCOLHER GENERO + ALTERAR GENERO

# Funcao Alterar Genero

def AlterarGenero():
    clear_terminal()
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                          ┏┓┏┓┳┓┏┓┳┓┏┓                                                                         |")
    print("| ----------------------------------------------------------------------~- ┃┓┣ ┃┃┣ ┣┫┃┃ -~----------------------------------------------------------------- [X] |")
    print("|                                                                          ┗┛┗┛┛┗┗┛┛┗┗┛                                                                         |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                    -~- ALTERAR GÉNERO -~-                                                                     |")
    print("|                                                                                                                                                               |")
    print("|                                                           > [A] Masculino <        > [B] Feminino <                                                           |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    while True:
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == 'X':
            Classes.PlayerCharacter.Genero = "Imput Required"
            Classes.PlayerCharacter.Classe = "Imput Required"
            Classes.PlayerCharacter.Nome = "Imput Required"
            MainMenu()
            break

        if opcao == 'A':
            print("Genero alterado com sucesso")
            print("Genero 'Masculino' escolhido com sucesso")
            Classes.PlayerCharacter.Genero = 'Masculino'
            break
            
        if opcao == 'B':
            print("Genero alterado com sucesso")
            print("Genero 'Feminino' escolhido com sucesso")
            Classes.PlayerCharacter.Genero = 'Feminino'
            break

        else:
            print("ERRO: Escolha uma opção válida.")
                

    clear_terminal()
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                         ┏┓┏┓┏┓┏┓┓ ┓┏┏┓                                                                        |")
    print("| ---------------------------------------------------------------------~- ┣ ┗┓┃ ┃┃┃ ┣┫┣┫ -~---------------------------------------------------------------- [X] |")
    print("|                                                                         ┗┛┗┛┗┛┗┛┗┛┛┗┛┗                                                                        |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                    -~- ESCOLHA UMA OPÇÃO -~-                                                                  |")
    print("|                                                                                                                                                               |")
    print("|                                                      > [A] Alterar Género <        > [B] Escolher Classe <                                                    |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    while True:
        opcao = input("Escolha uma opção: ").strip()
        if opcao != 'A' and opcao != 'B' and opcao != 'X':
            print("ERRO: Escolha uma opção válida.")
        if opcao == 'X':
            Classes.PlayerCharacter.Genero = "Imput Required"
            Classes.PlayerCharacter.Classe = "Imput Required"
            Classes.PlayerCharacter.Nome = "Imput Required"
            MainMenu()
            break
        if opcao == 'A':
            AlterarGenero()
            break
        if opcao == 'B':
            EscolherClasse()
            break


# ALTERAR GENERO 2

def AlterarGenero2():
    clear_terminal()
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                          ┏┓┏┓┳┓┏┓┳┓┏┓                                                                         |")
    print("| ----------------------------------------------------------------------~- ┃┓┣ ┃┃┣ ┣┫┃┃ -~----------------------------------------------------------------- [X] |")
    print("|                                                                          ┗┛┗┛┛┗┗┛┛┗┗┛                                                                         |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                    -~- ALTERAR GÉNERO -~-                                                                     |")
    print("|                                                                                                                                                               |")
    print("|                                                           > [A] Masculino <        > [B] Feminino <                                                           |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")

    while True:
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == 'X':
            Classes.PlayerCharacter.Genero = "Imput Required"
            Classes.PlayerCharacter.Classe = "Imput Required"
            Classes.PlayerCharacter.Nome = "Imput Required"
            MainMenu()
            break

        if opcao == 'A':
            print("Genero alterado com sucesso")
            print("Genero 'Masculino' escolhido com sucesso")
            Classes.PlayerCharacter.Genero = 'Masculino'
            JogadorIndeciso()
            break
            
        if opcao == 'B':
            print("Genero alterado com sucesso")
            print("Genero 'Feminino' escolhido com sucesso")
            Classes.PlayerCharacter.Genero = 'Feminino'
            JogadorIndeciso()
            break

        else:
            print("ERRO: Escolha uma opção válida.")
            
  


# Funcao Escolher Genero

def EscolherGenero():
    clear_terminal()
    
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                          ┏┓┏┓┳┓┏┓┳┓┏┓                                                                         |")
    print("| ----------------------------------------------------------------------~- ┃┓┣ ┃┃┣ ┣┫┃┃ -~---------------------------------------------------------------- [X]  |")
    print("|                                                                          ┗┛┗┛┛┗┗┛┛┗┗┛                                                                         |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                    -~- ESCOLHA UM GÉNERO -~-                                                                  |")
    print("|                                                                                                                                                               |")
    print("|                                                           > [A] Masculino <        > [B] Feminino <                                                           |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    while True:
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == 'X':
            Classes.PlayerCharacter.Genero = "Imput Required"
            Classes.PlayerCharacter.Classe = "Imput Required"
            Classes.PlayerCharacter.Nome = "Imput Required"
            MainMenu()
            break
        if opcao == 'A':
            print("Género 'Masculino' escolhido com sucesso")
            Classes.PlayerCharacter.Genero = 'Masculino'
            break
            
        if opcao == 'B':
            print("Género 'Feminino' escolhido com sucesso")
            Classes.PlayerCharacter.Genero = 'Feminino'
            break
        else:
            print("ERRO: Escolha uma opção válida.")


    clear_terminal()
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                         ┏┓┏┓┏┓┏┓┓ ┓┏┏┓                                                                        |")
    print("| ---------------------------------------------------------------------~- ┣ ┗┓┃ ┃┃┃ ┣┫┣┫ -~---------------------------------------------------------------- [X] |")
    print("|                                                                         ┗┛┗┛┗┛┗┛┗┛┛┗┛┗                                                                        |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                    -~- ESCOLHA UMA OPÇÃO -~-                                                                  |")
    print("|                                                                                                                                                               |")
    print("|                                                      > [A] Alterar Género <        > [B] Escolher Classe <                                                    |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")

    while True:
        opcao = input("Escolha uma opção: ").strip()
        if opcao != 'A' and opcao != 'B' and opcao != 'X':
            print("ERRO: Escolha uma opção válida.")
        if opcao == 'X':
            Classes.PlayerCharacter.Genero = "Imput Required"
            Classes.PlayerCharacter.Classe = "Imput Required"
            Classes.PlayerCharacter.Nome = "Imput Required"
            MainMenu()
            break
        if opcao == 'A':
            AlterarGenero()
            break
        if opcao == 'B':
            EscolherClasse()
            break
            
                    
# ALTERAR NOME

def AlterarNome():
    clear_terminal()
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                            ┳┓┏┓┳┳┓┏┓                                                                          |")
    print("| ------------------------------------------------------------------------~- ┃┃┃┃┃┃┃┣ -~------------------------------------------------------------------- [X] |")
    print("|                                                                            ┛┗┗┛┛ ┗┗┛                                                                          |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                      -~- ALTERAR NOME -~-                                                                     |")
    print("|                                                                                                                                                               |")
    print("|                                                          > Escreva um novo nome para a sua Personagem <                                                       |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")

    while True:
        nome = input("Novo nome: ").strip()

        if nome != "":
            Classes.PlayerCharacter.Nome = nome
            print("Nome alterado para '" + str(nome) + "' com sucesso")
            break
        else:
            print("ERRO: Insira um nome de pelo menos 1 caracter")

    clear_terminal()
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                         ┏┓┏┓┏┓┏┓┓ ┓┏┏┓                                                                        |")
    print("| ---------------------------------------------------------------------~- ┣ ┗┓┃ ┃┃┃ ┣┫┣┫ -~---------------------------------------------------------------- [X] |")
    print("|                                                                         ┗┛┗┛┗┛┗┛┗┛┛┗┛┗                                                                        |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                    -~- ESCOLHA UMA OPÇÃO -~-                                                                  |")
    print("|                                                                                                                                                               |")
    print("|                                                      > [A] Alterar Nome <        > [B] Terminar Personagem <                                                  |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")

    while True:
        opcao = input("Escolha uma opção: ").strip()
        if opcao !=  'A' and opcao != 'B' and opcao != 'X':
            input("ERRO: Escolha uma opção válida.")
        if opcao == 'X':
            Classes.PlayerCharacter.Genero = "Imput Required"
            Classes.PlayerCharacter.Classe = "Imput Required"
            Classes.PlayerCharacter.Nome = "Imput Required"
            MainMenu()
        else:
            if opcao == 'A':
                AlterarNome()
                break
            if opcao == 'B':
                CharacterFinalization()
                break
            

# ALTERAR NOME 2

def AlterarNome2():
    clear_terminal()
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                            ┳┓┏┓┳┳┓┏┓                                                                          |")
    print("| ------------------------------------------------------------------------~- ┃┃┃┃┃┃┃┣ -~------------------------------------------------------------------- [X] |")
    print("|                                                                            ┛┗┗┛┛ ┗┗┛                                                                          |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                      -~- ALTERAR NOME -~-                                                                     |")
    print("|                                                                                                                                                               |")
    print("|                                                          > Escreva um novo nome para a sua Personagem <                                                       |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")

    while True:
        nome = input("Novo nome: ").strip()

        if nome != "":
            Classes.PlayerCharacter.Nome = nome
            print("Nome alterado para '" + str(nome) + "' com sucesso")
            JogadorIndeciso()
            break
        else:
            print("ERRO: Insira um nome de pelo menos 1 caracter")



# ESCOLHER NOME

def EscolherNome():
    clear_terminal()

    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                            ┳┓┏┓┳┳┓┏┓                                                                          |")
    print("| ------------------------------------------------------------------------~- ┃┃┃┃┃┃┃┣ -~------------------------------------------------------------------- [X] |")
    print("|                                                                            ┛┗┗┛┛ ┗┗┛                                                                          |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                    -~- ESCOLHA UM NOME -~-                                                                    |")
    print("|                                                                                                                                                               |")
    print("|                                                           > Escreva um nome para a sua Personagem <                                                           |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")

    while True:
        nome = input("Nome: ").strip()

        if nome != "":
            Classes.PlayerCharacter.Nome = nome
            print("Nome " + "'" + str(nome) + "'" + " definido com sucesso")
            break
        else:
            print("ERRO: Insira um nome de pelo menos 1 caracter")

    clear_terminal()
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                         ┏┓┏┓┏┓┏┓┓ ┓┏┏┓                                                                        |")
    print("| ---------------------------------------------------------------------~- ┣ ┗┓┃ ┃┃┃ ┣┫┣┫ -~---------------------------------------------------------------- [X] |")
    print("|                                                                         ┗┛┗┛┗┛┗┛┗┛┛┗┛┗                                                                        |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                    -~- ESCOLHA UMA OPÇÃO -~-                                                                  |")
    print("|                                                                                                                                                               |")
    print("|                                                      > [A] Alterar Nome <        > [B] Terminar Personagem <                                                  |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")

    while True:
        opcao = input("Escolha uma opção: ").strip()
        if opcao !=  'A' and opcao != 'B' and opcao != 'X':
            input("ERRO: Escolha uma opção válida.")
        if opcao == 'X':
            Classes.PlayerCharacter.Genero = "Imput Required"
            Classes.PlayerCharacter.Classe = "Imput Required"
            Classes.PlayerCharacter.Nome = "Imput Required"
            MainMenu()
        else:
            if opcao == 'A':
                AlterarNome()
                break
            if opcao == 'B':
                CharacterFinalization()
                break


# Finalizar Personagin e Iniciar o Jogo

def CharacterFinalization():
    clear_terminal()
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                     ┏┓┏┓┳┓┏┓┏┓┳┓┏┓┏┓┏┓┳┳┓                                                                     |")
    print("| -----------------------------------------------------------------~- ┃┃┣-┣┫┗┓┃┃┃┃┣┫┃┓┣-┃┃┃ -~------------------------------------------------------------ [X]  |")
    print("|                                                                     ┣┛┗┛┛┗┗┛┗┛┛┗┛┗┗┛┗┛┛-┗                                                                     |")
    print("|                                                                                                                                                               |")
    print("|                    ■-----------------------------------------------------------------------------------------------------------------------■                  |")
    print("|                                                                                                                                                               |")
    print("                                         GÉNERO     =========> " +         str(Classes.PlayerCharacter.Genero)                                                    )
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                                        CLASSE     =========> " +         str(Classes.PlayerCharacter.DisplayClasseName)                                         )
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                                        NOME      =========> " +         str(Classes.PlayerCharacter.Nome)                                                       )
    print("|                                                                                                                                                               |")
    print("|                    ■-----------------------------------------------------------------------------------------------------------------------■                  |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                       VALIDAR PERSONAGEM                                                                      |")
    print("|                                                                           -~- & -~-                                                                           |")
    print("|                                                                         INICIAR JOGO?                                                                         |")
    print("|                                                                                                                                                               |")
    print("|                                                                > [A] Sim <       > [B] Não <                                                                  |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")

    while True:
        opcao = input("Escolha uma opção: ").strip()
        if opcao !=  'A' and opcao != 'B' and opcao != 'X':
            input("ERRO: Escolha uma opção válida.")
        if opcao == 'X':
            Classes.PlayerCharacter.Genero = "Imput Required"
            Classes.PlayerCharacter.Classe = "Imput Required"
            Classes.PlayerCharacter.Nome = "Imput Required"
            MainMenu()
        else:
            if opcao == 'A':
                LoadingScreen.LoadingScreen()
                import Jogo as StartGame
                StartGame.Jogo()
                
            if opcao == 'B':
                JogadorIndeciso()
                break
         
# Caso o Jogador queira alterar escolhas prévias
                                                
def JogadorIndeciso():
    clear_terminal()
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")
    print("|                                                                                                                                                               |")
    print("|                                                                     ┏┓┏┓┳┓┏┓┏┓┳┓┏┓┏┓┏┓┳┳┓                                                                     |")
    print("| -----------------------------------------------------------------~- ┃┃┣-┣┫┗┓┃┃┃┃┣┫┃┓┣-┃┃┃ -~------------------------------------------------------------ [X]  |")
    print("|                                                                     ┣┛┗┛┛┗┗┛┗┛┛┗┛┗┗┛┗┛┛-┗                                                                     |")
    print("|                                                                                                                                                               |")
    print("|                    ■-----------------------------------------------------------------------------------------------------------------------■                  |")
    print("|                                                                                                                                                               |")
    print("                                         GÉNERO     =========> " +         str(Classes.PlayerCharacter.Genero)                                                    )
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                                        CLASSE     =========> " +         str(Classes.PlayerCharacter.DisplayClasseName)                                         )
    print("|                                                                                                                                                               |")
    print("|                        ■-------------------------------------------------------------------------------------------------------------■                        |")
    print("|                                                                                                                                                               |")
    print("|                                        NOME      =========> " +         str(Classes.PlayerCharacter.Nome)                                                       )
    print("|                                                                                                                                                               |")
    print("|                    ■-----------------------------------------------------------------------------------------------------------------------■                  |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                 -~- O QUE DESEJA ALTERAR? -~-                                                                 |")
    print("|                                                                                                                                                               |")
    print("|                                                          > [A] Nada <               > [B] Tudo <                                                              |")
    print("|                                                          > [C] Género <             > [D] Classe <                                                            |")
    print("|                                                          > [E] Nome <                                                                                         |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                ---------------------------------------------------------------                                                |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("■ ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— ■")

    while True:
        opcao = input("Escolha uma opção: ")
        

        if opcao == 'X':
            Classes.PlayerCharacter.Genero = "Imput Required"
            Classes.PlayerCharacter.Classe = "Imput Required"
            Classes.PlayerCharacter.Nome = "Imput Required"
            MainMenu()
            break

        if opcao == 'A':
            CharacterFinalization()
            break

        if opcao == 'B':
            Classes.PlayerCharacter.Genero = "Imput Required"
            Classes.PlayerCharacter.Classe = "Imput Required"
            Classes.PlayerCharacter.Nome = "Imput Required"
            CharacterCreation()
            break

        if opcao == 'C':
            AlterarGenero2()
            break

        if opcao == 'D':
            AlterarClasse2()
            break

        if opcao == 'E':
            AlterarNome2()
            break

        else:
            input("ERRO: Escolha uma opção válida.")





# GAME LAUNCHER 

def LaunchGame():
    MainMenu()
    
                                


# =======================================================================================================================================*/

LaunchGame()