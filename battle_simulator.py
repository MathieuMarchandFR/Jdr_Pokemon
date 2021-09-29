#Importation of libraries
import random
import numpy as np
import csv
import pandas as pd

#Each Pokemon and attacks are defined in dictionaries

Pokemon1={"Name":"example", "Type1":"example", "Type2":"example", "HP":0, "current_HP":0, "Atk":0, "Def": 0, "SpeAtk":0, "SpeDef":0, "Speed":0}
Pokemon2={"Name":"example", "Type1":"example", "Type2":"example", "HP":0, "current_HP":0, "Atk":0, "Def": 0, "SpeAtk":0, "SpeDef":0, "Speed":0}

Attack1={"Name":"example", "Type":"example", "test":'none', "roll_bonus": 0, "Nb_d6": 0, "damage_bonus":0}
Attack2={"Name":"example", "Type":"example", "test":'none', "roll_bonus": 0, "Nb_d6": 0, "damage_bonus":0}

#function section

#Input fonction will fill the dictionaries will the data in the database
def input_poke1(name,type1,type2,HP,atk,_def,speatk,spedef,speed):
    Pokemon1["Name"] = name
    Pokemon1["Type1"] = type1
    Pokemon1["Type2"] = type2
    Pokemon1["HP"] = int(HP)
    Pokemon1["Atk"] = int(atk)
    Pokemon1["Def"] = int(_def)
    Pokemon1["SpeAtk"] = int(speatk)
    Pokemon1["SpeDef"] = int(spedef)
    Pokemon1["Speed"] = int(speed)
    return Pokemon1

def input_poke2(name,type1,type2,HP,atk,_def,speatk,spedef,speed):
    Pokemon2["Name"] = name
    Pokemon2["Type1"] = type1
    Pokemon2["Type2"] = type2
    Pokemon2["HP"] = int(HP)
    Pokemon2["Atk"] = int(atk)
    Pokemon2["Def"] = int(_def)
    Pokemon2["SpeAtk"] = int(speatk)
    Pokemon2["SpeDef"] = int(spedef)
    Pokemon2["Speed"] = int(speed)
    return Pokemon2

def input_att1(name,type,test,roll_bonus,nb_d6,damage_bonus):
    Attack1["Name"] = name
    Attack1["Type"] = type
    Attack1["test"] = test
    Attack1["roll_bonus"] = int(roll_bonus)
    Attack1["Nb_d6"] = int(nb_d6)
    Attack1["damage_bonus"] = int(damage_bonus)
    return Attack1

def input_att2(name,type,test,roll_bonus,nb_d6,damage_bonus):
    Attack2["Name"] = name
    Attack2["Type"] = type
    Attack2["test"] = test
    Attack2["roll_bonus"] = int(roll_bonus)
    Attack2["Nb_d6"] = int(nb_d6)
    Attack2["damage_bonus"] = int(damage_bonus)
    return Attack2


#The aim is to compare speed between Pokemon to know who will attack first. In the tabletops rules, if the both pokemons have the same speed
#Pokemon of the players moves first. Here we chose the first to move at random
def initiative():
    if Pokemon1["Speed"] > Pokemon2["Speed"]:
        first_poke = Pokemon1["Name"]
    elif Pokemon1["Speed"] < Pokemon2["Speed"]:
        first_poke = Pokemon2["Name"]
    else:
        coin = random.randint(1,2)
        if coin == 1:
            first_poke = Pokemon1["Name"]
        else:
            first_poke = Pokemon2["Name"]
    return first_poke

#the type_function will return a number of additionnal dices for damage calculation
#If the attack has no effect on the Pokemon (for instance a electric attack on a ground pokemon), the result is -1000.
#The damage will be well below 0. Later, a condition will change negative damage to 0.
def type_function(type_Attack, type_defense1, type_defense2):
    type_list = ["normal", "feu", "eau", "electrique", "plante", "glace", "combat", "poison", "sol", "vol", "psy", "insecte", "roche", "spectre", "dragon", "tenebres", "acier", "fee"]
    type_dice = 0
    type_table = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1000, 0, 0, -1, 0],
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

    type_index_Attack = 0
    for i in range(18):
        if type_Attack == type_list[i]:
            type_index_Attack = i

    type_index_defense1 = 0
    for i in range(18):
        if type_defense1 == type_list[i]:
            type_index_defense1 = i

    type_index_defense2 = 0
    for i in range(18):
        if type_defense2 == type_list[i]:
            type_index_defense2 = i

    type_dice = type_table[type_index_Attack, type_index_defense1] + type_table[type_index_Attack, type_index_defense2]
    return type_dice

#difficulty and resistance are calculated outside of the fonction damage because the values won't change between battle
def difficulty1():
    if Attack1["test"] == "Atk":
        difficulty1 = Pokemon1["Atk"] + Attack1["roll_bonus"]
    elif Attack1["test"] == "SpeAtk":
        difficulty1 = Pokemon1["SpeAtk"] + Attack1["roll_bonus"]
    else:
        difficulty1 = 20
    return difficulty1

def difficulty2():
    if Attack2["test"] == "Atk":
        difficulty2 = Pokemon2["Atk"] + Attack2["roll_bonus"]
    elif Attack2["test"] == "SpeAtk":
        difficulty2 = Pokemon2["SpeAtk"] + Attack2["roll_bonus"]
    else:
        difficulty2 = 20
    return difficulty2 

def resistance_Poke1():
    if Attack2["test"] == "Atk" and Pokemon2["Atk"] >= 15:
        resistance_Poke1 = Pokemon1["Def"] - 10 + (Pokemon2["Atk"] - 15)
    elif Attack2["test"] == "SpeAtk" and Pokemon2["SpeAtk"] >= 15:
        resistance_Poke1 = Pokemon1["SpeDef"] - 10 + (Pokemon2["SpeAtk"] - 15)
    elif Attack2["test"] == "Atk" and Pokemon2["Atk"] < 15:
        resistance_Poke1 = Pokemon1["Def"] - 10
    elif Attack2["test"] == "SpeAtk" and Pokemon2["SpeAtk"] <15:
        resistance_Poke1 = Pokemon1["SpeDef"] - 10
    else:
        resistance_Poke1 = 0
    
    if resistance_Poke1 < 0:
        resistance_Poke1 = 0
    return resistance_Poke1

def resistance_Poke2():
    if Attack1["test"] == "Atk" and Pokemon1["Atk"] >= 15:
        resistance_Poke2 = Pokemon2["Def"] - 10 + (Pokemon1["Atk"] - 15)
    elif Attack1["test"] == "SpeAtk" and Pokemon1["SpeAtk"] >= 15:
        resistance_Poke2 = Pokemon2["SpeDef"] - 10 + (Pokemon1["SpeAtk"] - 15)
    elif Attack1["test"] == "Atk" and Pokemon1["Atk"] < 15:
        resistance_Poke2 = Pokemon2["Def"] - 10
    elif Attack1["test"] == "SpeAtk" and Pokemon1["SpeAtk"] <15:
        resistance_Poke2 = Pokemon2["SpeDef"] - 10
    else:
        resistance_Poke2 = 0

    if resistance_Poke2 < 0:
        resistance_Poke2 = 0
    return resistance_Poke2

#The calcul damage compare the roll and the difficulty.
#If it's a success (roll =< difficulty), we compute the damage thanks to caracteristicks of the attack/Pokemon, the resistance and the type
def calcul_damage_Attack1():
    roll = random.randint(1, 20)
    modif_type = 0
    roll_damage = 0
    damage = 0
    if roll <= dif1:
        Nb_d6_type = type_function(Attack1["Type"], Pokemon2["Type1"], Pokemon2["Type2"])
        for i in range(abs(Nb_d6_type)):
            modif_type = modif_type + random.randint(1, 6)
        for i in range(Attack1["Nb_d6"]):
            roll_damage = roll_damage + random.randint(1, 6)
        if Nb_d6_type > 0:
            damage = roll_damage + modif_type + Attack1["damage_bonus"]
        else:
            damage = roll_damage - modif_type + Attack1["damage_bonus"]
        if damage < 0:
            damage = 0 #damage cannot be negative
    else :
        damage = 0
    if resi_Poke1 < damage:
        Pokemon2["current_HP"] = Pokemon2["current_HP"] - damage + resi_Poke2

def calcul_damage_Attack2():
    roll = random.randint(1, 20)
    modif_type = 0
    roll_damage = 0
    damage = 0
    if roll <= dif2:
        Nb_d6_type = type_function(Attack2["Type"], Pokemon1["Type1"], Pokemon1["Type2"])
        for i in range(abs(Nb_d6_type)):
            modif_type = modif_type + random.randint(1, 6)
        for i in range(int(Attack2["Nb_d6"])):
            roll_damage = roll_damage + random.randint(1, 6)
        if Nb_d6_type > 0:
            damage = roll_damage + modif_type + Attack2["damage_bonus"]
        else:
            damage = roll_damage - modif_type + Attack2["damage_bonus"]
        if damage < 0:
            damage = 0
    else :
        damage = 0
    if resi_Poke1 < damage:
        Pokemon1["current_HP"] = Pokemon1["current_HP"] - damage + resi_Poke1


database_generateur = []

file = open("C:\\Users\\33606\\Documents\\JDR\\jdr Pokemon\\Livre de Base Beta\\Data\\database_generateur.csv", "r")
reader = csv.DictReader(file, delimiter=';')
for row in reader:
    database_generateur.append(row)

data = {'Pokemon1': [],
        'Pokemon2': [],
        'Attack1': [],
        'Attack2': [],
        'nb_victory_pok1': [],
        'Nb_victory_pok2': [],
        'Mean_nb_turn': []}

df = pd.DataFrame(data)
indice_df = 0

for i in range(241):
    for j in range(i): #So two pokemons will only fight once together. One as Pokemon 1 and the other as Pokemon 2. The reverse battle is not interesting.
        #There are the data we want to observe
        Report_tour = []
        Nb_victory_Poke1 = 0
        Nb_victory_Poke2 = 0
        
        #Input the both Pokemon with their attack for the couple (i, j)
        input_poke1(database_generateur[i]["ï»¿Name_Poke"] + "_1", database_generateur[i]["Type1"], database_generateur[i]["Type2"], database_generateur[i]["HP"], database_generateur[i]["Atk"], database_generateur[i]["Def"], database_generateur[i]["SpeAtk"], database_generateur[i]["SpeDef"], database_generateur[i]["Speed"])
        input_poke2(database_generateur[j]["ï»¿Name_Poke"] + "_2", database_generateur[j]["Type1"], database_generateur[j]["Type2"], database_generateur[j]["HP"], database_generateur[j]["Atk"], database_generateur[j]["Def"], database_generateur[j]["SpeAtk"], database_generateur[j]["SpeDef"], database_generateur[j]["Speed"])
        input_att1(database_generateur[i]["Name_Atk"], database_generateur[i]["Type"], database_generateur[i]["Test"], database_generateur[i]["Roll_bonus"], database_generateur[i]["Nb_d6"], database_generateur[i]["Damage_bonus"])
        input_att2(database_generateur[j]["Name_Atk"], database_generateur[j]["Type"], database_generateur[j]["Test"], database_generateur[j]["Roll_bonus"], database_generateur[j]["Nb_d6"], database_generateur[j]["Damage_bonus"])
        #I don't know why but python adds "ï»¿" before the name of the Pokemon, probably an encoding problem
        #The _1 and _2 prevent errors when we compare the name of the Pokemon (for instance in the initiative function)
        
        #During the 1000 battles, this values will not change, so we compute them before the for loop
        dif1 = difficulty1()
        dif2 = difficulty2()
        resi_Poke1 = resistance_Poke1()
        resi_Poke2 = resistance_Poke2()

        for k in range(1000):
            
            #Reset HP before the battle
            Pokemon1["current_HP"] = Pokemon1["HP"]
            Pokemon2["current_HP"] = Pokemon2["HP"]
            Nb_tour = 0

            while Pokemon1["current_HP"] > 0 and Pokemon2["current_HP"] >0 and Nb_tour < 20: #some battle are infinite so we introduce a limit
                initiative() #if the both pokemon have the same speed, we want to execute the function for each battle, that's why we don't execute it with difficulty and resistance
                if initiative() == Pokemon1["Name"]:
                    calcul_damage_Attack1()
                    if Pokemon2["current_HP"] > 0:
                        calcul_damage_Attack2()
                    Nb_tour = Nb_tour + 1
                else:
                    calcul_damage_Attack2()
                    if Pokemon1["current_HP"] > 0:
                        calcul_damage_Attack1()
                    Nb_tour = Nb_tour + 1
            Report_tour.append(Nb_tour)
            if Pokemon1["current_HP"] <= 0:
                Nb_victory_Poke2 = Nb_victory_Poke2 + 1
            elif Pokemon2["current_HP"] <= 0:
                Nb_victory_Poke1 = Nb_victory_Poke1 + 1
        Mean_nb_tour = sum(Report_tour)/len(Report_tour) 

        df.loc[indice_df] = [Pokemon1["Name"], Pokemon2["Name"], Attack1["Name"], Attack2["Name"], Nb_victory_Poke1, Nb_victory_Poke2, Mean_nb_tour]
        indice_df = indice_df + 1
        print(str(round((indice_df/28920)*100, 2)) + " %")
        #this indice allows us to know the progress

df.to_csv("C:\\Users\\33606\\Documents\\JDR\\jdr Pokemon\\Livre de Base Beta\\Data\\result.csv")
