# HTTP in Python

HTTP is een client-server protocol: de client, bijvoorbeeld de browser, stuurt een verzoek (*request*) naar de server,
die een antwoord (*response*) terug stuurt.
In ons geval is ons Python-programma (in dit notebook) de client. 

Met behulp van de `requests` library (https://requests.readthedocs.io) kun je in Python HTTP-verzoeken sturen
en de antwoorden verwerken.
Dit is de basis voor het gebruik van web-API's in Python.

Voordat we de library kunnen gebruiken moeten we deze importeren:

import requests

Het eenvoudigste HTTP-*request* is `get`, met een URL als parameter:

r = requests.get('https://ieni.org')

Aan de hand van de `status_code` kun je zien of de request geslaagd is, en een succesvolle response opgeleverd heeft.
De waarde `200` geeft succes aan; `404` is een niet-gevonden pagina; enz.

r.status_code

De *response* bevat onder meer de *headers* met metadata van de server.

for header in r.headers:
    print(header)

De `Content-type` header beschrijft het document-formaat van de response, in dit geval HTML:

r.headers['Content-Type']

We geven hier alleen een klein gedeelte van het ontvangen HTML-document weer:

r.text[0:500]

## Andere requests-mogelijkheden

Met de `requests`-library kun je onder andere:

* verzoeken versturen met verschillende HTTP-methods: naast `GET` ook `POST`, `PUT`, `DELETE`, enz.
* authenticatie/autorisatiegegevens meegeven (username/password)
* de headers die je opstuurt naar de server aanpassen
* de parameters in de URL opgeven (`...?key1=value1&key=value...`)
* de payload (data) opgeven voor een `POST` of `PUT`-request

Hieronder en in de andere notebooks kom je een aantal van deze mogelijkheden tegen.

## JSON

Zoals uit dit voorbeeld mogelijk blijkt, is HTML niet het meest handige formaat om in een programma te verwerken.
De meeste web-API's gebruiken daarom het JSON-formaat (JavaScript Object Notation, zie https://json.org).
JSON wordt veel gebruikt om "objecten" die je in programma's gebruikt buiten het programma te bewaren,
bijvoorbeeld in een document-database (zoals MongoDB of CouchDB);
en om objecten te communiceren naar andere programma's, zoals in web-API's.

De JSON-notatie lijkt sterk op de Python Dictionary notatie.
Voor het omzetten van een Python Dictionary naar en van JSON gebruiken we de functies `dumps` en `loads`: `string = json.dumps(object)` en `object = json.loads(string)`.

Voordat we deze functies kunnen gebruiken moeten we eerst de `json`-library importeren.

import json

In het voorbeeld hieronder maken we eerst een Python Dictionary aan:

mytodo = {"text": "Boodschappen supermarkt", "done": 0}
mytodo ["text"]

type(mytodo)

Via `json.dumps` zetten we dit om in een string (tekst).
Zo'n tekstformaat kun je zonder problemen communiceren of opslaan op een extern medium: je bent niet afhankelijk van een interne, binaire representatie.



mytodo_string = json.dumps(mytodo)
mytodo_string

Merk op dat deze string-representatie erg lijkt op de oorspronkelijke vorm.
Maar het is een gewone string, je kunt er geen velden in selecteren enz.

type(mytodo_string)

Met de functie `json.loads` zet je deze JSON stringwaarde om in een Python dictionary:

json.loads(mytodo_string)

* Ga na wat het type van het resultaat is van de vorige cel.
* Ga na dat je in dit resultaat het veld "done" kunt selecteren.



### JSON beperkingen

JSON heeft maar een beperkt aantal basis-types: number, string, boolean. 
Dit betekent dat je complexere basistypes zoals *datum* als string moet representeren.

## Voorbeeld HTTP met JSON

In dit voorbeeld gebruiken we een eenvoudige ToDo-toepassing.
Voor deze demonstratie hebben we deze beschikbaar gemaakt op `glitch.com`:
https://shadowed-alder.glitch.me/ .
Je kunt de broncode bekijken via: https://glitch.com/edit/#!/shadowed-alder?path=server.js

todo_app = "https://shadowed-alder.glitch.me"

Het volgende verzoek levert een JSON-document op met alle todo's:

r1 = requests.get(todo_app + "/todos")
r1.status_code

Zoals je ziet is het resultaat (de payload) een text in JSON-formaat:

r1.text

De requests-library heeft een ingebouwde JSON-decoder.
De functie `r1.json()` levert de Python-waarde (hier: list van dictionaries) als resultaat van de decodering.

r1.json()

We kunnen de gegevens van een enkele todo opvragen, door de `id` hiervan in de URL op te nemen:

r2 = requests.get(todo_app + "/todos/2")
r2.status_code

mytodo = r2.json()
mytodo

### PUT: update

Met een `PUT`-request kunnen we de toestand van deze todo veranderen, bijvoorbeeld `done` op 1 zetten.

mytodo['done'] = 1
r3 = requests.put(todo_app + "/todos/2", data=mytodo)
r3.status_code

r3.json()

### POST: create

Een nieuwe todo kunnen we aanmaken met een `POST` naar URL voor de verzameling todo's.
De `id` in het resultaat is de identificatie van de todo in de API.

newtodo = {'text': 'Huiswerk maken!', 'done': 0}
r4 = requests.post(todo_app + "/todos", data=newtodo)
r4.status_code

r4.json()

todo_id = r4.json()["id"]

r5 = requests.get(todo_app + "/todos/{id}".format(
        id = todo_id
     ))
r5.status_code

r5.json()

### Delete: delete

Met de `DELETE` http-method kunnen we een todo ook weer verwijderen.
De gebruiken de `id` van de zojuist aangemaakte todo.

r5 = requests.delete(todo_app + "/todos/{id}".format(
       id = todo_id
     ))
r5.status_code

r5.json()

## Authenticatie en autorisatie

Dit todo-voorbeeld is in één opzicht niet erg praktisch: iedereen kan deze lijst aanpassen.
In de praktijk zul je bij zo'n soort toepassing moeten inloggen, met een gebruikersnaam en wachtwoord.
Deze combinatie zorgt voor authenticatie: de server weet wie je bent, alleen jij kent deze combinatie (als het goed is ;-).
Impliciet zorgt dit ook voor autorisatie: je mag nu gebruik maken van de diensten die aan jouw naam gekoppeld zijn.

* authenticatie: ben jij wie je zegt dat je bent? Hoe kun je dat bewijzen?
* autorisatie: heb jij hiervoor toestemming?

Bij het gebruik van web-api's gebruik je vaak een API-key of een token dat de rol van de gebruikersnaam/wachtwoord vervult.
Je kunt als aangemelde gebruiker vaak zo'n key aanmaken. Wees erop bedacht dat je deze net zo vertrouwelijk moet behandelen als je gebruikersnaam/wachtwoord-combinatie!



## openweathermap

Via https://openweathermap.org kun je het actuele weer op een bepaalde lokatie ophalen.
Je moet daarvoor een gratis account aanmaken.
(Met een betaalde account krijg je meer mogelijkheden.)
De beschrijving van de API voor het huidige weer vind je via: https://openweathermap.org/current

In je account kun je een API-key aanmaken die je nodig hebt als authenticatie/autorisatie,
zie de tab API-keys (als je ingelogd bent).

openweathermap_key = 'vulhierjekeyin'
url = 'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={API_key}'.format(
        city = "Amsterdam",
        country = "nl",
        API_key = openweathermap_key
      )
rw = requests.get(url)

rw.status_code

rw.json()

