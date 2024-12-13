"""
Lucas B. Tinkler
Gr: 401
améloration des personnages D&D
"""
from random import randint
from enum import Enum
from dataclasses import dataclass


def roule_de(faces_de):
    de = randint(1, faces_de)
    return de


def roll_of_the_dices(nbr_de):
    resultat_de = []
    for i in range(nbr_de):
        de = roule_de(6)
        resultat_de.append(de)
    resultat_de.remove(min(resultat_de))
    valeur = sum(resultat_de)
    return valeur


class Alignement(Enum):
    NON_DEFINI = 0
    LAWFUL_GOOD = 1
    NEUTRAL_GOOD = 2
    CHAOTIC_GOOD = 3
    LAWFUL_NEUTRAL = 4
    TRUE_NEUTRAL = 5
    CHAOTIC_NEUTRAL = 6
    LAWFUL_EVIL = 7
    NEUTRAL_EVIL = 8
    CHAOTIC_EVIL = 9


class NPC:
    def __init__(self, nom, race, espece, proffession):
        self.force = roll_of_the_dices(4)
        self.agilite = roll_of_the_dices(4)
        self.sagesse = roll_of_the_dices(4)
        self.charisme = roll_of_the_dices(4)
        self.intelligence = roll_of_the_dices(4)
        self.constitution = roll_of_the_dices(4)
        self.ac = randint(1, 12)
        self.nom = nom
        self.race = race
        self.espece = espece
        self.pv = randint(1, 20)
        self.proffession = proffession
        self.alignement = Alignement(roule_de(10) - 1)

    def afficher_characteristiques(self):
        print(f"\nNom: {self.nom}\nRace: {self.race}\nEspèce: {self.espece}\nProffession: {self.proffession}\n{self.alignement}\nPoints de vie: {self.pv}\nClasse d'armure: {self.ac}\nForce: {self.force}\nagilite: {self.agilite}\nsagesse: {self.sagesse}\ncharisme: {self.charisme}\nintelligence: {self.intelligence}\nconstitution: {self.constitution}")

    def verifier_vie(self):
        if self.pv > 0:
            print("vivant")
        else:
            print("mort")


class Kobold(NPC):
    def __init__(self):
        super().__init__("Ken", "kobold", "kobold", "bard")
        self.result_dice20 = roule_de(20)
        self.result_dice8 = roule_de(8)
        self.result_dice6 = roule_de(6)

    def attaquer(self, cible):
        self.cible = cible
        if self.result_dice20 == 20:
            print(f"\nle Kobold a roulé un 20! L'ennemi reçoit {self.result_dice8} dégat")
            self.cible.pv -= self.result_dice8
        elif self.result_dice20 == 1:
            print("\nL'attaque du Kobold a raté lamentablement")
        else:
            if self.result_dice20 >= self.cible.ac:
                print(f"\nle Kobold a roulé un {self.result_dice20}. Il fait {self.result_dice6} dégat")
                self.cible.pv -= self.result_dice6
            else:
                print(f"\nL'attaque du Kobold a raté, il a roulé un {self.result_dice20}")

        print(f"la vie de l'ennemi est de: {self.cible.pv} pv")

    def subir_dommage(self, qtte_dmg):
        self.qtte_dmg = qtte_dmg
        self.pv -= self.qtte_dmg
        print(f"\nle kobold reçois {self.qtte_dmg} dégats\nle kobold a {self.pv} pv")


class Hero(NPC):
    def __init__(self):
        super().__init__("Oppenheimer", "arakocra", "Rainbowplum", "artificier")
        self.result_dice20 = roule_de(20)
        self.result_dice8 = roule_de(8)
        self.result_dice6 = roule_de(6)

    def attaquer(self, cible):
        self.cible = cible
        if self.result_dice20 == 20:
            print(f"Oppenheimer a roulé un 20! L'ennemi reçoit {self.result_dice8} dégat")
            self.cible.pv -= self.result_dice8
        elif self.result_dice20 == 1:
            print("L'attaque de Oppenheimer a raté lamentablement")
        else:
            if self.result_dice20 >= self.cible.ac:
                print(f"Oppenheimer a roulé un {self.result_dice20}. Il fait {self.result_dice6} dégat")
                self.cible.pv -= self.result_dice6
            else:
                print(f"L'attaque de Oppenheimer a raté, il a roulé un {self.result_dice20}")

        print(f"la vie de l'ennemi est de: {self.cible.pv} pv")

    def subir_dommage(self, qtte_dmg):
        self.qtte_dmg = qtte_dmg
        self.pv -= self.qtte_dmg
        print(f"Oppenheimer reçois {self.qtte_dmg} dégats\nOppenheimer a {self.pv} pv")


@dataclass
class Item:
    quantite: int = 2
    nom: str = "potions"


class BackPack:
    def __init__(self):
        self.liste_items = []

    def ajouter_item(self):
        i = Item()
        self.repeat = True
        self.liste_items.append(i.quantite)
        self.liste_items.append(i.nom)
# boucle pour ajouter autant de potions que tu veux
        while self.repeat:
            print(self.liste_items)
            self.ajout = input(str("veux-tu ajouter d'autres potions Y/N? >>"))
            if self.ajout == "N":
                self.repeat = False
            if self.liste_items[0] > 0:
                self.liste_items[0] += i.quantite

    def retirer_item(self):
        print(self.liste_items)
        self.item_a_retirer = input(str("Quel item voulez-vous retirer? >>"))
        if self.liste_items[1] == self.item_a_retirer:
            print("effacage de l'item")
            self.nbr_item_effacer = input(int("Combien item voulez-vous retirer? >>"))
            self.nbr_effacer = self.nbr_item_effacer
            if self.liste_items[0] < self.nbr_item_effacer:
                print("ERROR: Le nombre d'item a retirer est plus grand que le nombre d'item")
            elif self.nbr_effacer < 0:
                print("ERROR: Ne peux pas effacer i=un nombre d'objets négatif")
        elif self.liste_items[1] != self.item_a_retirer:
            print("ERROR: L'item n'est pas dans le sac")


npc = NPC("ennemi", "méchant", "très méchant", "vilain")
npc.afficher_characteristiques()

k = Kobold()
h = Hero()
k.afficher_characteristiques()
h.afficher_characteristiques()
k.attaquer(npc)
h.attaquer(npc)
k.subir_dommage(roule_de(6))
h.subir_dommage(roule_de(6))
k.verifier_vie()
h.verifier_vie()

b = BackPack()
b.ajouter_item()
b.retirer_item()
