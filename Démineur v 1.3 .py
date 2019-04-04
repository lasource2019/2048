from tkinter import *
from random import *
Bse_Bombe = [0]*20
class Case:    
    def __init__(self, compteur, abse, Ord, Type):
   
        self.abse = abse
        self.ord = Ord 
        self.type = Type
        self.stat = print("Coordonnée(",abse,";",Ord,"), Type : ",self.type,  "id : ", compteur)
        self.compteur = compteur
        
        
        
'''
On définit un objet avec des attributs comme un abscisse, une ordonné, un type(Bombe ou pas) et un numéro.

On peut noter que l'absisse et l'ordonne sont maintenant inutile mais nous avons décidé de les laisser pour essayer de vous montrer la démarche que nous avons suivi.*/        
        

'''   
       
LINEUP = [1,2,3,4,5,6,7,8]
LINELEFT = [10,20,30,40,50,60,70,80]
LINERIGHT = [19,29,39,49,59,69,79,89]
LINEDOWN = [91,92,93,94,95,96,97,98]
CORNERRIGHTU = 9
CORNERLEFTU = 0
CORNERRIGHTD = 99
CORNERLEFT = 90

    

           
        

def actualise(x):
    Bse_donnee[x].type = "Bombe"
    Bse_Case[x].config(text=Bse_donnee[x].type)
'''
Cette fonction permet de changer le type d'une case d'une case.
Utile pour faire des tests !
'''
def SETBOMBE():
    numero = 0
    for loop in range(20):
        x = randint(0,99)
        Bse_donnee[x].type = "Bombe"
        Bse_Case[x].config(text=Bse_donnee[x].type)
        Bse_Bombe[numero] = x
        numero += 1
'''Fonction finale permettant de générer des bombes sans problèmes '''

def recherche_dichotomique( element, liste_triee ):
    global Recherche
    Recherche = ""
    a = 0
    b = len(liste_triee)-1
    m = (a+b)//2
    while a < b :
        if liste_triee[m] == element :
            
            Recherche = True
            return m
        
        elif liste_triee[m] > element :
            b = m-1
        else :
            a = m+1
        m = (a+b)//2
    return a       
'''Fonction pour vérifier qu'un élément soit dans une liste'''

        

def detectonecase(case, nubertoadd):
    IgnoreCase = [0,1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,19,29,39,49,59,69,79,89,91,92,93,94,95,96,97,98,99]
    recherche_dichotomique(case, IgnoreCase)
    if Recherche == True:
        pass
    
    elif Bse_donnee[case+nubertoadd].type == "Bombe":
        pass
    else:
        Bse_donnee[case+nubertoadd].type += 1
'''fonction :
        
        - cherchant si le numéro de Bombe est dans les cases à ne pas traiter
        - Si c'est le cas elle fait une sorte de break.
        - Sinon elle va ajouter 1 au type de la case + X
        - X étant nubertoadd avec un faute d'orthographe.
'''

def lineUp(numero, case):
    if (Bse_donnee[numero].compteur==1) or (Bse_donnee[numero].compteur==2) or (Bse_donnee[numero].compteur==3) or (Bse_donnee[numero].compteur==4) or (Bse_donnee[numero].compteur==5) or (Bse_donnee[numero].compteur==6) or (Bse_donnee[numero].compteur==7) or (Bse_donnee[numero].compteur==8):
        detectonecase(case,+10)
        detectonecase(case,+1)
        detectonecase(case,-1)
        detectonecase(case,+11)
        detectonecase(case,+9)
'''Detecte les bombes sur la ligne du haut,mais ne traite pas les coins'''

'''Listes à ignorer car lineUp, et d'autre fonctions le font déjà'''
           
def columnRight(numero, case):
    if (Bse_donnee[numero].compteur==19) or (Bse_donnee[numero].compteur==29) or (Bse_donnee[numero].compteur==39) or (Bse_donnee[numero].compteur==49) or (Bse_donnee[numero].compteur==59) or (Bse_donnee[numero].compteur==69) or (Bse_donnee[numero].compteur==79) or (Bse_donnee[numero].compteur==89):


        detectonecase(case,-1)
        detectonecase(case,+10)
        detectonecase(case,-10)
        detectonecase(case,+9)
        detectonecase(case,-9)

def columnLeft(numero, case):
    if (Bse_donnee[numero].compteur==10) or (Bse_donnee[numero].compteur==20) or (Bse_donnee[numero].compteur==30) or (Bse_donnee[numero].compteur==40) or (Bse_donnee[numero].compteur==50) or (Bse_donnee[numero].compteur==60) or (Bse_donnee[numero].compteur==70) or (Bse_donnee[numero].compteur==80):
    

        detectonecase(case,+1)
        detectonecase(case,+10)
        detectonecase(case,-10)
        detectonecase(case,+11)
        detectonecase(case,-11)
def lineDown(numero, case):
    if (Bse_donnee[numero].compteur==91) or (Bse_donnee[numero].compteur==92) or (Bse_donnee[numero].compteur==93) or (Bse_donnee[numero].compteur==94) or (Bse_donnee[numero].compteur==95) or (Bse_donnee[numero].compteur==96) or (Bse_donnee[numero].compteur==97) or (Bse_donnee[numero].compteur==98):
        detectonecase(case,-10)
        detectonecase(case,+1)
        detectonecase(case,-1)
        detectonecase(case,-11)
        detectonecase(case,-9)
def cornerRightU(numero, case):
    if Bse_donnee[numero].compteur == 9:
        detectonecase(case,+1)
        detectonecase(case,+10)
        detectonecase(case,+11)
def cornerLeftU(numero, case):
    if Bse_donnee[numero].compteur == 0:
        detectonecase(case,-1)
        detectonecase(case,+10)
        detectonecase(case,+9)
def cornerRightD(numero, case):
    if Bse_donnee[numero].compteur == 99:
        detectonecase(case,-1)
        detectonecase(case,-10)
        detectonecase(case,-11)
def cornerLeftD(numero, case):
    if Bse_donnee[numero].compteur == 90:
            
        detectonecase(case,+1)
        detectonecase(case,+10)
        detectonecase(case,+11)
        
def DetectBombe():
    
    for loop in range(20):
        case = Bse_Bombe[loop]
        if recherche_dichotomique(Bse_Bombe[loop], LINEDOWN) == True:
            lineDown(loop,case)
        elif recherche_dichotomique(Bse_Bombe[loop], LINEUP) == True:
            lineUp(loop,case)
        elif recherche_dichotomique(Bse_Bombe[loop], LINERIGHT) == True:
            columnRight(loop,case)
        elif recherche_dichotomique(Bse_Bombe[loop], LINELEFT) == True:
            columnLeft(loop,case)
        elif Case == 9:
            cornerRightU(loop, case)
        elif Case == 90:
            cornerLeftD(loop, case)
        elif Case == 99:
            cornerRightD(loop, case)
        elif Case == 0:
            cornerLeftU(loop, case)
        else:
            detectonecase(case,+1)
            detectonecase(case,-1)
            detectonecase(case,+10)
            detectonecase(case,-10)
            detectonecase(case,-11)
            detectonecase(case,+11)
            detectonecase(case,-9)
            detectonecase(case,+9)
'''fonction détectant les bombes'''           
             
Bse_donnee = [0]*100
Bse_Case = [0]*100
Compteur = 0

fenetre = Tk()        

for ligne in range(10):
    for colonne in range(10):
         
        Bse_donnee[Compteur] = Case(Compteur, colonne, ligne, 0)
        Bse_Case[Compteur] = Button(fenetre, width=8, height=4, text=Bse_donnee[Compteur].type)
        Bse_Case[Compteur].grid(row=ligne, column=colonne)
                
        Compteur += 1
SETBOMBE()

def ActualiseAll():    
    for abkzbdkq in range(100):
        Bse_Case[abkzbdkq].config(text=Bse_donnee[abkzbdkq].type)
'''fonction mettant les cases à jour'''

ActualiseAll()