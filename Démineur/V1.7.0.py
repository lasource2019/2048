from tkinter import *
from random import *

class Case:

#On définit un objet avec des attributs comme un abscisse, une ordonné, un type(Bombe ou pas) et un numéro. On peut noter que l'absisse et l'ordonne sont maintenant inutile mais nous avons décidé de les laisser pour essayer de vous montrer la démarche que nous avons suivi.  

    def __init__(self, compteur, abse, Ord, Type):
   
        self.abse = abse
        self.ord = Ord 
        self.type = Type
        self.stat = print("Coordonnée(",abse,";",Ord,"), Type : ",self.type,  "id : ", compteur)
        self.compteur = compteur

def ChangerUneBombe(Compteur):

#Cette fonction permet de changer le type d'une case d'une case. Utile pour faire des tests !

    Bse_donnee[Compteur].type = "Bombe"
    Bse_Case[Compteur].config(text=Bse_donnee[Compteur].type)
    Bse_Bombe.insert(0, Compteur)
    


def SETBOMBE(nombredebombes):
    
#Fonction plaçant les bombes dans la grille
#La liste d'interdits est une liste contenant les cases où les bombes ont déjà été placées, pour éviter de les superposer
    
    ListeInterdits = [100]*nombredebombes
    for loop in range(nombredebombes):
        x = randint(0,99)
        while x in ListeInterdits:
            print("Bombe répétée:", x)
            x = randint(0,99)
        Bse_donnee[x].type = "Bombe"
        Bse_Case[x].config(image = ImageBombe)
        Bse_Bombe[loop] = x
        ListeInterdits[loop] = x


LINEUP = [1,2,3,4,5,6,7,8]
LINELEFT = [10,20,30,40,50,60,70,80]
LINERIGHT = [19,29,39,49,59,69,79,89]
LINEDOWN = [91,92,93,94,95,96,97,98]
CORNERRIGHTU = 9
CORNERLEFTU = 0
CORNERRIGHTD = 99
CORNERLEFTD = 90      

def ActualiserUneCaseAutourDUneBombe(NumeroCase, NombreAAjouter):

#Fonction servant plusieurs fois dans les fonctions suivantes
#Pour chaque case ayant une bombe, cette fonction ajoute "+1" aux cases adjacentes (pour la valeur du nombre de bombes adjacentes)
    
    if Bse_donnee[NumeroCase+NombreAAjouter].type != "Bombe":
        Bse_donnee[NumeroCase+NombreAAjouter].type += 1

#Les fonctions suivantes traient à part les cas des bords du tableau

def lineUp(numero, case):
    if case in LINEUP:
        ActualiserUneCaseAutourDUneBombe(case,+10)
        ActualiserUneCaseAutourDUneBombe(case,+1)
        ActualiserUneCaseAutourDUneBombe(case,-1)
        ActualiserUneCaseAutourDUneBombe(case,+11)
        ActualiserUneCaseAutourDUneBombe(case,+9)
           
def columnRight(numero, case):
    if case in LINERIGHT:
        ActualiserUneCaseAutourDUneBombe(case,-1)
        ActualiserUneCaseAutourDUneBombe(case,+10)
        ActualiserUneCaseAutourDUneBombe(case,-10)
        ActualiserUneCaseAutourDUneBombe(case,+9)
        ActualiserUneCaseAutourDUneBombe(case,-11)

def columnLeft(numero, case):
    if case in LINELEFT:
        ActualiserUneCaseAutourDUneBombe(case,+1)
        ActualiserUneCaseAutourDUneBombe(case,+10)
        ActualiserUneCaseAutourDUneBombe(case,-10)
        ActualiserUneCaseAutourDUneBombe(case,+11)
        ActualiserUneCaseAutourDUneBombe(case,-9)
        
def lineDown(numero, case):
    if case in LINEDOWN:
        ActualiserUneCaseAutourDUneBombe(case,-10)
        ActualiserUneCaseAutourDUneBombe(case,+1)
        ActualiserUneCaseAutourDUneBombe(case,-1)
        ActualiserUneCaseAutourDUneBombe(case,-11)
        ActualiserUneCaseAutourDUneBombe(case,-9)
        
def cornerRightU(numero, case):
    if case == CORNERRIGHTU:
        ActualiserUneCaseAutourDUneBombe(case,-1)
        ActualiserUneCaseAutourDUneBombe(case,+9)
        ActualiserUneCaseAutourDUneBombe(case,+10)
        
def cornerLeftU(numero, case):
    if case == CORNERLEFTU:
        ActualiserUneCaseAutourDUneBombe(case,+1)
        ActualiserUneCaseAutourDUneBombe(case,+10)
        ActualiserUneCaseAutourDUneBombe(case,+11)
        
def cornerRightD(numero, case):
    if case == CORNERRIGHTD:
        ActualiserUneCaseAutourDUneBombe(case,-1)
        ActualiserUneCaseAutourDUneBombe(case,-10)
        ActualiserUneCaseAutourDUneBombe(case,-11)
        
def cornerLeftD(numero, case):
    if case == CORNERLEFTD:
        ActualiserUneCaseAutourDUneBombe(case,+1)
        ActualiserUneCaseAutourDUneBombe(case,-9)
        ActualiserUneCaseAutourDUneBombe(case,-10)
        
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
            ActualiserUneCaseAutourDUneBombe(Bombe,+10)
            ActualiserUneCaseAutourDUneBombe(Bombe,-10)
            ActualiserUneCaseAutourDUneBombe(Bombe,-11)
            ActualiserUneCaseAutourDUneBombe(Bombe,+11)
            ActualiserUneCaseAutourDUneBombe(Bombe,-9)
            ActualiserUneCaseAutourDUneBombe(Bombe,+9)
            
def ActualiseAll():
    
#Fonction actualisant les cases
    
    for loop in range(100):
        Bse_Case[loop].config(text=Bse_donnee[loop].type)
       
def PhotosNbBombes():

#Affiche les images pour le nombre de bombes adjacentes
    
    for Compteur in range(100):
        for n in range(9):
            if Bse_donnee[Compteur].type == n:
                Bse_Case[Compteur].config(image = ImagesNuméros[n])


#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------

TableauDemineur = Tk()
TableauDemineur.title("Démineur - Aristide, Matéo et Raphaël - ISN 2018-2019")
NBBOMBES = 20 
Bse_donnee = [0]*100
Bse_Case = [0]*100
Bse_Bombe = [0]*NBBOMBES
#Création des images
ImageBombe = PhotoImage(file="ImageBombe.png")
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
for ligne in range(10):
    for colonne in range(10):
         
        Bse_donnee[Compteur] = Case(Compteur, colonne, ligne, 0)
        Bse_Case[Compteur] = Button(TableauDemineur)
        Bse_Case[Compteur].grid(row=ligne, column=colonne)
        Compteur += 1
    
SETBOMBE(NBBOMBES)
DetectBombe()
PhotosNbBombes()