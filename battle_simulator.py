# Importation of libraries
import random
import numpy as np
import csv
import pandas as pd
import os

# relative path
absolutepath = os.path.abspath(__file__)
fileDirectory = os.path.dirname(absolutepath)
parentDirectory = os.path.dirname(fileDirectory)
databasePath = os.path.join(fileDirectory, 'database.csv')
resultPath =  os.path.join(fileDirectory, 'result.csv')


# Each Pokemon and attacks are defined in dictionaries

Pokemon1={
    "name":"s", 
    "type1":"s", 
    "type2":"s", 
    "hp":0, 
    "current_hp":0, 
    "atk":0, 
    "def": 0, 
    "speatk":0, 
    "spedef":0, 
    "speed":0
    }


Pokemon2={
    "name":"s", 
    "type1":"s", 
    "type2":"s", 
    "hp":0, 
    "current_hp":0, 
    "atk":0, 
    "def": 0, 
    "speatk":0, 
    "spedef":0, 
    "speed":0
    }

Attack1={
    "name":"s", 
    "type":"s", 
    "test":"s", 
    "roll_bonus": 0, 
    "nb_d6": 0, 
    "damage_bonus":0
    }

Attack2={
    "name":"s", 
    "type":"s", 
    "test":"s", 
    "roll_bonus": 0, 
    "nb_d6": 0, 
    "damage_bonus":0
    }

#function section

#Input fonction will fill the dictionaries will the data in the database
def input_poke1(name,type1,type2,HP,atk,_def,speatk,spedef,speed):
    Pokemon1["name"] = name
    Pokemon1["type1"] = type1
    Pokemon1["type2"] = type2
    Pokemon1["hp"] = int(HP)
    Pokemon1["atk"] = int(atk)
    Pokemon1["def"] = int(_def)
    Pokemon1["speatk"] = int(speatk)
    Pokemon1["spedef"] = int(spedef)
    Pokemon1["speed"] = int(speed)
    return Pokemon1

def input_poke2(name,type1,type2,HP,atk,_def,speatk,spedef,speed):
    Pokemon2["name"] = name
    Pokemon2["type1"] = type1
    Pokemon2["type2"] = type2
    Pokemon2["hp"] = int(HP)
    Pokemon2["atk"] = int(atk)
    Pokemon2["def"] = int(_def)
    Pokemon2["speatk"] = int(speatk)
    Pokemon2["spedef"] = int(spedef)
    Pokemon2["speed"] = int(speed)
    return Pokemon2

def input_att1(name,type,test,roll_bonus,nb_d6,damage_bonus):
    Attack1["name"] = name
    Attack1["type"] = type
    Attack1["test"] = test
    Attack1["roll_bonus"] = int(roll_bonus)
    Attack1["nb_d6"] = int(nb_d6)
    Attack1["damage_bonus"] = int(damage_bonus)
    return Attack1

def input_att2(name,type,test,roll_bonus,nb_d6,damage_bonus):
    Attack2["name"] = name
    Attack2["type"] = type
    Attack2["test"] = test
    Attack2["roll_bonus"] = int(roll_bonus)
    Attack2["nb_d6"] = int(nb_d6)
    Attack2["damage_bonus"] = int(damage_bonus)
    return Attack2


#The aim is to compare speed between Pokemon to know who will attack first. In the tabletops rules, if the both pokemons have the same speed
#Pokemon of the players moves first. Here we chose the first to move at random
def initiative():
    if Pokemon1["speed"] > Pokemon2["speed"]:
        first_poke = Pokemon1["name"]
    elif Pokemon1["speed"] < Pokemon2["speed"]:
        first_poke = Pokemon2["name"]
    else:
        coin = random.randint(1,2)
        if coin == 1:
            first_poke = Pokemon1["name"]
        else:
            first_poke = Pokemon2["name"]
    return first_poke

#the type_function will return a number of additionnal dices for damage calculation
#If the attack has no effect on the Pokemon (for instance a electric attack on a ground pokemon), the result is -1000.
#The damage will be well below 0. Later, a condition will change negative damage to 0.
def type_function(type_attack, type_defense1, type_defense2):
    type_list = ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]
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

    type_index_attack = 0
    for i in range(18):
        if type_attack == type_list[i]:
            type_index_attack = i

    type_index_defense1 = 0
    for i in range(18):
        if type_defense1 == type_list[i]:
            type_index_defense1 = i

    type_index_defense2 = 0
    for i in range(18):
        if type_defense2 == type_list[i]:
            type_index_defense2 = i

    type_dice = type_table[type_index_attack, type_index_defense1] + type_table[type_index_attack, type_index_defense2]
    return type_dice

#difficulty and resistance are calculated outside of the fonction damage because the values won't change between battle
def difficulty1():
    if Attack1["test"] == "atk":
        difficulty1 = Pokemon1["atk"] + Attack1["roll_bonus"]
    elif Attack1["test"] == "speatk":
        difficulty1 = Pokemon1["speatk"] + Attack1["roll_bonus"]
    else:
        difficulty1 = 20
    return difficulty1

def difficulty2():
    if Attack2["test"] == "atk":
        difficulty2 = Pokemon2["atk"] + Attack2["roll_bonus"]
    elif Attack2["test"] == "speatk":
        difficulty2 = Pokemon2["speatk"] + Attack2["roll_bonus"]
    else:
        difficulty2 = 20
    return difficulty2 

def resistance_Poke1():
    if Attack2["test"] == "atk" and Pokemon2["atk"] >= 15:
        resistance_Poke1 = Pokemon1["def"] - 10 + (Pokemon2["atk"] - 15)
    elif Attack2["test"] == "speatk" and Pokemon2["speatk"] >= 15:
        resistance_Poke1 = Pokemon1["spedef"] - 10 + (Pokemon2["speatk"] - 15)
    elif Attack2["test"] == "atk" and Pokemon2["atk"] < 15:
        resistance_Poke1 = Pokemon1["def"] - 10
    elif Attack2["test"] == "speatk" and Pokemon2["speatk"] <15:
        resistance_Poke1 = Pokemon1["spedef"] - 10
    else:
        resistance_Poke1 = 0
    
    if resistance_Poke1 < 0:
        resistance_Poke1 = 0
    return resistance_Poke1

def resistance_Poke2():
    if Attack1["test"] == "atk" and Pokemon1["atk"] >= 15:
        resistance_Poke2 = Pokemon2["def"] - 10 + (Pokemon1["atk"] - 15)
    elif Attack1["test"] == "speatk" and Pokemon1["speatk"] >= 15:
        resistance_Poke2 = Pokemon2["spedef"] - 10 + (Pokemon1["speatk"] - 15)
    elif Attack1["test"] == "atk" and Pokemon1["atk"] < 15:
        resistance_Poke2 = Pokemon2["def"] - 10
    elif Attack1["test"] == "speatk" and Pokemon1["speatk"] <15:
        resistance_Poke2 = Pokemon2["spedef"] - 10
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
        nb_d6_type = type_function(Attack1["type"], Pokemon2["type1"], Pokemon2["type2"])
        for i in range(abs(nb_d6_type)):
            modif_type = modif_type + random.randint(1, 6)
        for i in range(Attack1["nb_d6"]):
            roll_damage = roll_damage + random.randint(1, 6)
        if nb_d6_type > 0:
            damage = roll_damage + modif_type + Attack1["damage_bonus"]
        else:
            damage = roll_damage - modif_type + Attack1["damage_bonus"]
        if damage < 0:
            damage = 0 #damage cannot be negative
    else :
        damage = 0
    if resi_Poke1 < damage:
        Pokemon2["current_hp"] = Pokemon2["current_hp"] - damage + resi_Poke2

def calcul_damage_Attack2():
    roll = random.randint(1, 20)
    modif_type = 0
    roll_damage = 0
    damage = 0
    if roll <= dif2:
        nb_d6_type = type_function(Attack2["type"], Pokemon1["type1"], Pokemon1["type2"])
        for i in range(abs(nb_d6_type)):
            modif_type = modif_type + random.randint(1, 6)
        for i in range(int(Attack2["nb_d6"])):
            roll_damage = roll_damage + random.randint(1, 6)
        if nb_d6_type > 0:
            damage = roll_damage + modif_type + Attack2["damage_bonus"]
        else:
            damage = roll_damage - modif_type + Attack2["damage_bonus"]
        if damage < 0:
            damage = 0
    else :
        damage = 0
    if resi_Poke1 < damage:
        Pokemon1["current_hp"] = Pokemon1["current_hp"] - damage + resi_Poke1


database = []

file = open(databasePath, "r")
reader = csv.DictReader(file, delimiter=';')
for row in reader:
    database.append(row)

result = {
    'Pokemon1': [],
    'Pokemon2': [],
    'Attack1': [],
    'Attack2': [],
    'Nb_victory_pok1': [],
    'Nb_victory_pok2': [],
    'Mean_nb_turn': []
    }

df = pd.DataFrame(result)
indice_df = 0

for i in range(len(database)):
    for j in range(i): #So two pokemons will only fight once together. One as Pokemon 1 and the other as Pokemon 2. The reverse battle is not interesting.
        #There are the data we want to observe
        report_tour = []
        nb_victory_Poke1 = 0
        nb_victory_Poke2 = 0
        
        #Input the both Pokemon with their attack for the couple (i, j)
        input_poke1(database[i]["ï»¿name_poke"], database[i]["type1"], database[i]["type2"], database[i]["hp"], database[i]["atk"], database[i]["def"], database[i]["speatk"], database[i]["spedef"], database[i]["speed"])
        input_poke2(database[j]["ï»¿name_poke"], database[j]["type1"], database[j]["type2"], database[j]["hp"], database[j]["atk"], database[j]["def"], database[j]["speatk"], database[j]["spedef"], database[j]["speed"])
        input_att1(database[i]["name_atk"], database[i]["type"], database[i]["test"], database[i]["roll_bonus"], database[i]["nb_d6"], database[i]["damage_bonus"])
        input_att2(database[j]["name_atk"], database[j]["type"], database[j]["test"], database[j]["roll_bonus"], database[j]["nb_d6"], database[j]["damage_bonus"])
        #I don't know why but python adds "ï»¿" before the name of the Pokemon, probably an encoding problem
        
        #During the 1000 battles, this values will not change, so we compute them before the for loop
        dif1 = difficulty1()
        dif2 = difficulty2()
        resi_Poke1 = resistance_Poke1()
        resi_Poke2 = resistance_Poke2()

        for k in range(1000):
            
            #Reset HP before the battle
            Pokemon1["current_hp"] = Pokemon1["hp"]
            Pokemon2["current_hp"] = Pokemon2["hp"]
            nb_tour = 0

            while Pokemon1["current_hp"] > 0 and Pokemon2["current_hp"] >0 and nb_tour < 20: #some battle are infinite so we introduce a limit
                initiative() #if the both pokemon have the same speed, we want to execute the function for each battle, that's why we don't execute it with difficulty and resistance
                if initiative() == Pokemon1["name"]:
                    calcul_damage_Attack1()
                    if Pokemon2["current_hp"] > 0:
                        calcul_damage_Attack2()
                    nb_tour = nb_tour + 1
                else:
                    calcul_damage_Attack2()
                    if Pokemon1["current_hp"] > 0:
                        calcul_damage_Attack1()
                    nb_tour = nb_tour + 1
            report_tour.append(nb_tour)
            if Pokemon1["current_hp"] <= 0:
                nb_victory_Poke2 = nb_victory_Poke2 + 1
            elif Pokemon2["current_hp"] <= 0:
                nb_victory_Poke1 = nb_victory_Poke1 + 1
        mean_nb_tour = sum(report_tour)/len(report_tour) 

        df.loc[indice_df] = [Pokemon1["name"], Pokemon2["name"], Attack1["name"], Attack2["name"], nb_victory_Poke1, nb_victory_Poke2, mean_nb_tour]
        indice_df = indice_df + 1
        print(str(round((indice_df/28920)*100, 2)) + " %")
        #this indice allows us to know the progress

df.to_csv(resultPath)