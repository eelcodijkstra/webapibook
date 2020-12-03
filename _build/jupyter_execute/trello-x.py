# Trello: plannen met kaartjes

Trello is een handige toepassing gebaseerd op het model van een planbord met kaartjes.
Dit kun je onder andere gebruiken voor een *kanban*" planning.

Trello heeft een REST API waarmee je de toepassing kunt besturen.
Daarnaast kun je *webhooks* opgeven waarmee Trello bepaalde gebeurtenissen naar externe diensten kan signaleren.
Bovendien heeft Trello de mogelijkheid om gegevens van andere toepassingen te bewaren,
en om buttons voor de besturing van andere toepassingen in het user interface op te nemen.
Dit zorgt ervoor dat Trello uitbreidbaar is, via "power-ups":
een soort apps op basis van Trello.
Ook kan Trello hiermee gekoppeld worden aan andere toepassingen ("integrations"),
bijvoorbeeld een berichtendienst als Slack, agenda's en andere takenlijsten.


## Concepten en terminologie

Een bord (*board*) bestaat uit een reeks lijsten (*lists*) of kolommen.
Elke lijst bevat 0 of meer kaartjes (*cards*).
Elk bord, lijst of kaartje heeft een naam.

Een kaartje kan allerlei gegevens bevatten, onder meer een todo-lijst.
We gaan hier niet verder in de details op kaartjes.

## Notebook initialisatie

import requests
import json

## Trello API

De gegevens van het Trello API vind je op: https://developer.atlassian.com/cloud/trello/rest/.
        

## Authenticatie en autorisatie: API-key en tokens

Om de Trello API te kunnen gebruiken heb je een *token* nodig.
De beschrijving van de authenticatie en autorisatie vind je op https://developer.atlassian.com/cloud/trello/guides/rest-api/authorization/
De stappen hieronder zijn een uitwerking daarvan.

### API-key

Elke Trello-gebruiker heeft een API-key. Dit is een identificatie van de gebruiker voor de API.
Deze key heb je onder andere nodig om een *token* aan te vragen.

* log in bij Trello, en zoek je API-key op via: https://trello.com/app-key/
* vul je API-key hieronder in (voer de cel hieronder uit):

api_key = input("API-key? ")

### Token

Voor deze oefening gebruik je een tijdelijk token.
Dit vraag je aan via een URL in de browser.
We maken eerst deze URL aan via Python, met behulp van je API-key.

* maak de URL aan (voer de cel hieronder uit)
* klik op de URL die als uitvoer verschijnt, en geef via de geopende webpagina toestemming voor het token
* kopieer ("Copy") het token uit die webpagina om deze straks hieronder in te vullen

url = "https://trello.com/1/authorize?expiration=1day&name=MyTestToken&scope=read,write&response_type=token&key=" + api_key
print(url)

* vul het token hieronder in (voer de cel hieronder uit en "Paste"), voor gebruik in de volgende opdrachten.

token = input("token? ")

## Borden

Vraag de namen van je borden op (als je die hebt), met hun ID's.
Deze ID's heb je later nodig in de API.



Geef op welk bord je in de volgende opdrachten wilt gebruiken:

## Lijsten

Vraag de lijsten op n

### Maak een nieuw bord aan

bordnaam = "API-testbord"


url = "https://api.trello.com/1/members/me/boards"

headers = {
   "Accept": "application/json"
}

query = {
   'key': api_key,
   'token': token
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query
)

response

boards = response.json()

for board in boards:
    print(board["name"], " - ", board["id"])

url1 = "https://api.trello.com/1/board/" + "52493e119ba1b91046002d9e" + "/lists"

response1 = requests.request(
   "GET",
   url1,
   headers=headers,
   params=query
)

response1

lists = response1.json()
for list in lists:
    print(list["name"], " - ", list["id"])

url2 = "https://api.trello.com/1/lists/" + "52493e119ba1b91046002d9f" + "/cards"
response2 = requests.request(
   "GET",
   url2,
   headers=headers,
   params=query
)

response2

response2.json()

cards = response2.json()
for card in cards:
    print(card["name"], " - ", card["id"])

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))?





### Maak nieuwe lijsten aan

Op dit bord maak je de lijsten aan: "Backlog", "ToDo", "Doing", "Testing", "Done", en "Archive"



response

api_key

token

## Opmerkingen

* in de code moeten we rekening houden met het resultaat van de response. Alleen als het resultaat "200" is, mogen we de inhoud (json) opvragen.
* kunnen we handig gebruik maken van Python format strings, voor het maken van de URLs?
* HTTP goed uitleggen, verschil tussen parameters en body/payload/

