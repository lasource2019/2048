from tkinter import *
from tkinter.messagebox import *
from random import randint
from collections import OrderedDict
from operator import itemgetter 
class Case:

#On définit un objet avec des attributs comme un abscisse, une ordonné, un type(Bombe ou pas) et un numéro. On peut noter que l'absisse et l'ordonne sont maintenant inutile mais nous avons décidé de les laisser pour essayer de vous montrer la démarche que nous avons suivi.  

    def __init__(self, compteur, abse, Ord, Type):
   
        self.abse = abse
        self.ord = Ord 
        self.type = Type
        self.compteur = compteur
        self.etat = "caché"
        
    
def Change(Case, Type):
    Bse_donnee[Case].type = Type

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
        
def firstcase(x):
    #Foncrion révélant plusieurs cases lorsque l'on clique sur une case pour la première fois.
    global CasesRévélées
    ListeOrientation = [1,-1,10,-10,9,-9,11,-11]
    if CasesRévélées == 0:
        listeRayons = [0]*8
        
        T = ((LargeurGrille-5)//3)
        
        Compteur = x
        ListeOrientation[6]
            
        for loop in range(8):
            Rayon = randint(1, T+1)
            for pool in range(Rayon):
                if Bse_donnee[x + pool*ListeOrientation[loop]].type == "Bombe":
                    pass
                else:
                    ClicCase(x + pool*ListeOrientation[loop])
                    print("pool : ",pool)
                    print("Rayon : ",Rayon)
                    print(ListeOrientation[loop])
                    print("fin")
        
def ClicCase(x):
    print("Case cliquée : ", x)
    
    
#Fonction réalisant une action lorsque l'on clique sur une case
    global CasesRévélées
    global statut
    global Dico
    global ListeDrapeau
    print(CasesRévélées)
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
                statut = "lose"
            else:
                while NbBombesAdjacentesPossibles != Bse_donnee[x].type:
                    NbBombesAdjacentesPossibles += 1
                if Bse_donnee[x].etat == "révélée":
                    pass
                else:
                    Bse_Case[x].config(image = ImagesNuméros[NbBombesAdjacentesPossibles], state = "disabled")
                    CasesRévélées += 1
                    Bse_donnee[x].etat = "révélée"
                    ListeCasesRévélées.append(x)
                    Dico[x] = Bse_donnee[x].type #inutile, une liste fonctionne mieux.
                    if Bse_donnee[x].type == 0:
                        
                        Liste = (itemgetter(*[idx for idx,e in enumerate(list(Dico.values())) if e == 0])(list(Dico.keys())))
                    else:
                        pass
                    
                    
    
    if ValeurDrapeau == 1:
        if Bse_Case_Drapeau[x] == 0:
            Bse_Case[x].config(image = ImageDrapeau)
            Bse_Case_Drapeau[x] = 1
            Bse_donnee[x].etat == "Drapeau"
            ListeDrapeau.append(x)
        elif Bse_Case_Drapeau[x] ==1:
            Bse_Case[x].config(image = ImageBlanc)
            Bse_Case_Drapeau[x] = 0
            Bse_donnee[x].etat == "caché"
            del ListeDrapeau[ListeDrapeau.index(x)]
            
    
    if CasesRévélées + NBBOMBES == LargeurGrille*LargeurGrille:
        for k in range(LargeurGrille*LargeurGrille):
            if Bse_Case_Drapeau[k] == 1:
                    Bse_Case[k].config(image = ImageDrapeauVrai, state = "disabled")
        Gagné = showinfo("Fin du game", message = "Vous avez gagné", default = "ok")
        statut = "win"
def fonction(x):
    firstcase(x)
    ClicCase(x)
'''def TriDico():
    sorted(Dico.items(), Type=lambda t: t[1])
    DicoTrie = OrderedDict(sorted(Dico.items(), Type=lambda t: t[0]))
'''
def ClicDrapeau():
    
#Fonction permettant d'activer/désactiver la pose de drapeau
    
    global ValeurDrapeau
    if ValeurDrapeau == 0:
        IndicateurDrapeau.config(image = ImageVert)
        ValeurDrapeau = 1
    else:
        IndicateurDrapeau.config(image = ImageRouge)
        ValeurDrapeau = 0
def VerificationEtat(ValeurAAjouter):
    #On vérifie si la case est un drapeau pour éviter de cliquer dessus une nouvelle fois.
    global Numero
    global Liste
    global ListeZérosT
    print(VerificationEtat)
    print(Bse_donnee[Liste[VariableLoop]])
    if len(Liste) == 0:
        Liste = (itemgetter(*[idx for idx,e in enumerate(list(Dico.values())) if e == 0])(list(Dico.keys())))
    #Cette condition est nécéssaire car si il y a qu'une case vide de révélée alors il Liste est une variable et non une liste.            
    elif Bse_donnee[Liste[VariableLoop]] in ListeCasesRévélées:
        NombreDeZérosDévoilée -=1
    else:
        if Bse_donnee[Liste[Numero]+ValeurAAjouter].etat == "Drapeau":
            pass
        else:
            ClicCase(Liste[Numero]+ValeurAAjouter)
            Liste = (itemgetter(*[idx for idx,e in enumerate(list(Dico.values())) if e == 0])(list(Dico.keys())))
    
            


def AutomatisationResolveur(Boucle, ValeursPoss):
    global Numero
    global NombreDeZérosDévoilée
    for loop in range(Boucle):
        VerificationEtat(ValeursPoss[loop])
    NombreDeZérosDévoilée +=1
    print("NombreDeZérosDévoilée : ",NombreDeZérosDévoilée)
    Numero += 1
        
def near(case, cmd1, cmd2, cmd3, cmd4, cmd5, cmd6,cmd7 ,cmd8,cmd9):
    if case in LINEDOWN:
        cmd1
    elif case in LINEUP:
        cmd2
    elif case in LINERIGHT:
        cmd3
    elif case in LINELEFT:
        cmd4
    elif case == CORNERRIGHTU:
        cmd5
    elif case == CORNERLEFTD:
        cmd6
    elif case == CORNERRIGHTD:
        cmd7
    elif case == CORNERLEFTU:
        cmd8
    else:
        cmd9
        
            
            
    
def Resolve():
    global NombreDeZérosDévoilée
    global Liste
    global LineUp
    global ListeZerosRévélés
    loop = 0
    global NombreDeZérosTraités
    global statut
    #Etape 1: Si aucune case n'a été activé: en activer une.
    if not Dico:
        firstcase(randint(0,99))#On clique sur une case aléatoire
    else:
        VariableLoop = 0
        if not Liste:
            #On actualise la liste des valeurs cliqué. Problème : on est dans une fonction
            Liste = (itemgetter(*[idx for idx,e in enumerate(list(Dico.values())) if e == 0])(list(Dico.keys())))
        
        while NombreDeZérosDévoilée != len(Liste):
            NombreDeZérosTraités += 1
        
            
            if Liste[loop] in LINEUP:
                
                if Dico[Liste[loop]] == 0:
                    AutomatisationResolveur(5, ValeursPossibles1)
                    
                    
            elif Liste[loop] in LINEDOWN:
                if Dico[Liste[loop]] == 0:
                    AutomatisationResolveur(5, ValeursPossibles2)
                    
                    
                    
            elif Liste[loop] in LINERIGHT:
                if Dico[Liste[loop]] == 0:
                    AutomatisationResolveur(5, ValeursPossibles3)
                    #Erreur ici
            elif Liste[loop] in LINELEFT:
                if Dico[Liste[loop]] == 0:
                    AutomatisationResolveur(5, ValeursPossibles4)
                    
            elif Liste[loop] == CORNERLEFTD:
                
                if Dico[Liste[loop]] == 0:
                    AutomatisationResolveur(3, ValeursPossibles5)
                    
                    
            elif Liste[loop] == CORNERLEFTU:
                if Dico[Liste[loop]] == 0:
                    AutomatisationResolveur(3, ValeursPossibles6)
                    
            elif Liste[loop] == CORNERRIGHTD:
                if Dico[Liste[loop]] == 0:
                    AutomatisationResolveur(3, ValeursPossibles8)
                    
            elif Liste[loop] == CORNERRIGHTU:
                if Dico[Liste[loop]] == 0:
                    AutomatisationResolveur(3, ValeursPossibles7)
                    
            else:
                if Dico[Liste[loop]] == 0:
                    AutomatisationResolveur(8, ValeursPossibles)          
            if statut == "lose":
                Bse_Case[Liste[loop]].config(image = ImageVert)
                break
            elif loop == len(Liste):
                break
            else:
                pass
            loop +=1
            
            print("NombreDeZérosTraités: ", NombreDeZérosTraités)
            print(loop)
             









def VerifiDrapEtat(Etat, NumeroCase, x, y):
    if Bse_donnee[NumeroCase].compteur in LINEUP:
        pass
    if Bse_donnee[NumeroCase].compteur in LINEDOWN:
        pass
    if Bse_donnee[NumeroCase].compteur in LINERIGHT:
        pass
    if Bse_donnee[NumeroCase].compteur in LINELEFT:
        pass
    if Bse_donnee[NumeroCase].compteur == 99:
        pass
    if Bse_donnee[NumeroCase].compteur == 0:
        pass
    if Bse_donnee[NumeroCase].compteur == 9:
        pass
    if Bse_donnee[NumeroCase].compteur == 90:
        pass
    else:
        if (Bse_donnee[NumeroCase+x].type != 0 and Bse_Case_Drapeau[NumeroCase+x] == 0)and (Bse_donnee[NumeroCase+y].type != 0 and Bse_Case_Drapeau[NumeroCase+y] == 0):
            if Bse_donnee[NumeroCase+x].etat == Etat and Bse_donnee[NumeroCase+x].etat == Etat:
                    
                return True
        else:
            return False


m = 0
def Drap(ValeursPoss, posDrap):
    for element in ValeursPoss:
        if Bse_donnee[posDrap + element].type == 1:
            for i in ValeursPoss :
                ClicCase(Bse_donnee[posDrap + element + i].compteur)
Liste1 = []
    
def VerifDrapeau():
    for boucle in ListeDrapeau:
        near(boucle, Drap(ValeursPossibles2, boucle), Drap(ValeursPossibles1, boucle), Drap(ValeursPossibles4, boucle),Drap(ValeursPossibles3, boucle) , Drap(ValeursPossibles5, boucle), Drap(ValeursPossibles6, boucle),Drap(ValeursPossibles7, boucle) ,Drap(ValeursPossibles8, boucle),Drap(ValeursPossibles, boucle))
def CornExtend():
    for l in range(len(ListeDrapeau)):
        for loop in ValeursPossibles:
            VerifCoin(LINEUP, ValeursPossibles1, loop)
            VerifCoin(LINEDOWN, ValeursPossibles2, loop)
            VerifCoin(LINERIGHT, ValeursPossibles3, loop)
            VerifCoin(LINELEFT, ValeursPossibles4, loop)
            
            
                        
    
        
def Coin(a,b,c,d,e,f,g,h):
    global Liste
    global Bse_donnee
    #On supprime toute les cases traités par le programme précédemment.

    #Maintenant on va demander au programme de reconnaître les paternes en formes de coins dans lesquels nous sommes sûr qu'il y a une bombe au boût avec un coin avec une valeur de 1.
        #On crée une nouvelle liste avec tout les cases avec la valeur 1 de révélée.
    Liste1 = (itemgetter(*[idx for idx,e in enumerate(list(Dico.values())) if e == 1])(list(Dico.keys())))
    for NumeroCase in Liste1:
        
        ev = a
        eb = b
        print("NumeroCase : ", NumeroCase, )
        #if NumeroCase in LINEUP == False and NumeroCase in LINELEFT == False and NumeroCase in LINERIGHT == False and NumeroCase in LINEDOWN == False and NumeroCase != 0 and NumeroCase != 90 and NumeroCase != 9 and NumeroCase != 99:
        if VerifiDrapEtat("révélée",NumeroCase, ev, eb) == True :
            if Bse_donnee[NumeroCase+c].etat != "caché" and Bse_donnee[NumeroCase + d].etat != "caché" and Bse_donnee[NumeroCase+e].etat != "caché" and Bse_donnee[NumeroCase+f].etat != "caché" and Bse_donnee[NumeroCase+g].etat != "caché":
                if Bse_donnee[NumeroCase+h].etat == "Drapeau":
                    pass
                    
                elif Bse_donnee[NumeroCase+h].etat == "caché":
                        
                    ClicDrapeau()
                    ClicCase(NumeroCase+h)
                    #Bse_Case[NumeroCase+h].config(image = ImageVert)
                    ClicDrapeau()
                    print(NumeroCase, "Sucess")
                    Bse_Case[NumeroCase].config(image = ImageVert)
            else:
                print("Erreur 1")
        else:
            print("Erreur 2")
                   
def ResolveCoin():
    Coin(10,1,-1,+9,-11,-10,-9,+11)#Coin Haut Gauche
    
    Coin(-10, -1,+1,+11,+11,+10,+9,-9)#Coin Bas Droite
    Coin(-10,+1,-1,-11,+9,+10,+11,-9)#Coin Bas Gauche
    Coin(+10,-1,+1,+11,-9,-10,-11,+9)#Coin Haut Droite        
            
Numero = 0                     
ListeZérosT = []           
NombreDeZérosTraités = 0

ListeCasesRévélées = [] 
VariableLoop = 0
    #Fonction résolvant le démineur; Le dioctionnaire sert ici.
ValeursPossibles = [1,-1,10,-10,11,-11,9,-9]
ValeursPossibles1 = [1,-1,10,9,11] #LineUp
ValeursPossibles2 = [1,-1,-10,-9,-11]#LineDown
ValeursPossibles3 = [-1,10,-10,9,-11]#Right
ValeursPossibles4 = [1,10,-10,-9,11]
ValeursPossibles5 = [1,-10,-9]
ValeursPossibles6 = [1,10,11]
ValeursPossibles7 = [-1,10,9]
ValeursPossibles8 = [-1,10,-11]



NombreDeZérosDévoilée = 0        
Liste = []
ListeDrapeau = []

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
TableauDémineur = Tk()
TableauDémineur.title("Démineur - Aristide, Matéo et Raphaël - ISN 2018-2019")
#
Dico = {}
#Largeur de la grille
LargeurGrille = 10

#Nombre de Bombes sur la grille
NBBOMBES = 10

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
#Partie Gaganée ou Perdue 
statut = ""


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
def Start():
    Compteur = 0

    for ligne in range(LargeurGrille):
        for colonne in range(LargeurGrille):
             
            Bse_donnee[Compteur] = Case(Compteur, colonne, ligne, 0)
            Bse_Case[Compteur] = Button(TableauDémineur, image = ImageBlanc, state = "active", command = lambda Compteur=Compteur:fonction(Bse_donnee[Compteur].compteur))
            Bse_Case[Compteur].grid(row=ligne, column=colonne)
            Compteur += 1
    #Nombre de cases révélées (pour savoir où l'on en est dans la partie
    CasesRévélées = 0

    #Si la valeur du drapeau est 0, alors le drapeau n'est pas activé (Rouge). Si c'est 0, alors il est activé (Vert).

    ValeurDrapeau = 0
    #Partie Gaganée ou Perdue 
    statut = ""
    SETBOMBE(NBBOMBES)
    DetectBombe()
Start()



#Génération du menu latéral droit

BoutonDrapeau = Button(TableauDémineur, image = ImageDrapeau, command = ClicDrapeau)
BoutonDrapeau.grid(row = 1, column = LargeurGrille)
IndicateurDrapeau = Label(TableauDémineur, image = ImageRouge)
IndicateurDrapeau.grid(row = 1, column = LargeurGrille + 1)
Resolveur = Button(TableauDémineur, text='Résoudre', command=Resolve)
Resolveur.grid(row = 3, column = LargeurGrille + 1 )
Suite = Button(TableauDémineur, text='Coins', command=ResolveCoin)
Suite.grid(row = 5, column = LargeurGrille + 1 )

