from tkinter import *
from tkinter.messagebox import *
from random import *

class Case:

#On définit un objet avec des attributs comme un abscisse, une ordonné, un type(Bombe ou pas) et un numéro. On peut noter que l'absisse et l'ordonne sont maintenant inutile mais nous avons décidé de les laisser pour essayer de vous montrer la démarche que nous avons suivi.  

    def __init__(self, compteur, abse, Ord, Type):
   
        self.abse = abse
        self.ord = Ord 
        self.type = Type
        self.compteur = compteur
    


def SETBOMBE(nombredebombes):
    
#Fonction plaçant les bombes dans la grille
#La liste d'interdits est une liste contenant les cases où les bombes ont déjà été placées, pour éviter de les superposer
    

    for loop in range(nombredebombes):
        x = randint(0,((LargeurGrille*LargeurGrille) - 1))
        while x in Bse_Bombe:
            print("Bombe répétée:", x)
            x = randint(0,((LargeurGrille*LargeurGrille) - 1))
        Bse_donnee[x].type = "Bombe"
        Bse_Bombe.append(x)

def ActualiserUneCaseAutourDUneBombe(NumeroCase, NombreAAjouter):

#Fonction servant plusieurs fois dans les fonctions suivantes
#Pour chaque case ayant une bombe, cette fonction ajoute "+1" aux cases adjacentes (pour la valeur du nombre de bombes adjacentes)
#Sert aussi dans le bouton de triche
    
    if Bse_donnee[NumeroCase+NombreAAjouter].type != "Bombe":
        Bse_donnee[NumeroCase+NombreAAjouter].type += 1
        

#Les fonctions suivantes traient à part les cas des bords du tableau

def lineUp(numero, case):
    if case in LINEUP:
        ActualiserUneCaseAutourDUneBombe(case,+LargeurGrille)
        ActualiserUneCaseAutourDUneBombe(case,+1)
        ActualiserUneCaseAutourDUneBombe(case,-1)
        ActualiserUneCaseAutourDUneBombe(case,+LargeurGrille+1)
        ActualiserUneCaseAutourDUneBombe(case,+LargeurGrille-1)
           
def columnRight(numero, case):
    if case in LINERIGHT:
        ActualiserUneCaseAutourDUneBombe(case,-1)
        ActualiserUneCaseAutourDUneBombe(case,+LargeurGrille)
        ActualiserUneCaseAutourDUneBombe(case,-LargeurGrille)
        ActualiserUneCaseAutourDUneBombe(case,+LargeurGrille-1)
        ActualiserUneCaseAutourDUneBombe(case,-LargeurGrille-1)

def columnLeft(numero, case):
    if case in LINELEFT:
        ActualiserUneCaseAutourDUneBombe(case,+1)
        ActualiserUneCaseAutourDUneBombe(case,+LargeurGrille)
        ActualiserUneCaseAutourDUneBombe(case,-LargeurGrille)
        ActualiserUneCaseAutourDUneBombe(case,+LargeurGrille+1)
        ActualiserUneCaseAutourDUneBombe(case,-LargeurGrille+1)
        
def lineDown(numero, case):
    if case in LINEDOWN:
        ActualiserUneCaseAutourDUneBombe(case,-LargeurGrille)
        ActualiserUneCaseAutourDUneBombe(case,+1)
        ActualiserUneCaseAutourDUneBombe(case,-1)
        ActualiserUneCaseAutourDUneBombe(case,-LargeurGrille-1)
        ActualiserUneCaseAutourDUneBombe(case,-LargeurGrille+1)
        
def cornerRightU(numero, case):
    if case == CORNERRIGHTU:
        ActualiserUneCaseAutourDUneBombe(case,-1)
        ActualiserUneCaseAutourDUneBombe(case,+LargeurGrille-1)
        ActualiserUneCaseAutourDUneBombe(case,+LargeurGrille)
        
def cornerLeftU(numero, case):
    if case == CORNERLEFTU:
        ActualiserUneCaseAutourDUneBombe(case,+1)
        ActualiserUneCaseAutourDUneBombe(case,+LargeurGrille)
        ActualiserUneCaseAutourDUneBombe(case,+LargeurGrille+1)
        
def cornerRightD(numero, case):
    if case == CORNERRIGHTD:
        ActualiserUneCaseAutourDUneBombe(case,-1)
        ActualiserUneCaseAutourDUneBombe(case,-LargeurGrille)
        ActualiserUneCaseAutourDUneBombe(case,-LargeurGrille-1)
        
def cornerLeftD(numero, case):
    if case == CORNERLEFTD:
        ActualiserUneCaseAutourDUneBombe(case,+1)
        ActualiserUneCaseAutourDUneBombe(case,-LargeurGrille+1)
        ActualiserUneCaseAutourDUneBombe(case,-LargeurGrille)
        
def DetectBombe():
    
#Fonction déterminant le nombre de bombes adjacentes (en appelant les fonctions précédentes)
    
    global NBBOMBES
    
    for loop in range(NBBOMBES):
        
        Bombe = Bse_Bombe[loop]
        
        if Bse_Bombe[loop] in LINEDOWN:
            lineDown(loop, Bombe)
        elif Bse_Bombe[loop] in LINEUP:
            lineUp(loop, Bombe)
        elif Bse_Bombe[loop] in LINERIGHT:
            columnRight(loop,Bombe)
        elif Bse_Bombe[loop] in LINELEFT:
            columnLeft(loop,Bombe)
        elif Bse_Bombe[loop] == CORNERRIGHTU:
            cornerRightU(loop, Bombe)
        elif Bse_Bombe[loop] == CORNERLEFTD:
            cornerLeftD(loop,Bombe)
        elif Bse_Bombe[loop] == CORNERRIGHTD:
            cornerRightD(loop,Bombe)
        elif Bse_Bombe[loop] == CORNERLEFTU:
            cornerLeftU(loop,Bombe)
        else:
            ActualiserUneCaseAutourDUneBombe(Bombe,+1)
            ActualiserUneCaseAutourDUneBombe(Bombe,-1)
            ActualiserUneCaseAutourDUneBombe(Bombe,+LargeurGrille)
            ActualiserUneCaseAutourDUneBombe(Bombe,-LargeurGrille)
            ActualiserUneCaseAutourDUneBombe(Bombe,-LargeurGrille-1)
            ActualiserUneCaseAutourDUneBombe(Bombe,+LargeurGrille+1)
            ActualiserUneCaseAutourDUneBombe(Bombe,-LargeurGrille+1)
            ActualiserUneCaseAutourDUneBombe(Bombe,+LargeurGrille-1)
            
def ActualiseAll():
    
#Fonction actualisant les cases
    
    for loop in range(LargeurGrille*LargeurGrille):
        Bse_Case[loop].config(text=Bse_donnee[loop].type)
       
def ClicCase(x):
    
#Fonction réalisant une action lorsque l'on clique sur une case
    global CasesRévélées
    if ValeurDrapeau == 0:
        
    #Cas où la pose de drapeau est désactivée, donc lorsque l'on veut dévoiler une case     

        if Bse_Case_Drapeau[x] == 0:
            
        #Cas où il n'y a pas de drapeau posé sur la case    
            NbBombesAdjacentesPossibles = 0
            if Bse_donnee[x].type == "Bombe":
                for k in range(LargeurGrille*LargeurGrille):
                    if k in Bse_Bombe:
                        if Bse_Case_Drapeau[k] == 1:
                            Bse_Case[k].config(image = ImageDrapeauVrai, state = "disabled")
                        else:
                            Bse_Case[k].config(image = ImageBombe, state = "disabled")
                    if Bse_Case_Drapeau[k] == 1:
                        if k not in Bse_Bombe:
                            Bse_Case[k].config(image = ImageDrapeauFaux, state = "disabled")
                Bse_Case[x].config(image = ImageBombeFaux, state = "disabled")
                Perdu = showwarning("Fin du game", message = "Vous avez perdu", default = "ok")
            else:
                while NbBombesAdjacentesPossibles != Bse_donnee[x].type:
                    NbBombesAdjacentesPossibles += 1
                Bse_Case[x].config(image = ImagesNuméros[NbBombesAdjacentesPossibles], state = "disabled")
                CasesRévélées += 1
    
    if ValeurDrapeau == 1:
        if Bse_Case_Drapeau[x] == 0:
            Bse_Case[x].config(image = ImageDrapeau)
            Bse_Case_Drapeau[x] = 1
        elif Bse_Case_Drapeau[x] ==1:
            Bse_Case[x].config(image = ImageBlanc)
            Bse_Case_Drapeau[x] = 0
            
    
    if CasesRévélées + NBBOMBES == LargeurGrille*LargeurGrille:
        for k in range(LargeurGrille*LargeurGrille):
            if Bse_Case_Drapeau[k] == 1:
                    Bse_Case[k].config(image = ImageDrapeauVrai, state = "disabled")
        Gagné = showinfo("Fin du game", message = "Vous avez gagné", default = "ok")

def ClicDrapeau():
    
#Fonction permettant d'activer/désactiver la pose de drapeau
    
    global ValeurDrapeau
    if ValeurDrapeau == 0:
        IndicateurDrapeau.config(image = ImageVert)
        ValeurDrapeau = 1
    else:
        IndicateurDrapeau.config(image = ImageRouge)
        ValeurDrapeau = 0      

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
TableauDémineur = Tk()
TableauDémineur.title("Démineur - Aristide, Matéo et Raphaël - ISN 2018-2019")

#Largeur de la grille
LargeurGrille = 14

#Nombre de Bombes sur la grille
NBBOMBES = 20

#Bse_donne contient les informations des cases
Bse_donnee = [0]*LargeurGrille*LargeurGrille

#Bse_Case contient les boutons (cases)
Bse_Case = [0]*LargeurGrille*LargeurGrille

#Bse_Bombe contient les numéros des cases où les bombes sont situées
Bse_Bombe = []*NBBOMBES

#Bse_Case_Drapeau contient l'information de la présence d'un drapeau ou non sur une case
Bse_Case_Drapeau = [0]*LargeurGrille*LargeurGrille

#Nombre de cases révélées (pour savoir où l'on en est dans la partie
CasesRévélées = 0

#Si la valeur du drapeau est 0, alors le drapeau n'est pas activé (Rouge). Si c'est 0, alors il est activé (Vert).

ValeurDrapeau = 0


#Listes endroits spécifiques (côtés et coins)
LINEUP = []
for k in range(LargeurGrille - 2):
    LINEUP.append(1 + k)
    
LINELEFT = []
for k in range(LargeurGrille - 2):
    LINELEFT.append((LargeurGrille * k) + LargeurGrille)
    
LINERIGHT = []
for k in range(LargeurGrille - 2):
    LINERIGHT.append((LargeurGrille * k) + ((LargeurGrille*2) - 1))
    
LINEDOWN = []
for k in range(LargeurGrille - 2):
    LINEDOWN.append((LargeurGrille * LargeurGrille) - LargeurGrille + 1 + k)

CORNERRIGHTU = LargeurGrille - 1
CORNERLEFTU = 0
CORNERRIGHTD = (LargeurGrille * LargeurGrille) - 1
CORNERLEFTD = (LargeurGrille * LargeurGrille) - LargeurGrille

#Création des images

ImageBlanc = PhotoImage(file="ImageBlanc.png")
ImageDrapeau = PhotoImage(file="ImageDrapeau.png")
ImageDrapeauVrai = PhotoImage(file="ImageDrapeauVrai.png")
ImageDrapeauFaux = PhotoImage(file="ImageDrapeauFaux.png")
ImageVert = PhotoImage(file="Vert.png")
ImageRouge = PhotoImage(file="Rouge.png")
ImageBombe = PhotoImage(file="ImageBombe.png")
ImageBombeFaux = PhotoImage(file="ImageBombeFaux.png")
ImagesNuméros = [0]*9
ImagesNuméros[0] = PhotoImage(file="Pic0.png")
ImagesNuméros[1] = PhotoImage(file="Pic1.png")
ImagesNuméros[2] = PhotoImage(file="Pic2.png")
ImagesNuméros[3] = PhotoImage(file="Pic3.png")
ImagesNuméros[4] = PhotoImage(file="Pic4.png")
ImagesNuméros[5] = PhotoImage(file="Pic5.png")
ImagesNuméros[6] = PhotoImage(file="Pic6.png")
ImagesNuméros[7] = PhotoImage(file="Pic7.png")
ImagesNuméros[8] = PhotoImage(file="Pic8.png")   

#Génération du tableau
Compteur = 0

for ligne in range(LargeurGrille):
    for colonne in range(LargeurGrille):
         
        Bse_donnee[Compteur] = Case(Compteur, colonne, ligne, 0)
        Bse_Case[Compteur] = Button(TableauDémineur, image = ImageBlanc, state = "active", command = lambda Compteur=Compteur:ClicCase(Bse_donnee[Compteur].compteur))
        Bse_Case[Compteur].grid(row=ligne, column=colonne)
        Compteur += 1

SETBOMBE(NBBOMBES)
DetectBombe()

#Génération du menu latéral droit

BoutonDrapeau = Button(TableauDémineur, image = ImageDrapeau, command = ClicDrapeau)
BoutonDrapeau.grid(row = 1, column = LargeurGrille)
IndicateurDrapeau = Label(TableauDémineur, image = ImageRouge)
IndicateurDrapeau.grid(row = 1, column = LargeurGrille + 1)