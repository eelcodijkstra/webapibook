# Het HTTP protocol

## Inleiding

HTTP (HyperText Transfer Protocol) is het protocol van het web. Het web is een toepassing van het internet.
In de internet protocol-stack is HTTP een *toepassingsprotocol*. HTTP maakt gebruik van TCP, voor betrouwbare bi-directionele verbindingen, eventueel aangevuld met TLS, voor versleutelde verbindingen.

HTTP is een *client-server* protocol. De client stuurt een request naar de server, die een response terugstuurt.

Voor de *adressering* gebruikt HTTP de URL: deze bevat, naast de naam van de server, het pad naar de betreffende *resource* (de "webpagina"). 

De *payload* in deze response is gewoonlijk een HTML-document; ook andere bestanden, zoals CSS, JavaScript en figuren (jpeg, png, enz.) kunnen als payload optreden.
De *headers* die meegegeven worden bij de client-server communicatie bevat de *metadata* bij het protocol, zoals bijvoorbeeld *cookies*.

## Client-server interactie

```{figure} images/iot-client-server-0.png
  :width: 600px
  :align: center

HTTP client-server interactie
```

Het web-protocol HTTP werkt op basis van client-server interacties:

* de browser, als client, stuurt een verzoek (request) naar de webserver,
  bijvoorbeeld een aanvraag voor een HTML-document.
  De URL in het request geeft aan welk document bedoeld wordt.
* de webserver stuurt een antwoord (response) terug naar de browser,
  met het gevraagde document.

De client-server interactie kun je vergelijken met een loket, bijvoorbeeld van een bank,
met een rij klanten die één voor één door de loketbeambte bediend worden.
De server krijgt allerlei request van verschillende clients door elkaar aangeboden,
en handelt deze onafhankelijk voor elkaar af.

Zoals we later zullen zien kunnen ook andere programma's als client van een webserver optreden:
dat vormt de basis voor het programmeerbare web.

## Adressering: URL

```{figure} images/http-url.png
:width: 600px
:align: center

Webadres: Uniform Resource Locator
```

Een webadres ofwel URL (Uniform Resource Locator) heeft de vorm: ``http://<host>:<poort><pad>``

* ``http:`` of ``https:`` - schema (protocol): HTTP of HTTPS;
* ``<host>`` - domeinnaam of IP-adres van de webserver, voor het IP-protocol;
* ``<poort>`` -nummer - TCP-poort; default: 80 voor HTTP, 443 voor HTTPS;
* ``<pad>`` - adres (bijv. bestandsnaam) van de *resource* binnen de server.

**Voorbeeld:** ``https://infvopedia.nl/demo/iot-app.html``

Voor een server in het publieke internet gebruik je meestal een domeinnaam,
zoals ``infvopedia.nl``.
De browser stuurt een verzoek naar de DNS-server om deze naam om te zetten in het bijbehorende IP-adres.
(Nog een voorbeeld van een client-server interactie.)
Het pad-gedeelte ``/demo/iot-app.html`` identificeert het HTML-document (bestand) op de server.

**Voorbeeld:** ``http://192.168.1.123/leds/0``

Dit is een voorbeeld van een IoT-knoop als webserver in een lokaal netwerk.
Een computer in een lokaal netwerk heeft meestal geen domeinnaam:
je gebruikt dan het IP-adres, zoals ``192.168.1.123``.
Het pad-gedeelte ``/leds/0`` identificeert led 0 van de IoT-knoop.

*Opmerking* In een URL kun je nog meer onderdelen tegenkomen, voor de eenvoud zijn die hierboven weggelaten.
Voor de details, zie de Wikipedia-pagina of de officiële beschrijving in RFC3986.

*Opmerking* De notatie voor URL's wordt ook voor andere protocollen dan HTTP gebruikt,
bijvoorbeeld: ``file:`` - voor bestanden; ``ftp:`` - voor het File Transfer Protocol (FTP); of ``mailto:`` - voor e-mail.

Zie:

* [https://en.wikipedia.org/wiki/URL](https://en.wikipedia.org/wiki/URL)
* [https://tools.ietf.org/html/rfc3986](https://tools.ietf.org/html/rfc3986) (officiële beschrijving van URI en URL)


## HTTP request

```{figure} images/http-request-ex1.png
:width: 700px
:align: center

HTTP request voorbeeld
```

Hierboven zie je een voorbeeld van een HTTP-request.
Dit begint met ``GET /hello HTTP/1.1``
Hierin is ``GET`` de **HTTP-method**: deze bepaald het type van het request.
De belangrijkste methods zijn

* ``GET``, waarmee de client (browser) een webpagina van de server vraagt; en
* ``POST``, waarmee de client de inhoud van een webformulier naar de server stuurt.

In het gedeelte over REST-APIs behandelen we nog enkele andere HTTP-methods.

Het URL-pad ``/hello`` geeft het pad van het webdocument op de server aan.
In veel gevallen verwijst dit naar een bestand in een filesysteem.

Tenslotte geeft ``HTTP/1.1`` de versie van het gebruikte protocol aan.

### Metadata: headers

Na de eerste regel volgen de *headers*:
dat zijn de metadata van het protocol, in de vorm van (naam, waarde)-paren.
Enkele veel-gebruikte headers zijn:

* ``Host`` - het domeinnaam:poortnr-deel uit de URL (bijv. ``infvopedia.nl:1880``).
* ``Accept`` - het type van de payload dat de client verwacht (bijv. ``text/html``);
* ``User-Agent`` - de identificatie van de client (browser);
* ``Cookie`` - een cookie dat eerder door de client van de server ontvangen is;
* ``Content-Type`` - het type van de payload (bijvoorbeeld ``text/html; charset=utf-8``)

## HTTP-response en payload


``` {figure} images/http-response-ex1.png
  :width: 500px
  :align: center
  
  HTTP response bij het eerdere request-voorbeeld
```

De eerste regel van de response geeft de resultaatcode.

``200`` betekent, zoals de rest van de regel zegt: OK.
Een andere code die je tegenkomt is bijvoorbeeld ``404``,
voor een webpagina die niet gevonden kan worden.

De regels daarna vormen de headers: de metadata van het protocol.
De header ``Content-Length`` geeft de lengte van de payload.
De header ``Content-Type`` geeft het payload-formaat aan.
Dat is in dit geval ``text/html``, voor een HTML-document;
in veel APIs kom je ook JSON tegen: ``application/json``.

De tekst daarna is de payload, in HTML-formaat.
Dit formaat is vooral bedoeld voor webpagina's die je in een browser weergeeft.
Voor APIs is het JSON-formaat handiger:
een programma kan JSON eenvoudig in een object omzetten, en omgekeerd.

## HTTP methods

P.M.

* GET, POST, PUT, DELETE, HEAD, PATCH, enz.

## HTTP in de protocolstack


```{figure} images/http-ip-stack.png
:width: 700 px
:align: center

Webserver protocolstack
```

De protocolstack voor de webserver-keten bevat de volgende elementen, vanaf de toepassing gezien:

* web-app
* web: hypertext transfer protocol (HTTP): HTML-documenten enz.
* internet: transmission control protocol (TCP): betrouwbare bi-direectionele bytestromen
* internet-protocol (IP): best-effort pakketcommunicatie;
  universeel datatransport, onafhankelijk van hardware en toepassingen
* fysieke (hardware) verbinding: WiFi of Ethernet

De basisprotocollen van het internet, TCP en IP, vormen een logische laag die de toepassingen scheidt van de hardware
(zie *3-lagen model*).

Het HTTP-protocol vind je alleen in de eindapparaten, niet in het netwerk zelf.
Dit is een voorbeeld van het *end-to-end principe* van het internet.
Dit betekent bijvoorbeeld dat wanneer er een nieuwe versie is van het HTTP-protocol,
er geen aanpassingen in het netwerk zelf nodig zijn.

Bovendien kan het verkeer tussen de client en de server "end-to-end" versleuteld worden:
alleen in de client en in de server is de data niet-versleuteld toegankelijk.
Voor deze versleuteling (in het geval van HTTPS) heb je een apart protocol nodig: TLS,
tussen TCP en HTTPS.

## Authenticatie en autorisatie

P.M.

* username/password
* cookies
* API-token

## Communicatie tussen webservers

```{figure} images/iot-web-api-1.png
:width: 400 px
:align: center

Computer (toepassing) als client van een webserver
```

Toepassing als client van een webserver.

```{figure} images/iot-web-api-2.png
:width: 500 px
:align: center

Een web van clients en servers, sterk verweven
```

Een webserver kan ook weer als client van een andere webserver optreden, en omgekeerd.
Deze onderlinge communicatie tussen webservers vormt de basis voor het programmeerbare web.
