# Voorbeeld: Trello

Trello ([https://trello.com](https://trello.com)) is een web-toepassing waarin je met borden, lijsten en kaartjes een planning kunt maken. Trello heeft een web-API waarmee je deze toepassing kunt besturen. Via dit web-API kan Trello met extra functionaliteit uitgrebreid worden ("power-ups"), en zijn er verbindingen ("integrations") met andere toepassingen mogelijk.

In dit hoofdstuk geven we een inleiding in het gebruik van deze web-API.
We vragen borden, lijsten en kaartjes op; en maken een bord aan, met daarop een kaartje, dat we van de ene lijst naar de andere verplaatsen. En we ruimen het bord weer op.

## Trello begrippen

Een Trello-bord (board) bestaat uit een serie lijsten (lists); elke lijst bestaat uit een serie kaartjes (cards). Op de kaartjes kun je allerlei informatie plaatsen, en je kunt de kaartjes van de ene lijst naar de andere verplaatsen. Vaak-gebruikte lijsten zijn "To Do", "Doing", en "Done". 

Andere Trello-begrippen zijn actions, attachments, organizations, enz. In dit materiaal gaan we daar niet verder op in. 

De beschrijving van de Trello API vind je op https://developer.atlassian.com/cloud/trello/

## Importeren Python libraries

Voor het gebruik van de Trello API hebben we de Python-libraries `requests` en `json` nodig.

```{admonition} Tip: uitvoeren van de opdrachten
:class: tip
Je kunt de onderstaande opdrachten uitvoeren in een Jupyter Notebook.
Klik daarvoor op de Binder-knop hierboven. Er wordt dan een server opgestart met dit hoofdstuk als interactief Notebook.
```

import requests
import json

## Authenticatie/autorisatie

Voor het gebruik van Trello via de normale user interface moet je inloggen, met een gebruikersnaam en wachtwoord. Op dezelfde manier moet je je identificeren en authenticeren bij het gebruik van de web-API. Daarvoor zijn twee onderdelen nodig: de Api-key, die gekoppeld is aan de ontwikkelaar (script-programmeur), en een token, dat gekoppeld is aan de gebruiker/borden, met de nodige toegangsrechten (autorisatie). 

* Je Api-key kun je ophalen (nadat je eerst ingelogd bent bij Trello) via: https://trello.com/app-key/
* De waarde die je daar vindt vul je in als invoer voor de volgende cel (eerst uitvoeren: shift-return, dan invoer geven, met return; daarna met pijltjes naar volgende cel).

api_key = input("API-key? ")

## API-token

Het API-token geeft toegang tot de borden van de gebruiker. Via de onderstaande URL vraag je een token aan voor je eigen borden. Daar moet je toestemming voor geven.

Je kunt de URL eventueel aanpassen: de URL hieronder geeft toestemming voor 1 dag, voor lezen en schrijven. Je kunt ook eerst werken met alleen lezen, maar voor de latere opdrachten heb je ook schrijfrechten nodig.

* Voer eerst de cel hieronder uit; deze geeft een URL
* Klik op die URL: daarmee krijg je een scherm waarin je toestemming moet geven voor toegang tot je borden.
* Nadat je toestemming gegeven hebt krijg je een scherm met het token; kopieer dit token (Copy).

url = "https://trello.com/1/authorize?expiration=1day&name=MyTestToken&scope=read,write&response_type=token&key=" + api_key
print(url)

* Voer de onderstaande cel uit, en vul (Paste) het token in bij de invoer.
* Ga met de pijltjes naar de volgende cel.

token = input("token? ")

## Opvragen van borden

Als eerste stap vraag je de beschikbare borden op.
In de URL moet je de api_key en het token meegeven, voor de authenticatie/autorisatie.
Daarnaast kun je (via `field`) aangeven welke velden je wilt hebben van de bord-objecten:
er zijn heel veel velden, maar meestal ben je maar in een paar geïnteresseerd.

Deze gegevens geef je als `parameters` mee achter het `?` in de URL: daar zorgt de `requests` library voor.

* voer de volgende twee cellen uit;
* als de status_code 200 is, dan is de opdracht geslaagd; anders is er mogelijk iets mis met de key/token combinatie.

parameters = {
   'key': api_key,
   'token': token,
   'fields': 'name,id,url'
}

response = requests.get(
   "https://api.trello.com/1/members/me/boards",
   headers={"Accept": "application/json"},
   params=parameters
)
response.status_code

* Als de status_code 200 is, dan is het resultaat beschikbaar in JSON-formaat:

boards = response.json()
boards

for board in boards:
    print(board["name"], " - ", board["id"])

* Het laatste bord in de lijst:

boards[-1]

## Opvragen van lists

* De volgende stap is het opvragen van de lijsten van één van de borden, bijvoorbeeld het laatste bord uit het overzicht. (Pas dit eventueel hieronder aan.)

board_id = boards[-1]["id"]

parameters = {
   'key': api_key,
   'token': token,
   'fields': 'name,id' 
}

response = requests.get(
   "https://api.trello.com/1/boards/{id}/lists".format(
       id = board_id
   ),
   headers={"Accept": "application/json"},
   params=parameters
)
response.status_code

* Als de status_code 200 is, is het resultaat als JSON beschikbaar:

lists = response.json()
lists

## Opvragen van de cards van een list

* De kaarten van de eerste lijst vraag je op met de URL `/lists/{id}/cards`, waarin `{id}` de identificatie van deze eerste lijst is:

list_id = lists[0]["id"]

parameters = {
   'key': api_key,
   'token': token,
   'fields': 'name,id' 
}

response = requests.get(
   "https://api.trello.com/1/lists/{id}/cards".format(
       id = list_id
   ),
   headers={"Accept": "application/json"},
   params=parameters
)
response.status_code

cards = response.json()
cards

## Opvragen van een card

* Met de volgende opdracht haal je de gegevens van het eerste kaartje uit de lijst op.
* Pas eventueel de lijst met velden aan die je van dit kaartje wilt zien.

card_id = cards[0]["id"]

parameters = {
   'key': api_key,
   'token': token,
   'fields': "name,desc,id,url"
}

response = requests.get(
   "https://api.trello.com/1/cards/{id}".format(
       id = card_id
   ),
   headers={"Accept": "application/json"},
   params=parameters
)
response.status_code

my_card = response.json()
my_card

**Opdracht**

* Zoek uit welke velden beschikbaar zijn voor een card (zie de API-beschrijving).
* Voeg twee velden toe in bovenstaande code, en voer de opdracht nog een keer uit.

## Een nieuw board

Maak een nieuw board aan, met de default-lijsten: 

* To Do, Doing, Done

parameters = {
   'key': api_key,
   'token': token,
   'name': "API test board"
}

response = requests.post(
   "https://api.trello.com/1/boards",
   headers={"Accept": "application/json"},
   params=parameters
)
response.status_code

my_board = response.json()
my_board

**Opdracht (2e ronde)**

Voer deze opdracht uit nadat je alle onderstaande opdrachten uitgevoerd hebt, en het bord weer opgeruimd is.

* Zoek uit hoe je in de API de lijsten van een nieuw bord aangeeft.
* Maak een nieuw bord aan met de lijsten: `Backlog`, `To Do`, `Doing`, `Testing`, `Done`

## Bepaal lijsten

* Vraag de lijsten van het nieuwe bord op.

parameters = {
   'key': api_key,
   'token': token,
   'fields': 'name,id' 
}

response = requests.get(
   "https://api.trello.com/1/boards/{id}/lists".format(
       id = my_board["id"]
   ),
   headers={"Accept": "application/json"},
   params=parameters
)
response.status_code

my_lists = response.json()
my_lists

## Lists in Python dictionary

Om deze lijsten beter te kunnen hanteren maken we hiervan een Python dictionary, zodat je de identificatie van een lijst via de naam kunt vinden, bijvoorbeeld `list_ids["Done"].

* zet het resultaat om in een Python dictionary `list_ids`.

list_ids = {}
for elem in my_lists:
    print(elem)
    name = elem["name"]
    list_ids[name] = elem["id"]

list_ids["To Do"]

## Nieuwe card in To Do list

We kunnen nu een nieuw kaartje aanmaken in de lijst "To Do".
Voor dit nieuwe kaartje kunnen we allerlei gegevens invullen; we beperken ons hier tot de naam, beschrijving en positie in de lijst.

* Maak een nieuwe kaart aan in de lijst "To Do".

parameters = {
   'key': api_key,
   'token': token,
   'name': "A new card",
   'desc': "A card generated via the API",
   'pos': 'top',
   'idList': list_ids["To Do"]
}

response = requests.post(
   "https://api.trello.com/1/cards",
   headers={"Accept": "application/json"},
   params=parameters
)
response.status_code

new_card = response.json()
new_card

**Opdracht (2e ronde)**

* zoek uit in de API-beschrijving welke gegevens je allemaal op een kaartje kunt invullen
* maak nog een kaartje aan in dezelfde lijst, met een andere naam, en met één of meer labels.

## Move card to Doing list

Voor het wijzigen (update) van een kaartje gebruik je de method `PUT`.
In de parameters geef je de velden aan die je wilt veranderen.

* Verplaats de card door een andere `idList` op te geven.

parameters = {
   'key': api_key,
   'token': token,
   'idList': list_ids["Doing"]
}

response = requests.put(
   "https://api.trello.com/1/cards/{id}".format(
       id = new_card["id"]
   ),
   headers={"Accept": "application/json"},
   params=parameters
)
response.status_code

new_card = response.json()
print(new_card["url"])

**Opdracht (2e ronde)**

* Zoek in de API-beschrijving uit welke velden je op een card kunt aanpassen.
* Verander tenminste 1 ander veld op het kaartje

## Delete card

Soms moet je een kaartje verwijderen. Dat kan met de `DELETE` method.

* Verwijder het kaartje dat je zojuist aangemaakt hebt.

parameters = {
   'key': api_key,
   'token': token
}

response = requests.delete(
   "https://api.trello.com/1/cards/{id}".format(
       id = new_card["id"]
   ),
   headers={"Accept": "application/json"},
   params=parameters
)
response.status_code

## Delete board

Je kunt nu het bord weer opruimen, met een `DELETE` voor het bord.

* Verwijder het bord

parameters = {
   'key': api_key,
   'token': token
}

response = requests.delete(
   "https://api.trello.com/1/boards/{id}".format(
       id = my_board["id"]
   ),
   headers={"Accept": "application/json"},
   params=parameters
)
response.status_code

## Volgende opdrachten

**2e ronde**: voer de opdrachten vanaf het aanmaken van een nieuw bord opnieuw uit, en voer daarbij de opdrachten uit die gelabeld zijn met "2e ronde".

**3e ronde**: zoek uit wat er nog meer mogelijk is met de Trello API, bijvoorbeeld op het gebied van Actions, en maak daarbij je eigen API-requests.



