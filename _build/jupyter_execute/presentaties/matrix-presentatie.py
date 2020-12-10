# Matrix instant messaging

Matrix (https://matrix.org)

* instant messaging (vgl. IRC, Slacj, WhatsApp, ...)
* open: open source, zelf hosten van server
* federatie van Matrix-servers
* bridges naar andere IM-diensten
* App: https://element.io

# Matrix instant messaging

Matrix (https://matrix.org) is een *instant messaging* toepassing, te vergelijken met IRC, Slack, Telegram, WhatsApp en dergelijke.
Matrix onderscheidt zich van de andere berichtendiensten door het open karakter.
Niet alleen is de software open source, de toepassing is helemaal gericht op het onderling verknopen (federation) van berichtentdiensten. Je kunt met je eigen Matrix-server (Selenium) werken, als je dat wilt, en deze in het Matrix-netwerk op laten nemen.
Via *bridges* koppel je Matrix aan andere berichtendiensten, zoals IRC, Slack en dergelijke.

Daarnaast is de dienst goed beveiligd, met de mogelijkheid van end-to-end encryption.

> In Europa wordt Matrix op een aantal plaatsen door overheden ingezet als alternatief voor de commerciële aanbieders uit vooral de USA. Hiermee is het onder andere gemakkelijker om privacy en security af te dwingen zonder inmenging van buiten.

Je kunt Matrix ook combineren met audio- of videoverbindingen.

Voor Matrix zijn er verschillende *clients* beschikbaar. Hiervan is *Element* (https://element.io) wel de belangrijkste. Deze kun je in de browser gebruiken, als desktop-applicatie, of als mobiele app.

```{admonition} Meld je aan bij Matrix
Voor de volgende opdrachten is het nodig dat je een gratis Matrix-account aanmaakt via https://element.io.
Let op, je krijgt de bevestigingsmail van matrix.org; soms belandt deze in je spam-box.
Stuur als het gelukt is even een bericht naar `@eelcod:matrix.org`.
```

## Termen

* (chat)room: het gesprek - bijv. `#infvo-test:matrix.org`
* user - bijv. `@infvobot:matrix.org`
* community - bijv. `+infvo:matrix.org`

*room* heeft een verzameling *users*; vaak alleen op uitnodiging.

room_id: gebruikt in API in plaats van naam

## Matrix terminologie

* *room*: de plek waar berichten over een bepaald onderwerp uitgewisseld worden; je kunt dit ook zien als een gesprek. Een room heeft een naam, bijvoorbeeld:  `#infvo-test:matrix.org`
* *community*: een groep waaraan *rooms* en *users* gekoppeld kunnen zijn. Bijvoorbeeld: `+infvo:matrix.org`
* *user*: een gebruiker geef je aan met een `@`, bijvoorbeeld `@infvobot:matrix.org`.

Ewn *room* heeft een verzameling gebruikers; sommige rooms zijn vrij toegankelijk, terwijl andere rooms alleen werken met uitgenodigde deelnemers (invited). Het deelnemen aan een room heet *join*.

In de API's worden in plaats van de normale namen vaak IDs gebruikt. Deze kun je achterhalen via de API, of via het user interface (web of Element).

* https://www.snoyman.com/blog/2018/05/guide-to-matrix-riot

## Matrix API

Zie:  https://matrix.org/docs/api/client-server/

* POST /_matrix/client/r0/login
* PUT  /_matrix/client/r0/rooms/{id}/send/m.room.message/{nd}
* GET  /_matrix/client/r0/sync
* GET  /_matrix/client/r0/rooms/{roomID}/messages


## Matrix API

De Matrix client-server API vind je op https://matrix.org/docs/api/client-server/.
Bij de uitleg vind je daar ook de mogelijkheid om queries uit te proberen.

Voor ons zijn de belangrijkste functies:

* POST https://matrix.org/_matrix/client/r0/login: dit geeft als resultaat een *access token* dat je in de volgende API-aanroepen gebruikt voor authenticatie.
* PUT https://matrix.org/_matrix/client/r0/rooms/{roomID}/send/m.room.message/{txnr}: verstuur een bericht met volgnr *txnr* naar de genoemde *room*.
* GET https://matrix.org/_matrix/client/r0/sync: synchroniseer de ontvanger met de toestand van de verbonden *rooms*. 
* GET https://matrix.org/_matrix/client/r0/rooms/{roomID}/messages: de berichten sinds de vorige opvraging


## Login en token

Voor de authenticatie van de API-requests heb je een *access token* nodig.
Dit kun je krijgen door een login-request, waarbij je username en password nodig hebt.

> Je kunt dit access token vergelijken met een cookie dat de HTTP-server bij de browser achterlaat,
  nadat een gebruiker ingelogd heeft. Dit cookie wordt dan met alle volgende requests vanuit de browser
  naar de server gestuurd. Dit fungeert dan als authenticatie van deze volgende requests. 

## Login voor API-token

import requests
import json
import urllib

Om te voorkomen dat de username/password-combinatie in de code van het Jupyter Notebook opgenomen wordt, moet je deze invoeren bij het uitvoeren van de onderstaande cel. Voer de cel uit (Shift-Enter); voer dan de *username* in gevolgd door Return; en dan het *password* gevolgd door Return. Navigeer met de pijl naar beneden naar de volgende cel.

### Username en password

matrix_username = input("Matrix username: ")
matrix_password = input("Matrix password: ")
msgnr = 1

Volgens de API-beschrijving moet je onderstaande gegevens als data meesturen bij het login-request.

### Login-data

request_data = {
  "identifier": {
    "type": "m.id.user",
    "user": matrix_username
  },
  "initial_device_display_name": matrix_username,
  "password": matrix_password,
  "type": "m.login.password"
}

### Login: POST request

r = requests.post('https://matrix.org/_matrix/client/r0/login', json=request_data)

Als de query succesvol is (code 200), dan vinden we het access_token in het resultaat.
Dit access-token gebruiken we in de volgende API-aanroepen voor de authenticatie en autorisatie.

if r.status_code == 200:
    display(r.json())
    access_token = r.json()['access_token']
else:
    display(r.status_code)
    access_token = "no-access-token"

access_token

## Room en room_id

Voordat een gebruiker berichten kan plaatsen in een *room*, moet deze eerst toegang krijgen.
Voor besloten *rooms* betekent dit dat de gebruiker uitgenodigd moet worden (*invite*),
waarna de gebruiker deel kan nemen in de room (*join*).

We gaan er hieronder vanuit dat de betreffende gebruiker toegang heeft tot de room.
In Element vind je de room_id via de (...)room-options->instellingen->geavanceerd.

## Rooom_id

room_id = input("Room ID? ")
print("Ingevulde room_id: ", room_id)

## Sturen van een bericht

Als eerste stap versturen we een bericht naar de betreffende *room*.
Berichten worden genummerd om ervoor te zorgen dat eenzelfde bericht maar één keer geplaatst wordt,
ook als dit meermalen verstuurd wordt (*idempotent* gedrag). 
Berichten met een lager nummer dan het laatst ontvangen nummer worden niet geplaatst.

## Sturen van een bericht

Het bericht (tekst) met volgnr. en de URL:

msgnr = msgnr + 1
msg1 = {
  "msgtype": "m.text",
  "body": "Hallo! Hier is " + matrix_username
}
url1 = "https://matrix.org/_matrix/client/r0/rooms/{roomid}/send/m.room.message/{txnr}?access_token={token}".format(
          roomid = room_id, txnr = str(msgnr), token = access_token
       )
url1

### Send: PUT-request

snd = requests.put(url1, json=msg1)
if snd.status_code == 200:
    event_id = snd.json()["event_id"]
    display(event_id)
else:
    display(snd.status_code)

## Ontvangen van berichten

1. sync - geeft toestand (incl. history) van alle rooms
2. get messages - herhalen voor nieuwe berichten

Het ontvangen van berichten is nogal wat ingewikkelder dan het versturen van een bericht.
In principe kan er in de *timeline* van de *room* al een flinke lijst van berichten zijn die op dit moment nog niet ontvangen zijn. En tussen twee verzoeken om nieuwe berichten kunnen er meerdere berichten ontvangen zijn.

> Naast de ontvangen berichten bevat de *timeline* van een *room* ook andere *events*, zoals de *join* van een nieuwe gebruiker. Het hangt van je toepassing af of je dit soort *events* wilt verwerken. In de voorbeelden hieronder gaat het ons alleen om de ontvangen berichten.

De manier van het ontvangen berichten verloopt als volgt:

1. synchroniseer ("sync") de ontvanger met de server (dit geeft o.a. de waarde voor "prev_batch")
2. (herhaald) bijwerken van de ontvangen berichten (steeds "prev_batch" bijwerken)

Het eigenlijke protocol is om eerst "sync" te gebruiken: dit geeft de toestand voor alle verbonden rooms.
De volgende berichten kun je dan per room opvragen via "messages". Deze sync geeft ook de waarde voor "prev_batch" waarmee de volgende reeks ontvangen berichten begint.
Daarbij geef je steeds de *eventid* mee van het laatst ontvangen bericht ("prev_batch").

url2 = "https://matrix.org/_matrix/client/r0/sync?access_token={token}".format(
          token = access_token
       )
url2

r2 = requests.get(url2)
if r2.status_code == 200:
    display(r2.json())
    result = r2.json()
    prev_batch = result["rooms"]["join"][room_id]["timeline"]["prev_batch"]
else:
    display(r2.status_code)

prev_batch

Voor elke room is er een timeline met events.
Er zijn events voor het aanmaken van een room, voor het uitnodigen/join van gebruikers, enz.
Wij zijn hier alleen geïnteresseerd in de tekstberichten van type: "m.room.message".

## Berichten in de historie

events = result["rooms"]["join"][room_id]["timeline"]["events"]
for event in events:
    if event["type"] == "m.room.message":
        print(event["sender"], ": ", event["content"]["body"])

## Opvragen van nieuwe berichten

"messages" URL; bijwerken `prev_batch`

url3 = "https://matrix.org/_matrix/client/r0/rooms/{roomid}/messages?access_token={token}&from={prev}".format(
          roomid = room_id,
          token = access_token,
          prev = prev_batch
       )

r3 = requests.get(url3)
r3.status_code

result3 = r3.json()
result3

prev_batch = result3["end"]
prev_batch

### De nieuwe berichten

events = result3["chunk"]
for event in events:
    if event["type"] == "m.room.message":
        print(event["sender"], ": ", event["content"]["body"])

## Functie get_messages(last_msg)

resultaat: `(messages, last_msg)`

def get_messages(last_msg):
    global room_id, access_token
    url = "https://matrix.org/_matrix/client/r0/rooms/{roomid}/messages?access_token={token}&from={prev}".format(
          roomid = room_id,
          token = access_token,
          prev = last_msg
       )
    res = requests.get(url)
    if res.status_code != 200:
        return[]
    result = res.json()
    last_msg = result["end"]
    return (result["chunk"], last_msg)    

## Ophalen nieuwe berichten

Voor de volgende cel herhaald uit

(mesgs, prev_batch) = get_messages(prev_batch)
if mesgs == []:
    print("<no new messages>")
for event in mesgs:
    if event["type"] == "m.room.message":
        print(event["sender"], ": ", event["content"]["body"])

