#Ce scraper a pour but de récupérer les attaques d'une liste de Pokémon sur le site Poképédia
#Les résultats n'ont pas été très concluant et je n'avais finalement pas besoin de ces données
#J'ai néanmoins appris les bases du scrapping avec BeautifulSoup et je pourrais m'adapter à d'autres sites et pousser mes connaissances si besoin.

import os
import csv
import requests
from bs4 import BeautifulSoup
import codecs 

def encodageMaison(texte):
    AccentMoche = ['Ã©', 'Ã¨', 'Ã ', 'Ã¯', 'Ã´', 'Ã§', 'Ãª', 'Ã«', 'Ã¢', 'â™', 'â™€', 'Ã‰', 'ï»¿']
    AccentBeau = ['é', 'è', 'à', 'ï', 'ô', 'ç', 'ê', 'ë', 'â', '♂', '♀', 'É', '']
    for i in range(len(AccentMoche)):
        texte = texte.replace(AccentMoche[i],AccentBeau[i])
    return texte


file = open('C:\\Users\\33606\\Documents\\JDR\\jdr Pokemon\\Livre de Base Beta\\Data\\Build Fiches opti\\Scrapper\\nomPokemon.csv',newline='')
reader = csv.reader(file)


links = []
for row in reader:
    row = str(row)
    row = row[2:]
    row = row[:-2]
    links.append('https://www.pokepedia.fr/' + row)
file.close


with open('urls.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')


with open('urls.txt', 'r') as file:
    with open('extract.csv', 'w') as outf:
        outf.write('extract\n')
        for row in file:
            url = str(row.strip())
            url = encodageMaison(url)
            response = requests.get(url)
            

            if response.ok:
                soup = BeautifulSoup(response.text,'lxml')
                if soup.find('tbody', {'class': 'ListeCapacites8'}) is None:
                    #extract = soup.find('tbody', {'class': 'ListeCapacites7'}).findAll('a', title=True)
                    extract = soup.find('tbody', {'class': 'ListeCapacites7'})
                    outf.write(str(extract) + '\n')
                else:
                    #extract = soup.find('tbody', {'class': 'ListeCapacites8'}).findAll('a', title=True)
                    extract = soup.find('tbody', {'class': 'ListeCapacites8'})
                    outf.write(str(extract) + '\n')
