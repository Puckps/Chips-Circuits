# Chips-Circuits

## Introductie
Voor de minor Programmeren aan de UvA hebben wij de opdracht gekregen om de paden tussen gates op een chip te optimaliseren. Op een chip zitten een aantal begin en eindpunten (ook wel gates genoemd) deze moeten op een een bepaalde manier met elkaar verbonden worden. De paden die hiervoor worden gebruikt moeten zo kort mogelijk worden, mogen niet dubbel gebruikt worden en mogen ook niet door andere gates heen gaan. Wel mogen deze paden kruisen en de over elkaar heen gaan.

Om de case goed te begrijpen zijn de gebruikte termen hieronder uitgelegt.
![Terminologie](doc/terminologie_chips&circuts.PNG)
<br />
De locaties van de gates en de volgorde van het leggen van de paden zijn gegeven. In de [data folder](data) zijn de verschillende chips met bijbehorende netlists (lijsten met de volgordes van het leggen van de paden) te vinden. Per chip zijn er 3 van deze netlist gegeven. Om te kunnen berekenen of een oplossing beter is dan een andere oplossing is er ook een formule gegeven voor de kosten van de oplossing.

```C = n + k * 300``` 
<br />Hierin is **C** de totale kosten, **n** het aantal stukjes pad wat is gelegd en **k** het aantal kruisingen, deze zijn dus wel toegestaan maar krijgen extreem veel strafpunten. Het doel is dus om zo min mogelijk kosten te maken.

## State Space
Zonder een oplossing te hebben gemaakt hebben wij een inschatting gemaakt van de State Space van deze case. 
Aangezien de chip een grootte heeft van 15 x 16 x 8 zijn er 1920 nodes, en op elke node kan wel of geen pad worden gelegd. Hierdoor hebben we 1920 keuzemomenten met twee keuzes, hiervan is de volgorde belangrijk. <br />
![Formule tabel](doc/formule.PNG) 
<br />Met deze formule zijn wij op een State Space van 2^1920 gekomen. 

## BaseLine
Voor de BaseLine hebben wij een Greedy geschreven aangezien het random leggen van paden niet op een antwoord zou uitkomen. In ons Greedy algoritme bekijken we welke volgende stap van het pad het dichtst bij het eindpunt ligt. Dit doet het Greedy algoritme totdat hij bij de eind-node is aangekomen.

**Werking**<br />
Voor het runnen van het Greedy algoritme moet je deze activeren in de main.py<br />
```python3 main.py {de gewenste chip} {de gewenste netlist}```
<br />
Wanneer dit gerund wordt ontstaat er een output file en de daarbij horende representatie. 

### Uitkomsten
| Chip  | Netlist   	| Kosten   | Aantal intersections |
| ----- | ------------- | -------- | -------------------- |
| _0    | netlist_1     | 20       | 0                    |
| _0    | netlist_2     | 971      | 3                    |
| _0    | netlist_3     | 98       | 0                    |
| _1    | netlist_4     | 29.329   | 95 met gates         |
| _1    | netlist_5     | 70.199   | 228                  |
| _1    | netlist_6     | 86.711   | 285 met gates        |
| _2    | netlist_7     | 100.630  | 331 met gates        |
| _2    | netlist_8     | 117.804  | 386 met gates        |
| _2    | netlist_9     | 167.633  | 551 met gates        |
<br />
De scores die uit de baseline komen zijn nog niet valide. Dit komt doordat de intersections niet op een geldige manier worden gebruikt. Het kan zo zijn dat ze pad stukken dubbelbezetten. Ook is er te zien dat bij chip_2 er nog gates worden gebruikt om paden te kunnen leggen. Om te zorgen dat dit zo min mogelijk gebeurd hebben we hier wel een kosten van 500 aan gegeven. De uitkomsten zijn via Mathplotlib ook gevisualiseerd. Deze visualisaties zijn 

[hier](doc/greedy_uitkomsten.jpg) terug te vinden.

## Algoritme 1
Het eerste algoritme dat wij hebben geimplementeerd is het A* algoritme. Dit algoritme vindt altijd een pad naar het eindpunt wanneer er een pad bestaat.

Het A* algoritme maakt gebruikt van 3 soorten kosten:
1. G-cost: Afstand van pad naar begin-node.
2. H-cost: Afstand naar de eind-node.
3. F-cost: H-cost + G-cost.

De A* houdt ten alle tijden 2 lijsten bij:
1. Open nodes.
2. Gesloten nodes.

Uit de open-nodes wordt telkens de node gekozen met de laagste F-cost en de laagste H-cost gehaald. Deze node wordt vervolgens in de gesloten nodes gezet en zijn buren worden toegevoegd aan de open-nodes. Dit process gaat net zo lang door totdat het algoritme aankomt bij de eind-node. 

**Werking**<br />
Voor het runnen van het A* algoritme moet je deze activeren in de main.py<br />
```python3 main.py {de gewenste chip} {de gewenste netlist}```
<br />
Wanneer dit gerund wordt ontstaat er een output file en de daarbij horende representatie. Dit algoritme zorgt dat de uitkomt altijd het zelfde is.

### Uitkomsten
| Chip  | Netlist   	| Kosten   | Aantal intersections |
| ----- | ------------- | -------- | -------------------- |
| _0    | netlist_1     | 20       | 0                    |
| _0    | netlist_2     | 343      | 1                    |
| _0    | netlist_3     | 360      | 1                    |
| _1    | netlist_4     | 4.025    | 12                   |
| _1    | netlist_5     | 9.793    | 31                   |
| _1    | netlist_6     | 16.671   | 53                   |
| _2    | netlist_7     | 16.570   | 52                   |
| _2    | netlist_8     | 16.733   | 53                   |
| _2    | netlist_9     | 37.815   | 122                  |

<br />
Bij de Baseline waren de uitkomsten nog niet valide door het dubbel gebruiken van paden en door het gebruiken van gates in de paden. De uitkomsten van de A* zijn wel allemaal valide. Ook zijn ze ten opzichte van de Baseline flink verbeterd. De visualisaties zijn 

[hier](doc/A_uitkomsten.jpg) terug te vinden.

## Algoritme 2
Het tweede algoritme is een hill climber die de volgorde bepaald waarop paden gelegd moeten worden. De paden worden dus <ins>niet</ins> halverwege weggehaald en opnieuw aangelegd, er wordt enkel aan het begin van het leggen een volgorde bepaald waar aan vast wordt gehouden. De paden worden d.m.v. het eerder genoemde A* algoritme gelegd. Vervolgens worden steeds de netlists met de laagste kosten geselecteerd om kleine mutaties (paden verwisselen) op toe te passen, waarna deze stap veelvuldig herhaald wordt.

**Werking**<br />
Voor het runnen van het Hill Climber algoritme moet je deze activeren in de main.py <br />
```python3 main.py {de gewenste chip} {de gewenste netlist} {het aantal restarts} {het aantal keer verbeteren}```
<br />
Als uitkomst krijg je dan de beste gevonde uitkomt met de daarbij horende output file en representatie. Deze uitkomst is niet altijd dezelfde uitkomst, dit komt doordat de volgorde van de netlist random gekozen worden. 
Er kan ook een grafiek van de kosten over tijd gegenereert worden. Daarvoor moet eerst de code onderaan main.py ge-uncomment worden (niet compatible met andere algoritmen).

### Uitkomsten
| Chip  | Netlist   	| Kosten   | Aantal intersections |
| ----- | ------------- | -------- | -------------------- |
| _0    | netlist_1     | 22       | 0                    |
| _0    | netlist_2     | 43       | 0                    |
| _0    | netlist_3     | 56       | 0                    |
| _1    | netlist_4     | 365      | 1                    |
| _1    | netlist_5     | 2.589    | 7                    |
| _1    | netlist_6     | 7.661    | 23                   |
| _2    | netlist_7     | 6.910    | 20                   |
| _2    | netlist_8     | 10.748   | 33                   |
| _2    | netlist_9     | 20.449   | 64                   |
<br />
De Hill Climber gebruikt het A* algoritme wat er voor zorgt dat alle oplossingen valide zijn. Door het toepassen van een Hill Climber op de volgorde van de netlist kunnen we betere scores halen. De scores die zijn weer gegeven bij een begin populatie van 20 en het 20 keer verbeteren van de beste 5. De visualisaties zijn 

[hier](doc/hill_uitkomsten.jpg) terug te vinden.

## Experiment
Wij hebben drie experimenten uitgekozen om te onderzoeken. Deze zijn:
1. Het swappen van mindere onderdelen in de netlist inplaats van 1 net naar voren te plaatsen
2. Met het huidige algoritme hadden wij gekozen dat de beste 5 door gingen naar de "volgende ronde". Deze parameter hebben wij voor een experiment verhoogt en verlaagt.
3. Ook zijn we gaan kijken wat het invloed is als de aantal restarts en het aantal herhalingen groeit. 
4. Als laatste hebben wij toegevoegd dat hoe hoger het pad gaat hoe goedkoper het leggen van een pad is. 

**Experiment 1**
<br />
Voor experiment 1 hebben wij gekeken naar het effect van het aantal swaps op de hill-climber uitkomsten. Hiervoor hebben wij de hillclimber gedraaid met slechts 1 verwisseling van de netlist, met 5 verwisselingen van de netlist en met 10 verwisselingen in de netlist. Elk van de drie condities is tien keer gedraaid op chip 1 met netlist 5.
| Swaps | Gem. kosten | 
| ----- | ----------- |
| 1     | 11.787      |
| 5     | 10.599      |
| 10    | 11.343      | 

Uit de resultaten komt naar voren dat een hillclimber waarbij telkens 5 items uit de netlist worden verwisseld het beste presteert. 

**Experiment 2**
<br />
Voor het tweede experiment hebben we de invloed van het aantallen kinderen getest (populatie algoritme). Voor aantallen hebben we 3, 5 en 10 gekozen. Voor elk van deze aantallen is het programma 5 keer gedraaid op chip 1 met netlist 5. (Sinds het verkrijgen van resultaten, is een bug gefixt. De kosten zouden met de huidige versie lager zijn, maar de conclusie zou zelfde zijn.)

| Kinderen | Gem. kosten | 
| -------- | ----------- |
| 3        | 11.595,8    |
| 5        | 11.343      |
| 10       | 11.681,4    | 

Geen van deze aantallen gaf beduidend lagere kosten (zie tabel), maar we hebben 5 kinderen alsnog als standaard gekozen, omdat dit in de laagste gemiddelde kosten resulteerde.

**Experiment 3**
<br />
Wij hebben voor chip 1 en 2 gekeken wat het veranderen van het aantal restarts en het aantal herhalingen doet op de uitkomst. Hieruit blijkt dat hoe meer restarts je doet hoe meer kans op een betere oplossing. Dit is ook goed te verklaren aangezien de restart random volgordes van netlists zijn. Dus hoe meer verschillende volgordens hoe meer kans op een volgorde die bij een goede score past.
Wel hebben we ook gemerkt dat er na een hoeveelheid restarts de uitkomsten niet meer groot veranderen. 

**Experiment 4**
<br />
Voor experiment 4 zijn we gaan kijken wat het effect op de kosten is wanneer hoe hoger het pad gaat hoe goedkoper de kosten worden. Door dit experiment hebben wij nu alle chips (op netlist 9 na) kunnen oplossen zonder intersections. Deze uitkomsten zijn te zien in onderstaande tabel, hierin zijn ook de optimale kosten per netlist en chip weergeven. Dit zijn de kosten wanneer alle paden via de kortste weg worden gelegd zonder rekening te houden met intersections, gates en het dubbel gebruiken van paden. 
<br />
| Chip  | Netlist   	| Optimale kosten | Kosten uit laatste experiment |
| ----- | ------------- | --------------- | ----------------------------- |
| _0    | netlist_1     | 20              | 22                            |
| _0    | netlist_2     | 35              | 39                            |
| _0    | netlist_3     | 48              | 56                            |
| _1    | netlist_4     | 291             | 489                           |
| _1    | netlist_5     | 341             | 629                           |
| _1    | netlist_6     | 475             | 877                           |
| _2    | netlist_7     | 600             | 1014                          |
| _2    | netlist_8     | 578             | 1070                          |
| _2    | netlist_9     | 761             | 2029 met 2 int                |
<br />
Het laatste experiment is gerund met een begin populatie van 1000 en het dan 100 keer de top 5 verbeteren waarbij er bij het verbeteren steeds 5 swaps worden gebruikt met de multi_swap. Hiervoor hebben wij gekozen omdat dit uit de eerdere experimenten naar boven kwamen als de beste parameters. De visualisaties zijn 

[hier](doc/experiment_uitkomsten.jpg) 
terug te vinden.