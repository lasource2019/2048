from tkinter import *
from random import *
class Case:
    

    
    def __init__(self, compteur, abse, Ord, Type, nbbombesadjacentes):
   
        self.abse = abse
        self.ord = Ord 
        self.type = Type
        
        self.stat = print("Coordonnée(",abse,";",Ord,"), Type : ",self.type,  "id : ", compteur)
        self.compteur = compteur
        self.nbbombesadjacentes = 0
        
        
        
    

           
        
def setBombe(nbBombe):
    
    for tailleBombe in range(nbBombe):
       
        Abscisse = randint(0,9)
        print(Abscisse,";",end="")
        Ordonnee = randint(0,9)
        print(Ordonnee)
        compteur = 0
        Result = 0
        while Bse_donnee[Result].ord != Ordonnee and Bse_donnee[Result].abse != Abscisse:
            if (Bse_donnee[Result].abse == Abscisse) and (Bse_donnee[Result].ord != Ordonnee):
                
                Result += 10
            elif Bse_donnee[Result].ord == Ordonnee and Bse_donnee[Result].abse != Abscisse:
            
                Result += 1
            else:
                Result += 1  
            Bse_donnee[Result] = Case(Result, Abscisse, Ordonnee, "Bombe")
            Button(fenetre, text="Bombe", width=8,height=4).grid(row=Abscisse, column=Ordonnee)
            print(Bse_donnee[Result].type)
            break
            
def actualise(x):
    Bse_donnee[x].type = "Bombe"
    Bse_Case[x].config(text=Bse_donnee[x].type)
    
def actualiseAl():
    for loop in range(15):
        x = randint(0,99)
        Bse_donnee[x].type = "Bombe"
        Bse_Case[x].config(text=Bse_donnee[x].type)
    

        
def near():
    for case in range(len(Bse_donnee)):
    
        print(case)
        if Bse_donnee[case].compteur == 0:
            if Bse_donnee[case+1].type == "Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case+11].type == "Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case+10].type == "Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            Bse_Case[case].config(text=Bse_donnee[case].type)
        elif Bse_donnee[case].compteur == 9 :
            if Bse_donnee[case-1].type == "Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case+9].type == "Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case+10].type == "Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            Bse_Case[case].config(text=Bse_donnee[case].type)
        elif Bse_donnee[case].compteur == 99:
            if Bse_donnee[case-1].type == "Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case-11].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case-10].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            Bse_Case[case].config(text=Bse_donnee[case].type)
        elif Bse_donnee[case].compteur == 90:
            if Bse_donnee[case-9].type == "Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case+1].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case-10].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            Bse_Case[case].config(text=Bse_donnee[case].type)
        
        elif (Bse_donnee[case].compteur==1) or (Bse_donnee[case].compteur==2) or (Bse_donnee[case].compteur==3) or (Bse_donnee[case].compteur==4) or (Bse_donnee[case].compteur==5) or (Bse_donnee[case].compteur==6) or (Bse_donnee[case].compteur==7) or (Bse_donnee[case].compteur==8):
            if Bse_donnee[case+9].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case+10].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case+11].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case+1].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case-1].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            Bse_Case[case].config(text=Bse_donnee[case].type)
            
        elif (Bse_donnee[case].compteur==19) or (Bse_donnee[case].compteur==29) or (Bse_donnee[case].compteur==39) or (Bse_donnee[case].compteur==49) or (Bse_donnee[case].compteur==59) or (Bse_donnee[case].compteur==69) or (Bse_donnee[case].compteur==79) or (Bse_donnee[case].compteur==89):
            if Bse_donnee[case+9].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case-1].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case-11].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case+10].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case-10].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            Bse_Case[case].config(text=Bse_donnee[case].type)
        elif (Bse_donnee[case].compteur==91) or (Bse_donnee[case].compteur==92) or (Bse_donnee[case].compteur==93) or (Bse_donnee[case].compteur==94) or (Bse_donnee[case].compteur==95) or (Bse_donnee[case].compteur==96) or (Bse_donnee[case].compteur==97) or (Bse_donnee[case].compteur==98):
            if Bse_donnee[case-10].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case-9].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case-11].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case+1].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case-1].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            Bse_Case[case].config(text=Bse_donnee[case].type)
        elif (Bse_donnee[case].compteur==10) or (Bse_donnee[case].compteur==20) or (Bse_donnee[case].compteur==30) or (Bse_donnee[case].compteur==40) or (Bse_donnee[case].compteur==50) or (Bse_donnee[case].compteur==60) or (Bse_donnee[case].compteur==70) or (Bse_donnee[case].compteur==80):
            if Bse_donnee[case-10].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case-9].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case+11].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case+10].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            elif Bse_donnee[case+10].type=="Bombe" and Bse_donnee[case].type != "Bombe":
                Bse_donnee[case].type += 1
            Bse_Case[case].config(text=Bse_donnee[case].type)
        else:
            if Bse_donnee[case-10].type=="Bombe":
                if Bse_donnee[case].type != "Bombe":
                    Bse_donnee[case].type += 1
            elif Bse_donnee[case-9].type=="Bombe":
                if Bse_donnee[case].type != "Bombe":
                    Bse_donnee[case].type += 1
            elif Bse_donnee[case-11].type=="Bombe":
                if Bse_donnee[case].type != "Bombe":
                    Bse_donnee[case].type += 1
            elif Bse_donnee[case+1].type=="Bombe":
                if Bse_donnee[case].type != "Bombe":
                    Bse_donnee[case].type += 1
            elif Bse_donnee[case-1].type=="Bombe":
                if Bse_donnee[case].type != "Bombe":
                    Bse_donnee[case].type += 1
            elif Bse_donnee[case+10].type=="Bombe":
                if Bse_donnee[case].type != "Bombe":
                    Bse_donnee[case].type += 1
            elif Bse_donnee[case+9].type=="Bombe":
                if Bse_donnee[case].type != "Bombe":
                    Bse_donnee[case].type += 1
            elif Bse_donnee[case+11].type =="Bombe":
                if Bse_donnee[case].type != "Bombe":
                    Bse_donnee[case].type += 1
            Bse_Case[case].config(text=Bse_donnee[case].type)
            
      
      
def findCase(Bse_donnee, abss, Ord):
    AbscisseR = 0
    ordonneeR = 0
    compteur = 0
    global Result
    
    for i in range(len(Bse_donnee)):
        if Bse_donnee[i].getabse == abss:
            Result = i
            i += 1
        else:
            i+1
        if Bse_donnee[i].getord == Ord:
            Result = i
            i += 10
        elif Bse_donnee[i].getord == Ord and Bse_donnee[i].getabse == abss:
            print(Bse_donnee[Result].stat)
            break

def NumberBombAround():
    """
    Fonction pour déterminer le nombre de bombes adjacentes
    """
    for abse in range(10):
        for ord in range(10):
            Compteur = abse +ord
            if Case(compteur-11).type == "Bombe":
                Case(compteur) = Case(compteur, abse, ord, Type, nbbombesadjacentes=nbbombesadjacentes+1)
            if Case(compteur-10).type == "Bombe":
                Case(compteur) = Case(Compteur, abse, ord, Type, nbbombesadjacentes=nbbombesadjacentes+1)
            if Case(compteur-9).type == "Bombe":
                Case(compteur) = Case(Compteur, abse, ord, Type, nbbombesadjacentes=nbbombesadjacentes+1)
            if Case(compteur-1).type == "Bombe":
                Case(compteur) = Case(Compteur, abse, ord, Type, nbbombesadjacentes=nbbombesadjacentes+1)
            if Case(compteur+1).type == "Bombe":
                Case(compteur) = Case(Compteur, abse, ord, Type, nbbombesadjacentes=nbbombesadjacentes+1)
            if Case(compteur+9).type == "Bombe":
                Case(compteur) = Case(Compteur, abse, ord, Type, nbbombesadjacentes=nbbombesadjacentes+1)
            if Case(compteur+10).type == "Bombe":
                Case(compteur) = Case(Compteur, abse, ord, Type, nbbombesadjacentes=nbbombesadjacentes+1)
            if Case(compteur+11).type == "Bombe":
                Case(compteur) = Case(Compteur, abse, ord, Type, nbbombesadjacentes=nbbombesadjacentes+1)
    
    

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

actualiseAl()










