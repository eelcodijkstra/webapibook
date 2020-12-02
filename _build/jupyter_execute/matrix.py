# Matrix instant messaging

Matrix (https://matrix.org) is een *instant messaging* toepassing, te vergelijken met IRC, Slack, Telegram, WhatsApp en dergelijke.
Matrix onderscheidt zich van de andere berichtendiensten door het open karakter.
Niet alleen is de software open source, de toepassing is helemaal gericht op het onderling verknopen (federation) van berichtentdiensten. Je kunt met je eigen Matrix-server (Selenium) werken, als je dat wilt, en deze in het Matrix-netwerk op laten nemen.
Via *bridges* koppel je Matrix aan andere berichtendiensten, zoals IRC, Slack en dergelijke.

Daarnaast is de dienst goed beveiligd, met de mogelijkheid van end-to-end encryption.

> In Europa wordt Matrix op een aantal plaatsen door overheden ingezet als alternatief voor de commerciële aanbieders uit vooral de USA. Hiermee is het onder andere gemakkelijker om privacy en security af te dwingen zonder inmenging van buiten.

Je kunt Matrix ook combineren met audio- of videoverbindingen.

Voor Matrix zijn er verschillende *clients* beschikbaar. Hiervan is *Element* (https://element.io) wel de belangrijkste.


## Matrix terminologie

* *room*: de plek waar berichten over een bepaald onderwerp uitgewisseld worden; je kunt dit ook zien als een gesprek. Een room heeft een naam, bijvoorbeeld:  `+infvo-test:matrix.org`???
* *community*: een groep waaraan *rooms* en *users* gekoppeld kunnen zijn?? Bijvoorbeeld: `+infvo:matrix.org`
* *user*: een gebruiker geef je aan het een `@`, bijvoorbeeld `@infvobot:matrix.org`.

Ewn *room* heeft een verzameling gebruikers; sommige rooms zijn vrij toegankelijk, terwijl andere rooms alleen werken met uitgenodigde deelnemers (invited). Het deelnemen aan een room heet "join".

In de API's worden in plaats van de normale namen vaak IDs gebruikt. Deze kun je achterhalen via de API, of via het user interface (web of Element).

## Matrix API

De Matrix client-server API vind je op https://matrix.org/docs/api/client-server/.
Bij de uitleg vind je daar ook de mogelijkheid om queries uit te proberen.

Voor ons zijn de belangrijkste functies:

* https://matrix.org/docs/api/client-server/#!/Session32management/login: als resultaat van de login krijg je een *access token* dat je in de andere API-aanroepen gebruikt voor authenticatie.
* 

Voordat je via de API de berichten in een 

## Login en token

Voor de authenticatie van de API-requests heb je een *access token* nodig.
Dit kun je krijgen door een login-request, waarbij je username en password nodig hebt.

> Je kunt dit access token vergelijken met een cookie dat de HTTP-server bij de browser achterlaat,
  nadat een gebruiker ingelogd heeft. Dit cookie wordt dan met alle volgende requests vanuit de browser
  naar de server gestuurd. Dit fungeert dan als authenticatie van deze volgende requests. 

import requests
import urllib

matrix_username = input("Matrix username: ")
matrix_password = input("Matrix password: ")
msgnr = 1

request_data = {
  "identifier": {
    "type": "m.id.user",
    "user": "infvobot"
  },
  "initial_device_display_name": matrix_username,
  "password": matrix_password,
  "type": "m.login.password"
}

r = requests.post('https://matrix.org/_matrix/client/r0/login', json=request_data)

Als de query succesvol is (code 200), dan vinden we het access_token in het resultaat.
Dit access-token gebruiken we in de volgende API-aanroepen voor de authenticatie en autorisatie.

if r.status_code == 200:
    display(r.json())
    access_token = r.json()['access_token']
else:
    display(r.status_code)
    access_token = "no-access-token"

## Room en room_id

Voordat een gebruiker berichten kan plaatsen in een *room*, moet deze eerst toegang krijgen.
Voor besloten *rooms* betekent dit dat de gebruiker uitgenodigd moet worden (*invite*),
waarna de gebruiker deel kan nemen in de room (*join*).

We gaan er hieronder vanuit dat de betreffende gebruiker toegang heeft tot de room.
In Element vind je de room_id via de (...)room-options->instellingen->geavanceerd.

room_id = "!ZxQixdOxFLFZDVEFam:matrix.org"

## Sturen van een bericht

Als eerste stap versturen we een bericht naar de betreffende *room*.
Berichten worden genummerd om ervoor te zorgen dat eenzelfde bericht maar één keer geplaatst wordt,
ook als dit meermalen verstuurd wordt. (*idempotent* gedrag). 
Berichten met een lager nummer dan het laatst ontvangen nummer worden niet geplaatst.
(Dit geeft bovendien bescherming tegen "replay attacks"?)



msgnr = msgnr + 1
msg = {
  "msgtype": "m.text",
  "body": "Hallo! Hier is " + matrix_username
}
url1 = "https://matrix.org/_matrix/client/r0/rooms/{roomid}/send/m.room.message/{txnr}?access_token={token}".format(
          roomid = room_id, txnr = str(msgnr), token = access_token
       )
url1



snd = requests.put(url1, json=msg)
if snd.status_code == 200:
    event_id = snd.json()["event_id"]
    display(event_id)
else:
    display(snd.status_code)

## Ontvangen van berichten

url2 = "https://matrix.org/_matrix/client/r0/rooms/{roomid}/context/{eventid}?access_token={token}".format(
          roomid = urllib.parse.quote(room_id), 
          eventid = urllib.parse.quote(event_id), 
          token = access_token
       )
url2

r2 = requests.get(url2)

r2.json()

Verwerken van deze context: filteren van relevante berichten. (NB: deze berichten staan in omgekeerde volgorde.)

> ??Kunnen we de tijd hierbij vermelden?

context = r2.json()
for msg in context["events_before"]:
    if msg["type"] == "m.room.message":
        print(msg["sender"], ": ", msg["content"]["body"])

Het eigenlijke protocol is om eerst "sync" te gebruiken: dit geeft de toestand voor alle verbonden rooms.
De volgende berichten kun je dan per room opvragen via "messages".
Daarbij geef je steeds de eventid mee van het laatst ontvangen bericht ("prev batch").

url3 = "https://matrix.org/_matrix/client/r0/sync?access_token={token}".format(
          token = access_token
       )
url3

r3 = requests.get(url3)
if r3.status_code == 200:
    display(r3.json())
    result = r3.json()
    next_batch = r3.json()["next_batch"]
else:
    display(r3.status_code)
    

NB: ik heb de `prev_batch` van de betreffende room nodig...

result = r3.json()

result["rooms"]["join"][room_id]["timeline"]["prev_batch"]

events = result["rooms"]["join"][room_id]["timeline"]["events"]
for event in events:
    if event["type"] == "m.room.message":
        print(event["sender"], ": ", event["content"]["body"])

