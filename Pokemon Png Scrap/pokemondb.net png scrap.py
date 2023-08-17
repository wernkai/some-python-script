"""
Purpose: To auto download Pokemon pixel image in png from Pokemondb.net
"""
import requests
from bs4 import BeautifulSoup

url = 'https://pokemondb.net/pokedex/national'
data = requests.get(url).content
soup = BeautifulSoup(data, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
index = 1

table = soup.find('div', attrs = {'infocard-list infocard-list-pkmn-lg'}) 

for row in table.findAll('a', attrs = {'class':'ent-name'}):
    
    name = ''
    name = row.text

    urlImg = f'https://img.pokemondb.net/sprites/lets-go-pikachu-eevee/normal/{name.lower()}.png'
    img = requests.get(urlImg).content

    fname = str(index) + "_" + name
    f = open(f'C:\\Users\\username\\Desktop\\pokemon png\\{fname}.png','wb')
    f.write(img)
    f.close()
    index += 1