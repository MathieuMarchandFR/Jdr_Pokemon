import numpy as np
import numpy.linalg as alg


type_attaque = "sol"
type_defense1 = "feu"
type_defense2 = "electrique"
liste_type = ["normal", "feu", "eau", "electrique", "plante", "glace", "combat", "poison", "sol", "vol", "psy", "insecte", "roche", "spectre", "dragon", "tenebres", "acier", "fee"]

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

de_type = 0

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

print(de_type)
