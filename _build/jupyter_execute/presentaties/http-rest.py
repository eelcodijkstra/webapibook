# REST API's

REpresentational State Transfer

* resource: "ding" (concreet/abstract/fysiek/virtueel)
* URL: Uniform Resource Locator: identificatie van resource
* representation (document): beschrijft toestand van resource
* methods: voor opvragen en veranderen van resource-toestand
    * GET, POST, PUT, DELETE, PATCH, ...
    
REST is verzameling afspraken/principes,
passend bij het web.

## HTTP methods 

* *idempotent*: geen verschil tussen 1x en vaker
* belangrijk bij onbetrouwbare communicatie/uitvoering    
    
| method | toestand?            | idempotent? |
| :--    | :--                  | :--         |
| GET    | onveranderd          | ja          |
| POST   | veranderd            | nee         |
| PUT    | veranderd            | ja          |
| DELETE | veranderd            | ja          |    

## CRUD

* methods voor collectie van *things*
* en voor individuele *things*

| method | `/things`            | `/things/id`            |
| :--    | :--                  | :--                     |
| GET    | get all things (ids) | get state of thing `id` |
| POST   | create new thing     | -                       |
| PUT    | -                    | set/update thing `id`   |
| DELETE | -                    | delete thing `id`       |

## Voorbeeld: Trello

https://trello.com

Begrippen:

* boards
* lists (per board)
* cards (per list)
* actions; users; organizations; ...

Trello API: https://developer.atlassian.com/cloud/trello/

## Importeren Python libraries

import requests
import json

## Authenticatie/autorisatie

API-key: identificeert gebruiker

Genereren/ophalen via:

* https://trello.com/app-key/

api_key = input("API-key? ")

## API-token

API-token fungeert als username/password

Genereren via:

url = "https://trello.com/1/authorize?expiration=1day&name=MyTestToken&scope=read,write&response_type=token&key=" + api_key
print(url)

token = input("token? ")

## Opvragen van borden

`parameters` zijn de parameters achter het `?`

`fields` geeft aan welke velden in het resultaat nodig zijn.

parameters = {
   'key': api_key,
   'token': token,
   'fields': 'name,id'
}

response = requests.get(
   "https://api.trello.com/1/members/me/boards",
   headers={"Accept": "application/json"},
   params=parameters
)
response.status_code

boards = response.json()
boards

for board in boards:
    print(board["name"], " - ", board["id"])

boards[-1]

## Opvragen van lists

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

lists = response.json()
lists

## Opvragen van de cards van een list

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

## Bepaal lijsten


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

list_ids = {}
for elem in my_lists:
    print(elem)
    name = elem["name"]
    list_ids[name] = elem["id"]

list_ids["To Do"]

## Nieuwe card in To Do list

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

## Move card to Doing list

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

## Delete card


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

------

Nu zelf aan de slag...