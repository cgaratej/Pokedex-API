import tkinter as tk
import requests
from Pokemon import pokemon
from PIL import ImageTk, Image
from io import BytesIO

URL = 'https://pokeapi.co/api/v2/pokemon?limit=1000'
pokeDict={}

window = tk.Tk()
window.geometry("250x360")

Titel = tk.Label(window, text="Pokedex", bg = "black", foreground= "white", font="20")
Titel.pack(fill = tk.X)
card = tk.Frame(window, bd=2, relief=tk.SOLID)
card.pack(padx=10, pady=10)
text = tk.Label(window, text="Search pokemon by name")
text.pack()
NameSearch = tk.Entry(window)
NameSearch.pack()

#Cuando demos la tecla enter nos haga la busqueda
def on_enter(event):
    SearchforPokémon(NameSearch.get().lower())

NameSearch.bind("<Return>", on_enter)
btnSearch = tk.Button(window, text="Search", command= lambda: SearchforPokémon(NameSearch.get().lower()))
btnSearch.pack()

labelName = tk.Label(card)
stats = tk.Frame(card)
labelAttack = tk.Label(stats)
labelDefense = tk.Label(stats)
labelSpeed = tk.Label(stats)
    
response = requests.get(URL)
payload = response.json()
results = payload.get('results', [])

def CreteDicionari():
    for pokemons in results:
        pokeName = pokemons['name']
        pokeUrl = pokemons['url']
        pokeDict.update({pokeName : pokeUrl})

CreteDicionari()

def CreateVisual(newPokemon):

    #Descargar la imagen de una url
    response = requests.get(newPokemon.GetUrlImg())
    img_data = response.content

    #Optner la imagen descargada
    img = Image.open(BytesIO(img_data))
    img = img.resize((150, 150))
    img_tk = ImageTk.PhotoImage(img)

    #Poner la imagen en un label
    label_img = tk.Label(card, image=img_tk)
    label_img.image = img_tk

    #Obtener los datos del pokemo desde la clase
    labelName["text"] = newPokemon.GetName(), newPokemon.Gethp(),"hp"
    labelAttack["text"] = newPokemon.GetAttack()
    labelDefense["text"] = newPokemon.GetDefence()
    labelSpeed["text"] = newPokemon.GetSpeed()

    label_img.grid(row=0, column=1)
    labelName.grid(row=1, column=1)
    stats.grid(row=2, column=1)

    attackNom = tk.Label(stats, text="Attack")
    attackNom.grid(row=1, column=0)
    defenseNom = tk.Label(stats, text="Defense")
    defenseNom.grid(row=1, column=1)
    speedNom = tk.Label(stats, text="Speed")
    speedNom.grid(row=1, column=2)
    
    labelAttack.grid(row=0, column=0)
    labelDefense.grid(row=0, column=1)
    labelSpeed.grid(row=0, column=2)

    #Imprimir el tipo del pokemon
    i = 1
    typeNom = tk.Label(stats, text="Type:")
    typeNom.grid(row=2, column=0)
    for type in newPokemon.GetType():
        labelType = tk.Label(stats, text=type)
        labelType.grid(row=2, column=i)
        i += 1

def SearchforPokémon(idPokemon):

    #Buscamos en el dicionario si exite el pokemon
    newRequest = requests.get(pokeDict[idPokemon])
    newResult = newRequest.json()

    #Optener los datos del pokemon desde la Api
    namePokemon = newResult["name"]
    hpPokemon = newResult['stats'][0]['base_stat']
    attackPokemon = newResult['stats'][1]['base_stat']
    defencePokemon = newResult['stats'][2]['base_stat']
    speedPokemon = newResult['stats'][5]['base_stat']
    urlImg = newResult['sprites']['other']['official-artwork']['front_default']
    types = newResult.get("types", [])

    arryaTypes = []
    for type in types:
        arryaTypes.append(type.get("type").get("name"))
    
    newPokemon = pokemon(namePokemon, hpPokemon, attackPokemon, defencePokemon, speedPokemon, urlImg, arryaTypes)

    CreateVisual(newPokemon)
    window.update()

window.mainloop()