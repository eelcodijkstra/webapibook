# Inleiding Jupyter Notebooks

Voor het oefenen met web-API's in Python gebruiken we [Jupyter Notebooks](https://jupyter.org).
Hiermee kun je op een interactieve manier aan de slag, waarbij je alle vrijheden hebt om je eigen varianten uit te proberen.

```{Tip} Opstarten als interactief notebook

Start het interactieve notebook met de Launch Binder knop, onder de "raket" hierboven.
Binder start dan een server voor het interactieve notebook in een apart browser-tabblad.
```

Een notebook bestaan uit cellen.

Je selecteert een cel door op de cel te klikken, of in de kantlijn links van de cel.
Je selecteert de volgende/vorige cel met de pijltjestoetsen up/down.
**Selecteer nu deze cel.**

Er zijn twee soorten cellen: **Code** en **Markdown**. 
Het type van de geselecteerde cel vind je in de interface-balk bovenin.
Met dit menu kun je ook het type van de cel veranderen
Deze cel is een **Markdown** cel, de volgende cel is een (Python) **Code** cel. **Controleer dit.**

2 + 3 * 4

## Code-cellen

**Uitvoeren van een cel**. De cel hierboven is een Code-cel, met daarin een Python opdracht. **Voer deze cel uit (Run)**:

1. Selecteer de cel
2. Voer de cel uit, via Run (pijltje) in het menu hierboven, of via SHIFT-RETURN.

Zoals je ziet verschijnt het resultaat van de Python-opdracht onder de cel.

> Bij het uitvoeren van een Code-cel verschijnt er in de kantlijn een getal tussen rechte haken. Dit geeft de volgorde van de uitgevoerde cellen aan. Als je de cel nogmaals uitvoert, zie je een volgend getal.

**Aanpassen van een cel.** Je kunt de code in een Code-cel eenvoudig aanpassen: selecteer de cel, en verander de tekst.

**Verander de Python-code in de cel hieronder in:** `2 + 3 * 5` en **voer de cel uit**.

2 + 3

## Code: samengestelde opdrachten

Je kunt in een cel willekeurige stukken Python-code opnemen, inclusief import-opdrachten, functie-definities, enz.
De definities en declaraties kun je in de volgende cellen weer gebruiken:
op die manier kun je een groter programma stap voor stap opbouwen.

Als je een cel uitvoert, wordt de laatste expressie van die cel daaronder als resultaat getoond.

def succ(x):
    return x+1

succ(3)

**Opeenvolgende cellen.** Je kunt alle Code-cellen in een Notebook beschouwen als één groot Python-programma, dat je stukje bij beetje (cel voor cel) kunt uitvoeren.
Bij het uitvoeren van een cel wordt de waarde van de laatste expressie in de cel afgedrukt:
dit gebruik je meestal om tussenresultaten te kunnen controleren.

**Voer de onderstaande 2 cellen achtereenvolgens uit**

a = 13
b = a * 2
b

c = 14
2 * a + b + c

Een Code-cel bevat een stukje Python-programma. Dat kan ook een functie-defintie zijn.
Deze functie kan dan in dezelfde of in een volgende cel gebruikt worden.

**Voer de onderstaande 2 code-cellen achtereenvolgens uit**

def sqr (x):
    return x * x

sqr(12)

num = 12
sqr(num + 1)

Je kunt de tekst in een Markdown-cel aanpassen door deze in **edit-mode** te brengen.
Dit doe je door een dubbel-klik op de cel.
Je herkent deze mode aan het gebruik van een ander lettertype.

**Pas de inhoud van deze cel aan**

Een Markdown-cell breng je van edit-mode naar de geformatteerde tekst-mode door deze cel uit te voeren.
Je *voert een cel uit* (*Run*) door op het pijl-symbool bovenin te klikken, of door SHIFT-RETURN.

**Voer de cel hierboven uit om deze weer in geformatteerde tekst-mode te brengen.**

* Het uitvoeren van een Markdown-cel resulteert in het formatteren van de tekst.
* Het uitvoeren van een Code-cel resulteert in het uitvoeren van de code.

## Opdrachten

1. pas de tekst in deze cel aan (edit-mode) en voer deze cel uit.
2. pas de tekst van de cel hieronder aan en voer die cel uit.
3. verander het type van de cel hieronder en voer die cel uit.
   Let op het verschil tussen (2) en (3).

2 + 3 * 4

## Code werkt over meerdere cellen

Code die je uitvoert kan een zij-effect: bijvoorbeeld het definiëren van een functie of een variabele.
Het resultaat van dit zij-effect blijft bewaard en kun je gebruiken bij de uitvoering van een volgende cel.
We gebruiken dit later om een groter programma in kleinere delen te presenteren.

De onderstaande expressie gebruikt de functie die je hierboven gedefinieerd hebt:

x = succ(5)
x

En de cel hieronder gebruikt de variabele die je hiervoor gedefinieerd hebt:

succ(x)

## Code: shell-opdrachten in Python

In Python-code (in Jupyter Notebooks) kun je ook shell-opdrachten uitvoeren.
Deze worden dan uitgevoerd in het onderliggende operating system.
Het resultaat van zo'n opdracht kun je weer in Python verwerken.

Een shell-opdracht geef je aan met een `!`, bijvoorbeeld `!ls` 
(voor het opvragen van de namen van de bestanden in de huidige map).

!ls

files = !ls
files

len(files)

## Kernel

De code-cellen worden uitgevoerd door een *Kernel*-proces op de server.
In ons geval is dat een Python-Kernel.
Er zijn ook kernels voor andere programmeertalen beschikbaar.

De toestand van de kernel wordt bepaald door de cellen die je uitvoert,
in de volgorde zoals je die uitvoert.
Dit is niet altijd de volgorde waarin ze in het Notebook staan.

### Herstarten van de Kernel

Als je allerlei experimenten uitgevoerd hebt, wil je soms weer "met een schone lei beginnen".
Hiervoor kun je de Kernel herstarten via het menu bovenin.
In het bijzonder is het handig om daarbij de uitvoer van alle cellen ook te verwijderen:
dan is duidelijk wat er tot nu toe uitgevoerd is, en wat niet.


## Learn Python - the hard way

De cursus [Learn Python - the hard way](https://learnpythonthehardway.org) bevat allerlei opdrachten die letterlijk overgetypt moeten worden.
De auteur legt er de nadruk op dat je die voorbeelden zelf moet intikken: van copy-paste leer je veel minder.
Het intikken vraagt meer aandacht, en je maakt mogelijk leerzame fouten.

In het materiaal gebruiken we zo nu en dan stukjes Python om over te tikken.
Je zou gebruik kunnen maken van Copy-Paste, maar dan leer je er veel minder van.

Tik de onderstaande code over in de volgende cel, en voer dan de cel uit

```Python
def pred(x):
  return x-1
  
pred(succ(succ(3)))
```



## Volgorde

Bij de opzet van de Notebooks proberen we de volgende regels te gebruiken.
Deze verminderen de kans op fouten en verwarring.

1. De volgorde van de cellen in het notebook is de natuurlijke volgorde: in principe voer je deze van voor naar achter uit.
2. De code in een cel is zoveel mogelijk *idempotent*: het maakt niet uit of je deze één keer of vaker uitvoert.

Regel (1) betekent dat als je een cel in het midden van een reeks cellen opnieuw uitvoert,
dat je dan in principe de cellen daarna ook opnieuw moet uitvoeren.

Regel (2) betekent dat je opdrachten van de vorm `x = x + 1` moet vermijden. Voer in zo'n geval een nieuwe variabele in: `x1 = x + 1` o.i.d.

## Tussenvoegen en verwijderen van cellen

Je kunt een cel toevoegen na de huidge cel met het `+`-symbool in het interface bovenin.

De huidige cel verwijder je met het schaar-symbool in het interface bovenin.
(Met Z -undo cell operation- maak je dat weer ongedaan.)

Je kunt een cel verplaatsen met behulp van het handvat in de linker kantlijn.
(Dit werkt alleen voor de nieuwere JupyterLab, niet voor Jupyter Notebook.)



## Samenvatting

* een notebook bestaat uit cellen; een cel kan *tekst* bevatten (Markdown), zoals deze cel, of (Python) *code*, zoals de cellen hieronder.
* je voert een cel uit door deze te selecteren (cursor in de cel), en vervolgens SHIFT-RETURN in te toetsen.
  Ook het pijltje in de opdrachtenbalk hierboven kun je gebruiken.
* onder de cel zie je dan de uitvoer van deze opdracht.
* alle variabelen enz. die je introduceert in de code van een cel kun je in de volgende cellen gebruiken.
* met een `!` kun je een shell-opdracht uitvoeren; het resultaat kun je in Python gebruiken (als string).
* om problemen te voorkomen voer je cellen alleen uit *in de volgorde in het notebook*.
* je kunt eventueel opnieuw beginnen door de "Kernel" opnieuw te starten (via het cirkeltje, als bij een reload in de browser).
* zie voor meer informatie: help, en [tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)

De meeste code-cellen kun je zo uitvoeren; probeer de code en de uitvoer te begrijpen.
Bij sommige opdrachten moet je de code aanpassen, en dan de cel uitvoeren.

## Shortcuts





