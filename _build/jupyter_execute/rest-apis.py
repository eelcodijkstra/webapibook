# REST API's

REST web-API's volgen een bepaalde stijl die aansluit bij de principes (*architectuur*) van het web.
Als je deze stijl kent, kun je redelijk snel begrijpen hoe een bepaald API in deze stijl werkt.

Naast REST zijn er ook andere stijlen van web-API's in gebruik, zoals RPC (remote procedure call) of SOAP (???).
Tegenwoordig wint de GraphQL-stijl aan populariteit. 
Daarmee kun je wat preciezer aangeven welke data je wilt ophalen via de API.



## REST

REST staat voor Representational State Transfer. (REF - wikipedia)
Dit is gebaseerd op het volgende model van het web:

* resource: dit is de web-term voor "ding"; dit kan zowel een concreet iets zijn, zoals een lamp; een persoon, zoals Rembrandt; of een abstract idee, zoals democratie.
* URI en URL: een resource kun je identificeren met een URI (uniform resource identifier) of een URL (uniform resource locator). Deze identificaties zijn context-onafhankelijk: overal waar je deze gebruikt heeft deze dezelfde betekenis. Het voordeel van een URL is dat deze ook aangeeft waar je meer over de resource kunt vinden.
    * voor gewone namen is dat niet het geval: de betekenis daarvan hangt sterk af van de context.  
* toestand (state) van een resource: een resource heeft een toestand. Deze toestand kun je beschrijven ("representeren") door middel van een document, bijvoorbeeld (in de context van het web) een HTML-document of een JSON-document. Bij een resource kun je verschillende documenten hebben die  de toestand beschrijven, afhnakelijk van de wensen van de gebruiker (bijvoorbeeld: HTML, in het Engels of in het Nederladnds; of JSON).
* door middel van een document (-aanpassing) kun je de toestand van de resource veranderen - als dat mogelijk is via dit interface.
* HTTP-methods: met behulp van de verschillende HTTP-methods kun je de toestand van een resource opvragen, aanpassen, een resource aanmaken of verwijderen. Daarbij is het belangrijk dat je de recht doet aan de normale betekenis van de HTTP-methods, zoals `GET` voor het opvragen van de toestand.

## Eigenschappen HTTP methods

In een REST API houd je rekening met de betekenis en eigenschappen van de HTTP-methods. 
(Er is niets dat dit gebruik afdwingt, maar dit zijn wel de aannames die overal in de web-infrastructuur gebruikt worden.)

* GET: idempotent; geen verandering in toestand van de resource
* POST: niet idempotent; (mogelijk) verandering in de toestand van de resource
* PUT: idempotent; verandering in de toestand
* DELETE: idempotent; verandering in de toestand

Eén van de gevolgen is dat je eenzelfde GET-operaties zonder problemen kunt herhalen. 
Voor een POST is dat niet het geval: de browser vraagt daarom bijvoorbeeld of je de opdracht nog een keer wilt uitvoeren. Het nogmaals opsturen van een formulier kan bijvoorbeeld betekenen dat je het artkel nog een keer bestelt.
De `PUT` en `DELETE` operaties zijn wel idempotent.

**idempotent: (tegen)voorbeelden**

* `i := 10` is idempotent en verandert de waarde (toestand) van `i`
* `i := i + 1` verandert de waarde van `i` op een niet-idempotente manier.
* op een afstandsbediening is het kiezen van NPO-1 idempotent,
* en het zappen naar de volgende zender niet idempotent

Idempotente operaties zijn vooral handig is de communicatie niet volledig betrouwbaar is (zoals in het web):
als je niet weet of een bericht overgekomen is, kun je dat zonder risico nog een keer sturen.

Nog een voorbeeld: een bediening van een lamp met twee knoppen, "aan" en "uit", is idempotent.
Dit soort knoppen vind je vaak bij IoT-apparaten, waarbij het niet altijd duidelijk is of een bericht niet aangekomen is,
of dat de verwerking wat langer duurt dan je verwacht.

## Collecties van resources

Vaak heb je te maken met een collectie van soortgelijke resources waarbinnen je de individuele resources wilt kunnen onderscheiden.
Een gebruikelijke manier is om de verzameling een naam te geven, en de elementen daarin een nummer als identificatie.

We gebruiken hier als naam voor een verzameling het *meervoud*, dus bijvoorbeeld: `lists`, of `cards`.
Een bepaalde lijst geven we dan bijvoorbeeld aan als: `lists/53`, een kaart als `cards/92`. Een kaart als onderdeel van een lijst: `lists/53/cards/11`. Dit laatste is een voorbeeld van een *geneste resource*.

> Sommige web-API's gebruiken enkelvoud in plaats van meervoud voor het benoemen van een collectie. Trello accepteert zowel meervoud (volgens de documentatie) als enkelvoud (als alternatief).

## Voorbeeld: lamp aan- en uitschakelen

Voor het aansturen van een lamp kun je de volgende API gebruiken:

* URL: `/lamps/17` - dit is de identificatie van de lamp (pad-gedeelte van de URL)
* 

Opmerking: in dit geval is de URL van de lamp lokaal: je gebruikt immers een lokaal netwerkadres.
Dit betekent dat je deze lamp niet wereldwijd op dezelfde manier kunt identificeren; maar misschien wil je dat ook niet.

## CRUD

In de database-wereld staat CRUD voor: create, read, update, delete. Dit zijn de basisoperaties op de elementen in een database.

Met behulp van een REST API kun je dit als volgt uitvoeren, voor een collectie van `things`.

| method | `/things`            | `/things/id`            |
| :--    | :--                  | :--                     |
| GET    | get all things (ids) | get state of thing `id` |
| POST   | create new thing     | -                       |
| PUT    | -                    | set/update thing `id`   |
| DELETE | -                    | delete thing `id`       |

