# ================================================================================================================*/

# Classe PlayerCharacter (Contentor para as informações sobre personagem do jogador) 

class PlayerCharacter:
    def __init__(self, genero, classe, nome, barulho):
        self.Genero = genero
        self.Classe = classe
        self.Nome = nome
        self.Barulho = barulho  # Needs further definition
        self.DisplayClasseName = 'chosen class name'



# ============================ CLASSES ============================

# Classe Soldado 

class Soldado:
    def __init__(self, life, strength, energy, intelligence, noisy, abilities, equipment, weapons):
        self.life = 100
        self.strength = 60
        self.energy = 80
        self.intelligence = 20
        self.noisy = True

        self.Habilidade1 = Esquivar()
        self.Habilidade2 = Atacar()
        self.Habilidade3 = Bloquear()
        self.Habilidade4 = FrontKick()

        self.equipment = {'Cabeça': 'Capacete de Ferro', 'Tronco': 'Armadura de Ferro', 'Mãos': 'Manoplas de Ferro', 'Pernas': 'Leggins de Ferro'}
        self.weapons = {'Mão Direita': 'Espada de Ferro', 'Mão Esquerda': 'Escudo de Ferro'}
        self.inventory = []


# Classe Bandido

class Bandido:
    def __init__(self, life, strength, energy, intelligence, noisy, abilities, equipment, weapons):
        self.life = 60
        self.strength = 30
        self.energy = 150
        self.intelligence = 50
        self.noisy = False

        self.Habilidade1 = Esquivar()
        self.Habilidade2 = Roubar()
        self.Habilidade3 = BackStab()
        self.Habilidade4 = Camuflar()

        self.equipment = {'Cabeça': 'Capuz Ocultante', 'Tronco': 'Capa de Cabedal Preta', 'Mãos': 'Luvas de Cabedal Pretas', 'Pernas': 'Calças de Cabedal Preto'}
        self.weapons = {'Mão Direita': 'Punhal', 'Mão Esquerda': 'null'}
        self.inventory = []



# Classe Ermita

class Ermita:
    def __init__(self, life, strength, energy, intelligence, noisy, abilities, equipment, weapons):
        self.life = 120
        self.strength = 120
        self.energy = 60
        self.intelligence = 10
        self.noisy = True

        self.Habilidade1 = "Esquivar"
        self.Habilidade2 = "Intimidar"
        self.Habilidade3 = "Atacar"
        self.Habilidade4 = "Camuflar"

        self.equipment = {'Cabeça': 'null', 'Tronco': 'null', 'Mãos': 'null', 'Pernas': 'Velhas Calças Rotas'}
        self.weapons = {'Mão Direita': 'null', 'Mão Esquerda': 'null'}
        self.inventory = []


# Classe Arqueiro

class Arqueiro:
    def __init__(self, life, strength, energy, intelligence, noisy, abilities, equipment, weapons, consumables):
        self.life = 60
        self.strength = 30
        self.energy = 120
        self.intelligence = 60
        self.noisy = False

        self.Habilidade1 = "Esquivar"
        self.Habilidade2 = "Atacar"
        self.Habilidade3 = "DespararFlecha"
        self.Habilidade4 = "Camuflar"

        self.equipment = {'Cabeça': 'Capuz de tecido', 'Tronco': 'Armadura de Cabedal', 'Mãos': 'null', 'Pernas': 'Leggins de Cabedal'}
        self.weapons = {'Mão Direita': 'Punhal', 'Mão Esquerda': 'Arco'}
        self.consumables = {'Flechas': 10}
        self.inventory = []

# Classe Alquimista

class Alquimista:
    def __init__(self, life, strength, energy, intelligence, noisy, abilities, equipment, weapons, consumables):
        self.life = 60
        self.strength = 10
        self.energy = 120
        self.intelligence = 60
        self.noisy = False

        self.Habilidade1 = "Esquivar"
        self.Habilidade2 = "Atacar"
        self.Habilidade3 = "UsarPocao"
        self.Habilidade4 = "FabricarPocao"

        self.equipment = {'Cabeça': 'null', 'Tronco': 'Vestes de Alquimista', 'Mãos': 'null', 'Pernas': 'Calças de Tecido'}
        self.weapons = {'Mão Direita': 'Punhal', 'Mão Esquerda': 'Consumivel(x)'}
        self.consumables = {'Poção de Vida': 1, 'Frasco de Veneno': 1, 'Frasco Explosivo': 1}
        self.inventory = []

# Classe Mendigo

class Mendigo:
    def __init__(self, life, strength, energy, intelligence, noisy, abilities, equipment, weapons):
        self.life = 10
        self.strength = 10
        self.energy = 20
        self.intelligence = 10
        self.noisy = False

        self.Habilidade1 = "Esquivar"
        self.Habilidade2 = "Atacar"
        self.Habilidade3 = "AskForMercy"
        self.Habilidade4 = "Camuflar"

        self.equipment = {'Cabeça': 'null', 'Tronco': 'null', 'Mãos': 'null', 'Pernas': 'Velhos Trapos Sujos'}
        self.weapons = {'Mão Direita': 'Pau Partido', 'Mão Esquerda': 'null'}
        self.inventory = []
   


# Mapa de classes:descrições

Classes_Descricoes = {
    'Soldado': "Um Soldado radiante, vestido em armadura de ferro inabalável. Efetivo em combate aproximado.",
    'Bandido': "Um bandido sombrio que prospera na escuridão. Furtivo, o combate não é o seu forte, mas vitória não é sinônimo de afronto direto.",
    'Ermita': "Um humano solitário que sobrevive na floresta isolada com a simples força dos punhos. Possivelmente louco, devido aos anos de solidão",
    'Arqueiro': "Um Arqueiro de precisão letal. Combatente intimidante em duelos à distância, mas capaz de se defender ao corpo-a-corpo.",
    'Alquimista': "Um Alquimista que domina as artes místicas. Um mestre das poções e preparações arcanas. Particularmente culto e informado.",
    'Mendigo': "Um Mendigo sem nome. Uma alma destituída pela vida, sem nada a perder. Fraco e frágil, por vezes desejante de nunca ter existido."
}





# ================================================================================================================*/


# ============================ HABILIDADES ============================

import random  # Import the random module to generate random numbers
#ver o que é isto do import random


# ESQUIVAR 

def Esquivar():
    global PlayerClass, GettingAttacked, AttackPower, PlayerArmor  # Ensure these variables are defined elsewhere

    if PlayerClass.Energia >= 10:
        PlayerClass.Energia -= 10
        numeroAleatorio = random.randint(0, 2)

        if numeroAleatorio == 1 or numeroAleatorio == 2:
            sucesso = True
        else:
            sucesso = False

    if not sucesso:
        if GettingAttacked:
            PlayerClass.Vida -= (AttackPower - PlayerArmor)

    if sucesso:
        PlayerClass.Vida = PlayerClass.Vida



# ATACAR

def Atacar():
    global PlayerClass, Mendigo, Oponente, DanoDaArma  # Ensure these variables are defined elsewhere

    if PlayerClass.Energia >= 10:
        PlayerClass.Energia -= 10

    if PlayerClass == Mendigo:
        numeroAleatorio = random.randint(0, 4)
        if numeroAleatorio != 0:
            sucesso = False
        else:
            sucesso = True
    else:
        numeroAleatorio = random.randint(0, 2)
        if numeroAleatorio == 0:
            sucesso = False
        else:
            sucesso = True

    if not sucesso:
        Oponente.Vida = Oponente.Vida
    else:
        if PlayerClass != Ermita:
            Oponente.Vida -= (DanoDaArma * (PlayerClass.Forca / 3))
        else:
            Oponente.Vida -= PlayerClass.Forca

        

# BLOQUEAR (Exclusivo Soldado)

def Bloquear():
    global PlayerClass, Oponente, PlayerArmor  # Ensure these variables are defined elsewhere

    UnblockedDamage = Oponente.AttackPower - PlayerClass.Energia

    if UnblockedDamage > 0:
        PlayerClass.Vida -= UnblockedDamage / PlayerArmor
    else:
        PlayerClass.Vida = PlayerClass.Vida

    if Oponente.AttackPower >= PlayerClass.Energia:
        PlayerClass.Energia = 0
    else:
        PlayerClass.Energia -= Oponente.AttackPower





# FRONTKICK (Exclusivo Soldado)

def FrontKick():
    global Oponente  # Ensure the Oponente variable is defined elsewhere

    if Oponente.Bloquear:
        Oponente.Bloquear = False
        Oponente.Energia = 0

    if Oponente.SitioPrecario:
        Oponente.Vida = 0





# ROUBAR (Exclusivo Bandido)

def Roubar():
    global PlayerClass, objetoInteragivel  # Ensure these variables are defined elsewhere

    if objetoInteragivel:
        PlayerClass.Inventario.append(objetoInteragivel)




# BACKSTAB (Exclusivo Bandido)

def BackStab():
    global PlayerClass, Oponente  # Ensure these variables are defined elsewhere

    if PlayerClass.Camuflado:
        if PlayerClass.Energia >= Oponente.Vida:
            PlayerClass.Energia -= Oponente.Vida
            Oponente.Vida = 0
        else:
            print("Não tens energia suficiente para usar [BackStab] neste oponente.")
    else:
        print("Tens de estar camuflado para usar [BackStab].")








# CAMUFLAR (Exclusivo Ermita)

def Camuflar():
    global PlayerClass, numeroAleatorio  # Ensure these variables are defined elsewhere

    if not PlayerClass.Camuflado:
        numeroAleatorio = random.randint(0, 4)
        if numeroAleatorio == 0:
            PlayerClass.Camuflado = False
            print("Não te conseguiste camuflar.")
        else:
            PlayerClass.Camuflado = True
            print("Conseguiste camuflar-te.")







# INTIMIDAR (Exclusivo Ermita)
def Intimidar():
    global PlayerCharacter, PlayerClass, Oponente, numeroAleatorio  # Ensure these variables are defined elsewhere

    print("Érgues-te e gritas como um animal:")
    input("Press Enter to continue...")
    print(PlayerCharacter.Nome + ": RRRRHEEEEAOOOOOOOOOO00AAAAR!!!")
    input("Press Enter to continue...")

    PlayerClass.Energia -= 20
    numeroAleatorio = random.randint(0, 1)
    if numeroAleatorio == 0:
        print("A tua tentativa de intimidar " + Oponente + " não resultou.")
    else:
        print("Intimidaste " + Oponente + " com sucesso.")
        print(Oponente + " ficou aterrorizado e fugiu!")







# DESPARAR FLECHA (Exclusivo Arqueiro)

def DespararFlecha():
    global PlayerClass, Oponente, ParteDoCorpoAtingida_Aleatoria, numeroAleatorio  # Ensure these variables are defined elsewhere

    print("Armas o teu arco com uma flecha e disparas:")
    input("Press Enter to continue...")

    PlayerClass.Energia -= 20
    numeroAleatorio = random.randint(0, 9)
    if numeroAleatorio == 0:
        print("Falhaste o teu tiro. A flecha passou ao lado de " + Oponente + ".")
    else:
        ParteDoCorpoAtingida_Aleatoria = random.choice([0, 1, 3, 4])
        if ParteDoCorpoAtingida_Aleatoria == 0:
            Oponente.Vida = 0
            print("A flecha atingiu a cabeça de " + Oponente + ".")
            input("Press Enter to continue...")
            print(Oponente + " morreu.")
        elif ParteDoCorpoAtingida_Aleatoria == 1:
            Oponente.Vida -= 30
            print("A flecha atingiu a barriga de " + Oponente + ".")
            input("Press Enter to continue...")
        elif ParteDoCorpoAtingida_Aleatoria == 3:
            Oponente.Vida -= 20
            print("A flecha atingiu o braço de " + Oponente + ".")
        elif ParteDoCorpoAtingida_Aleatoria == 4:
            Oponente.Vida -= 20
            input("Press Enter to continue...")
            print("A flecha atingiu o joelho de " + Oponente + ".")
            print("EASTER EGG: An Arrow to the Knee!")
            input("Press Enter to continue...")

    if Oponente.Vida <= 0:
        print(Oponente + " morreu!")
    else:
        print("sofreu dano mas continua vivo!")


print("SUCESSO. FICHEIRO <<CLASSES>> IMPORTADO")







