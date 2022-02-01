# Chips-Circuits

## Introductie
Voor de minor Programmeren aan de UvA hebben wij de opdracht gekregen om de paden tussen gates op een chip te optimaliseren. Op een chip zitten een aantal begin en eindpunten (ook wel gates genoemd) deze moeten op een een bepaalde manier met elkaar verbonden worden. De paden die hiervoor worden gebruikt moeten zo kort mogelijk worden, mogen niet dubbel gebruikt worden en mogen ook niet door andere gates heen gaan. Wel mogen deze paden kruisen en de over elkaar heen gaan.

Om de case goed te begrijpen zijn de gebruikte termen hieronder uitgelegt.
![Terminologie](doc/terminologie_chips&circuts.PNG)

De locaties van de gates en de volgoorde van het leggen van de paden zijn gegeven. In de [data folder](data) zijn de verschillende chips met bijbehorende netlists (lijsten met de volgoordes van het leggen van de paden) te vinden. Per chip zijn er 3 van deze netlist gegeven. Om te kunnen berekenen of een oplossing beter is dan een andere oplossing is er ook een formule gegeven voor de kosten van de oplossing.

```C = n + k * 300``` Hierin is **C** de totale kosten, **n** het aantal stukjes pad wat is gelegd en **k** het aantal kruisingen, deze zijn dus wel toegestaan maar krijgen extreem veel strafpunten. Het doel is dus om zo min mogelijk kosten te maken.

## State Space
Zonder een oplossing te hebben gemaakt hebben wij een inschatting gemaakt van de State Space van deze case. 
Aangezien de chip een grote heeft van 15 x 16 x 8 heeft 1920 nodes, op elke node kan wel of geen pad worden gelegd. Hierdoor hebben we 1920 keuzemomenten met twee keuzes, hiervan is de volgoorde belangrijk. ![Formule tabel](doc/formule.PNG) Met deze formule zijn wij op een State Space van 2^1920 gekomen. 

## BaseLine
Voor de BaseLine hebben wij een Greedy geschreven aangezien het random leggen van paden niet op een antwoord zou uitkomen. In ons Greedy algoritme hebben bekijken we welke volgende stap van het pad het dichts bij het eindpunt ligt. 

**Werking**

### Uitkomsten


## Algoritme 1
Aangezien onze Baseline nog niet voor alle chip valide uitkomsten genereerde zijn wij overgestapt naar een A* algoritme, 

**Werking**

### Uitkomsten

## Algoritme 2
De eerder gemaakte A* hebben wij voor het tweede algoritme gebruikt om een Hill Climber op te zetten. Hierin wordt de volgoorden van de netlist gesuffeld en vervolgens worden er in de beste netlist steeds kleine aanpassingen gemaakt om nog beter te worden.

**Werking**

### Uitkomsten

## Experiment
Wij hebben drie experimenten uitgekozen om te onderzoeken. Deze zijn:
1. Het swappen van mindere onderdelen in de netlist inplaats van 1 net naar voren te plaatsen
2. Met het huidige algoritme hadden wij gekozen dat de beste 5 door gingen naar de "volgende ronde". Deze parameter hebben wij voor een experiment verhoogt en verlaagt.
3. Als laatste zijn we gaan kijken wat het invloed is als de aantal restarts en het aantal herhalingen groeit. 
