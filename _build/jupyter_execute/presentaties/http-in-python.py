# Inleiding web-API's in Python

## Web voor mensen

<img src="../images/iot-client-server-0.png" alt="client-server"  width="600px" >

* web voor mensen: browser als client
* HTML als web-taal (payload)


## Web voor toepassingen

<img src="../images/iot-web-api-1.png" alt="web-api-server"  width="600px">

* web voor computers/toepassingen: toepassing als client
* basis voor het programmeerbare web
* JSON en XML in plaats van HTML

## Python requests

Python `requests` library:
    
vanuit Python-programma HTTP-requests versturen

en verwerken van het resultaat

=> scripting van een toepassing met web-api


import requests

## Voorbeeld

Voorbeeld: i&i website

r = requests.get('https://ieni.org')

r.status_code

r.text[0:500]

## Headers: metadata
    
    * `Content-type`: type van de payload

for header in r.headers:
    print(header)

r.headers['Content-Type']

## Andere request-mogelijkheden

* methods: GET, POST, PUT, DELETE, enz.
* JSON als payload
* parameters (in URL): aap/noot?key1=value1&key2=value2
* parameters in payload (JSON)

## JSON: JavaScript Object Notation
    
text-vorm van object, voor communicatie, opslag, enz. 

Python object (dict) <-> string (JSON)

import json

* `str = json.dumps(obj)` - van object naar string
* `obj = json.loads(str)` - van string naar object

mytodo = {"text": "Boodschappen supermarkt", "done": 0}
mytodo ["text"]

mytodo_string = json.dumps(mytodo)
mytodo_string

json.loads(mytodo_string)

## Voorbeeld: todo's

Simpele todo-app op glitch.com

todo_app = "https://shadowed-alder.glitch.me"

r1 = requests.get(todo_app + "/todos")
r1.status_code

`r.json()`: zet payload JSON om in object

r1.text

r1.json()

## GET: read(1)

r2 = requests.get(todo_app + "/todos/2")
r2.status_code

mytodo = r2.json()
mytodo

## PUT: update

mytodo['done'] = 1
r3 = requests.put(todo_app + "/todos/2", data=mytodo)
r3.status_code

r3.json()

## POST: create

* POST op collection levert id van nieuwe todo

newtodo = {'text': 'Huiswerk maken!', 'done': 0}
r4 = requests.post(todo_app + "/todos", data=newtodo)
r4.status_code

r4.json()

todo_id = r4.json()["id"]

## GET: read(2)

r5 = requests.get(todo_app + "/todos/{id}".format(
        id = todo_id
     ))
r5.status_code

r5.json()

## DELETE

r5 = requests.delete(todo_app + "/todos/{id}".format(
       id = todo_id
     ))
r5.status_code

r5.json()

## Authenticatie en autorisatie

openweathermap_key = 'vulhierjekeyin'
api_url = 'https://api.openweathermap.org/data/2.5'
url = api_url + '/weather?q={city},{country}&appid={key}'.format(
        city = "Amsterdam",
        country = "nl",
        key = openweathermap_key
      )
rw = requests.get(url)
rw.status_code

rw.json()