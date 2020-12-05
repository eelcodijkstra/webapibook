# Binder

Binder ([https://mybinder.org](https://mybinder.org)) biedt een laagdrempelige manier om Jupyter Notebooks uit te voeren.
Via een binder-link met daarin de naam van een GitHub-repository wordt een virtuele machine aangemaakt om de Notebooks in dat repository uit te voeren.

Deze virtuele machine blijft actief zolang je deze (interactief) gebruikt; als je deze een aantal minuten niet gebruikt hebt, verdwijnt deze weer.

## Tips

### Bewaren en herstellen in de browser

Als de binder-virtuele machine verdwijnt, verdwijnen ook de gegevens en opdrachten die je ingevoerd hebt.
Dit kan lastig zijn als je met een complexe opdracht in een notebook bezig bent.

```{image} images/jupyter-binder-save.png
:width: 400px
:align: center
```

Via twee knoppen bovenin het notebook-interface kun je de inhoud van je notebook in de browser bewaren,
en later weer herstellen:

* bewaar de toestand van je notebook in de browser, en verlaat de virtuele machine;
* ... enige tijd later...
* start via Binder een virtuele machine met hetzelfde notebook (in dezelfde browser);
* herlaad de bewaarde toestand in het notebook.

### Andere notebooks in het repository

Binder start een virtuele machine op met alle notebooks in het GitHub-repository.
Op de volgende manier kun je navigeren naar de andere notebooks:

* klik op het jupyter-logo linksboven om naar de lijst met bestanden te gaan
    * open bij voorkeur deze lijst in een nieuwe pagina in de browser;
    * anders krijg je mogelijk de vraag of je de huidige pagina wilt verlaten (OK).
* in de lijst met bestanden kun je een Jupyter notebook openen door op het bestand te klikken
* je kunt meerdere notebooks open hebben, in verschillende browser-vensters/tabbladen.

Je kunt eerst ook het repository op GitHub bekijken, om na te gaan welke bestanden en notebooks je daar kunt vinden.
Je vindt dit repository via de "repository"-knop, onder het GitHub logo (octocat) bovenin.

## Andere Notebook-platformen

Je kunt Jupyter Notebook op je eigen computer installeren, bijvoorbeeld via Anaconda ([https://anaconda.org](https://anaconda.org)).



