# Mailchimp

Mailchimp is een programma voor het versturen van mails aan groepen, bijvoorbeeld nieuwbrieven of marketing mails.

Mailchimp houdt bij of de ontvangen mails ontvangen en geopend worden (en gelezen?).


import requests
import json

## Mailchimp begrippen

## Mailchimp API

De (marketing) API van Maichimp is beschreven op: https://mailchimp.com/developer/.
Een goed beginpunt is de https://mailchimp.com/developer/guides/marketing-api-quick-start/.
Hier staat ook beschreven waar hoe je aan een API key komt.

* API reference: https://mailchimp.com/developer/api/marketing/

### API keys

Als je ingelogd bent brengt de url https://us10.admin.mailchimp.com/account/api/ je naar de pagina met API keys.

Let op: via de API-key heeft een toepassing volledig toegang tot de account-gegevens. Zorg ervoor dat deze keys niet in verkeerde handen vallen, en beschouw deze als een username/password combinatie.

Tip: maak per soort gebruik of per toepassing een aparte API key aan. Dan kun je deze ook per gebruik of toepassing weer verwijderen zonder dat dit voor de andere toepassingen gevolgen heeft.


api_key = input("Mailchimp API-key? ")

## Server

Je account is gebonden aan een server; deze server moet je ook opgeven in de API URL.
Je vindt deze server in de URL in de browser als je ingelogd bent.
Bijvoorbeeld: https://us10.admin.mailchimp.com betekent dat je server `us10` gebruikt.
De API-server is dan: `https://us10.api.mailchimp.com`.

mailchimp_server = 'us10'

### Eerste test

De Mailchimp-API heeft een `ping` test om te controleren of alles werkt.

url = "https://{server}.api.mailchimp.com/3.0/ping".format(
        server = mailchimp_server
      )
url

r = requests.get(url, auth=("user", api_key))
r.status_code

r.json()

## Lists

url1 = "https://{server}.api.mailchimp.com/3.0/lists".format(
        server = mailchimp_server
      )
url1

parameters = {"fields": "lists.id,lists.name,lists.stats.member_count"}
r1 = requests.get(url1, auth=("user", api_key), params=parameters)
r1.status_code

r1.json()

## List members

In principe krijg je erg veel gegevens per member. Het is daarom nodig om expliciet op te geven welke gegevens je wilt hebben.
Dit doe je met de parameter `fields`, met de lijst met veldnamen gescheiden door komma's. sub-veldnamen geef je aan met de "dot-notation".


parameters = {"fields": "members.id,members.email_address,members.merge_fields", 
              "count": 20,
              "offset": 0
             }

list_id = "2652a3638d"
url2 = "https://{server}.api.mailchimp.com/3.0/lists/{listid}/members".format(
        server = mailchimp_server,
        listid = list_id
      )
url2

r2 = requests.get(url2, auth=("user", api_key), params=parameters)
r2.status_code

r2.json()

## Python library

Er is een Python library voor Mailchimp. Deze maakt het gebruik van de API wat gemakkelijker.

* https://github.com/mailchimp/mailchimp-marketing-python
* installeren: 

