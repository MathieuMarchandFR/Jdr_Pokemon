# Jdr_Pokemon
This is my adaptation of Pokémon to a tabletop roleplaying game.

The files:
- The file 'database.csv' contains the caracteristics of the Pokemon with one of their attack.
- 'battle_simulator.py' is my first battle simulator. It uses the 'database.csv' to simulate the battle beetween each species of the dataset and report the result in the file 'result.csv'.
- 'Win_rate.ipynb' is a jupyter notebook which uses the file 'result' and return the win_rate of each pokemon.  


Though the analysis of the result. I discover that using different attacks influence to much the result of the battles. In addition, adding the most important abilities of each Pokemon will also improve the reliability of the result.


- The file 'pokemon_stat.xlsx' contains the statistics of the Pokemons.
- The file 'pokemon_abilities.xlsx' contains the abilities of the Pokemons as booleans.
- In the file 'clustering.ipynb', I used a k-mean algorithm to classify my Pokemons through different clusters.
- The file 'pokemon_cluster.csv' contains the cluster of the Pokemons.
- 'battle_simulator_poke_abilities.ipynb' is the new battle simulator. It takes into account the abailities and the Pokemon uses the best type and the best offensive statistics depending his opponent to maximize the damages. The results are exported in the file 'result_abilities.csv'.
- 'Enrich_the_data.ipynb' adds the win_rate and create the file 'poke_data.csv' which is ready to be analyzed.

'Web_scrapper.py' is a web scrapper using Beautiful Soup. It doesn't work for the moment.


You can find informations and my diary on this project on my notion :  
https://mathieumarchand.notion.site/Pokemon-RPG-Data-English-Version-a4e7fccb01334b09a4cbfd91903bf186

Enjoy!
