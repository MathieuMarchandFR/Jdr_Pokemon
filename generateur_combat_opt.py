import random
import numpy as np
import csv
import pandas as pd

Premier_poke = ""


Pokemon1={"Nom":"Exemple", "Type1":"exemple", "Type2":"exemple", "PV":45, "PV_actuel":0, "Att":10, "Def": 10, "AttSpe":10, "DefSpe":10, "Vit":10}
Pokemon2={"Nom":"Exemple", "Type1":"exemple", "Type2":"exemple", "PV":45, "PV_actuel":0, "Att":10, "Def": 10, "AttSpe":10, "DefSpe":10, "Vit":10}

Attaque1={"Nom":"Exemple", "Type":"exemple", "Epreuve":'Att', "Bonus_jet": 0, "Nb_d6": 2, "Bonus_degat":4}
Attaque2={"Nom":"Exemple", "Type":"exemple", "Epreuve":'Att', "Bonus_jet": 0, "Nb_d6": 2, "Bonus_degat":4}

def saisie_poke1(nom,type1,type2,pv,att,_def,attspe,defspe,vit):
    Pokemon1["Nom"] = nom
    Pokemon1["Type1"] = type1
    Pokemon1["Type2"] = type2
    Pokemon1["PV"] = int(pv)
    Pokemon1["Att"] = int(att)
    Pokemon1["Def"] = int(_def)
    Pokemon1["AttSpe"] = int(attspe)
    Pokemon1["DefSpe"] = int(defspe)
    Pokemon1["Vit"] = int(vit)
    return Pokemon1

def saisie_poke2(nom,type1,type2,pv,att,_def,attspe,defspe,vit):
    Pokemon2["Nom"] = nom
    Pokemon2["Type1"] = type1
    Pokemon2["Type2"] = type2
    Pokemon2["PV"] = int(pv)
    Pokemon2["Att"] = int(att)
    Pokemon2["Def"] = int(_def)
    Pokemon2["AttSpe"] = int(attspe)
    Pokemon2["DefSpe"] = int(defspe)
    Pokemon2["Vit"] = int(vit)
    return Pokemon2

def saisie_att1(nom,type,epreuve,bonus_jet,nb_d6,bonus_degat):
    Attaque1["Nom"] = nom
    Attaque1["Type"] = type
    Attaque1["Epreuve"] = epreuve
    Attaque1["Bonus_jet"] = int(bonus_jet)
    Attaque1["Nb_d6"] = int(nb_d6)
    Attaque1["Bonus_degat"] = int(bonus_degat)
    return Attaque1

def saisie_att2(nom,type,epreuve,bonus_jet,nb_d6,bonus_degat):
    Attaque2["Nom"] = nom
    Attaque2["Type"] = type
    Attaque2["Epreuve"] = epreuve
    Attaque2["Bonus_jet"] = int(bonus_jet)
    Attaque2["Nb_d6"] = int(nb_d6)
    Attaque2["Bonus_degat"] = int(bonus_degat)
    return Attaque2

def initiative():
    if Pokemon1["Vit"] > Pokemon2["Vit"]:
        Premier_poke = Pokemon1["Nom"]
    elif Pokemon1["Vit"] < Pokemon2["Vit"]:
        Premier_poke = Pokemon2["Nom"]
    else:
        piece = random.randint(1,2)
        if piece == 1:
            Premier_poke = Pokemon1["Nom"]
        else:
            Premier_poke = Pokemon2["Nom"]
    return Premier_poke

def fonction_type(type_attaque, type_defense1, type_defense2):
    liste_type = ["normal", "feu", "eau", "electrique", "plante", "glace", "combat", "poison", "sol", "vol", "psy", "insecte", "roche", "spectre", "dragon", "tenebres", "acier", "fee"]
    de_type = 0
    table_type = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1000, 0, 0, -1, 0],
                    [0, -1, -1, 0, 1, 1, 0, 0, 0, 0, 0, 1, -1, 0, -1, 0, 1, 0],
                    [0, 1, -1, 0, -1, 0, 0, 0, 1, 0, 0, 0, 1, 0, -1, 0, 0, 0],
                    [0, 0, 1, -1, -1, 0, 0, 0, -1000, 1, 0, 0, 0, 0, -1, 0, 0, 0],
                    [0, -1, 1, 0, -1, 0, 0, -1, 1, -1, 0, -1, 1, 0, -1, 0, -1, 0],
                    [0, -1, -1, 0, 1, -1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, -1, 0],
                    [1, 0, 0, 0, 0, 1, 0, -1, 0, -1, -1, -1, 1, -1000, 0, 1, 1, -1],
                    [0, 0, 0, 0, 1, 0, 0, -1, -1, 0, 0, 0, -1, -1, 0, 0, -1000, 1],
                    [0, 1, 0, 1, -1, 0, 0, 1, 0, -1000, 0, -1, 1, 0, 0, 0, 1, 0],
                    [0, 0, 0, -1, 1, 0, 1, 0, 0, 0, 0, 1, -1, 0, 0, 0, -1, 0],
                    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, -1, 0, 0, 0, 0, -1000, -1, 0],
                    [0, -1, 0, 0, 1, 0, -1, -1, 0, -1, 1, 0, 0, -1, 0, 1, -1, -1],
                    [0, 1, 0, 0, 0, 1, -1, 0, -1, 1, 0, 1, 0, 0, 0, 0, -1, 0],
                    [-1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, -1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, -1000],
                    [0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 1, 0, -1, 0, -1],
                    [0, -1, -1, -1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1, 1],
                    [0, -1, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 1, 1, -1, 0]])

    index_type_attaque = 0
    for i in range(18):
        if type_attaque == liste_type[i]:
            index_type_attaque = i

    index_type_defense1 = 0
    for i in range(18):
        if type_defense1 == liste_type[i]:
            index_type_defense1 = i

    index_type_defense2 = 0
    for i in range(18):
        if type_defense2 == liste_type[i]:
            index_type_defense2 = i

    de_type = table_type[index_type_attaque, index_type_defense1] + table_type[index_type_attaque, index_type_defense2]
    return de_type

def difficulté1():
    if Attaque1["Epreuve"] == "Att":
        difficulté1 = Pokemon1["Att"] + Attaque1["Bonus_jet"]
    elif Attaque1["Epreuve"] == "AttSpe":
        difficulté1 = Pokemon1["AttSpe"] + Attaque1["Bonus_jet"]
    else:
        difficulté1 = 20
    return difficulté1

def difficulté2():
    if Attaque2["Epreuve"] == "Att":
        difficulté2 = Pokemon2["Att"] + Attaque2["Bonus_jet"]
    elif Attaque2["Epreuve"] == "AttSpe":
        difficulté2 = Pokemon2["AttSpe"] + Attaque2["Bonus_jet"]
    else:
        difficulté2 = 20
    return difficulté2 

def resistance_Poke1():
    if Attaque2["Epreuve"] == "Att" and Pokemon2["Att"] >= 15:
        resistance_Poke1 = Pokemon1["Def"] - 10 + (Pokemon2["Att"] - 15)
    elif Attaque2["Epreuve"] == "AttSpe" and Pokemon2["AttSpe"] >= 15:
        resistance_Poke1 = Pokemon1["DefSpe"] - 10 + (Pokemon2["AttSpe"] - 15)
    elif Attaque2["Epreuve"] == "Att" and Pokemon2["Att"] < 15:
        resistance_Poke1 = Pokemon1["Def"] - 10
    elif Attaque2["Epreuve"] == "AttSpe" and Pokemon2["AttSpe"] <15:
        resistance_Poke1 = Pokemon1["DefSpe"] - 10
    
    if resistance_Poke1 < 0:
        resistance_Poke1 = 0
    return resistance_Poke1

def resistance_Poke2():
    if Attaque1["Epreuve"] == "Att" and Pokemon1["Att"] >= 15:
        resistance_Poke2 = Pokemon2["Def"] - 10 + (Pokemon1["Att"] - 15)
    elif Attaque1["Epreuve"] == "AttSpe" and Pokemon1["AttSpe"] >= 15:
        resistance_Poke2 = Pokemon2["DefSpe"] - 10 + (Pokemon1["AttSpe"] - 15)
    elif Attaque1["Epreuve"] == "Att" and Pokemon1["Att"] < 15:
        resistance_Poke2 = Pokemon2["Def"] - 10
    elif Attaque1["Epreuve"] == "AttSpe" and Pokemon1["AttSpe"] <15:
        resistance_Poke2 = Pokemon2["DefSpe"] - 10

    if resistance_Poke2 < 0:
        resistance_Poke2 = 0
    return resistance_Poke2

def calcul_degat_attaque1():
    jet = random.randint(1, 20)
    modif_type = 0
    jet_degat = 0
    degat = 0
    if jet <= dif1:
        Nb_d6_type = fonction_type(Attaque1["Type"], Pokemon2["Type1"], Pokemon2["Type2"])
        for i in range(abs(Nb_d6_type)):
            modif_type = modif_type + random.randint(1, 6)
        for i in range(Attaque1["Nb_d6"]):
            jet_degat = jet_degat + random.randint(1, 6)
        if Nb_d6_type > 0:
            degat = jet_degat + modif_type + Attaque1["Bonus_degat"]
        else:
            degat = jet_degat - modif_type + Attaque1["Bonus_degat"]
        if degat < 0:
            degat = 0
    else :
        degat = 0
    if resi_Poke1 < degat:
        Pokemon2["PV_actuel"] = Pokemon2["PV_actuel"] - degat + resi_Poke2

def calcul_degat_attaque2():
    jet = random.randint(1, 20)
    modif_type = 0
    jet_degat = 0
    degat = 0
    if jet <= dif2:
        Nb_d6_type = fonction_type(Attaque2["Type"], Pokemon1["Type1"], Pokemon1["Type2"])
        for i in range(abs(Nb_d6_type)):
            modif_type = modif_type + random.randint(1, 6)
        for i in range(int(Attaque2["Nb_d6"])):
            jet_degat = jet_degat + random.randint(1, 6)
        if Nb_d6_type > 0:
            degat = jet_degat + modif_type + Attaque2["Bonus_degat"]
        else:
            degat = jet_degat - modif_type + Attaque2["Bonus_degat"]
        if degat < 0:
            degat = 0
    else :
        degat = 0
    if resi_Poke1 < degat:
        Pokemon1["PV_actuel"] = Pokemon1["PV_actuel"] - degat + resi_Poke1


database_generateur = []

file = open("C:\\Users\\33606\\Documents\\JDR\\jdr Pokemon\\Livre de Base Beta\\Data\\database_generateur.csv", "r")
reader = csv.DictReader(file, delimiter=';')
for row in reader:
    database_generateur.append(row)

data = {'Pokemon1': [],
        'Pokemon2': [],
        'Attaque1': [],
        'Attaque2': [],
        'Nb victoire Pokemon1': [],
        'Nb victoire Pokemon2': [],
        'Moyenne du nombre de tour': []}

df = pd.DataFrame(data)
indice_df = 0

for i in range(241):
    for j in range(i):
        #Choix du combat, mise en place du report, des compteurs et des variables
        Report_tour = []
        Nb_victoire_Poke1 = 0
        Nb_victoire_Poke2 = 0
        saisie_poke1(database_generateur[i]["ï»¿Nom_Poke"] + "_1", database_generateur[i]["Type1"], database_generateur[i]["Type2"], database_generateur[i]["PV"], database_generateur[i]["Att"], database_generateur[i]["Def"], database_generateur[i]["AttSpe"], database_generateur[i]["DefSpe"], database_generateur[i]["Vit"])
        saisie_poke2(database_generateur[j]["ï»¿Nom_Poke"]+ "_2", database_generateur[j]["Type1"], database_generateur[j]["Type2"], database_generateur[j]["PV"], database_generateur[j]["Att"], database_generateur[j]["Def"], database_generateur[j]["AttSpe"], database_generateur[j]["DefSpe"], database_generateur[j]["Vit"])
        saisie_att1(database_generateur[i]["Nom_Att"], database_generateur[i]["Type"], database_generateur[i]["Epreuve"], database_generateur[i]["Bonus_jet"], database_generateur[i]["Nb_d6"], database_generateur[i]["Bonus_degat"])
        saisie_att2(database_generateur[j]["Nom_Att"], database_generateur[j]["Type"], database_generateur[j]["Epreuve"], database_generateur[j]["Bonus_jet"], database_generateur[j]["Nb_d6"], database_generateur[j]["Bonus_degat"])

        dif1 = difficulté1()
        dif2 = difficulté2()
        resi_Poke1 = resistance_Poke1()
        resi_Poke2 = resistance_Poke2()

        for k in range(1000):
            #Reset PV
            Pokemon1["PV_actuel"] = Pokemon1["PV"]
            Pokemon2["PV_actuel"] = Pokemon2["PV"]
            Nb_tour = 0
            while Pokemon1["PV_actuel"] > 0 and Pokemon2["PV_actuel"] >0 and Nb_tour < 20:
                initiative()
                if initiative() == Pokemon1["Nom"]:
                    calcul_degat_attaque1()
                    if Pokemon2["PV_actuel"] > 0:
                        calcul_degat_attaque2()
                    Nb_tour = Nb_tour + 1
                else:
                    calcul_degat_attaque2()
                    if Pokemon1["PV_actuel"] > 0:
                        calcul_degat_attaque1()
                    Nb_tour = Nb_tour + 1
            Report_tour.append(Nb_tour)
            if Pokemon1["PV_actuel"] <= 0:
                Nb_victoire_Poke2 = Nb_victoire_Poke2 + 1
            elif Pokemon2["PV_actuel"] <= 0:
                Nb_victoire_Poke1 = Nb_victoire_Poke1 + 1
        Moyenne_nb_tour = sum(Report_tour)/len(Report_tour) 

        df.loc[indice_df] = [Pokemon1["Nom"], Pokemon2["Nom"], Attaque1["Nom"], Attaque2["Nom"], Nb_victoire_Poke1, Nb_victoire_Poke2, Moyenne_nb_tour]
        indice_df = indice_df + 1
        print(indice_df)

#28920

df.to_csv("C:\\Users\\33606\\Documents\\JDR\\jdr Pokemon\\Livre de Base Beta\\Data\\result.csv")


        #with open('result.csv', 'w') as outf:
            #outf.write("Combat entre : " + str(Pokemon1["Nom"]) + " et " + str(Pokemon2["Nom"]) + "." + '\n' + "Score : " + str(Nb_victoire_Poke1) + " " + str(Nb_victoire_Poke2) + '\n' + "Moyenne du nombre de tour : " + str(Moyenne_nb_tour) + '\n')




#print("Combat N° " + str(i) + " terminé")

#print(Nb_victoire_Poke1)
#print(Nb_victoire_Poke2)
#print(Moyenne_nb_tour)

