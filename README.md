#Readme

Pogramet är skrivet i pyhon3.9
Pull requestsIssuesMarketplace
Explore
 
 
Znarfen/MonsterGamePublic
Pin
 Unwatch 1 
Fork 0
 Star 0
Code
Issues
Pull requests
Actions
Projects1

Pogramet är ett spel. I spelet har du monster som ska överleva så länge som möjligt.
Man satt mot en mostondare som är genererad av datorn. Om alla ens monster är döda är spelet slut.

## Teknologier/Språk

Pogramet är bara skrivet i python3.9 men använder sig av bibloteken; random, requests, time.
Alla bibloteken kommer med installationen av python3.9.

## Usage

Programet är uppdelad i två delar MonsterGame.py och monsters.py. I monsters.py finns alla klasser,
där förvaras hur ett monster genererar, hur ett monster kan bli uppgraderad och vem som får in bonus 
skada eller en negativ bonus skada. Medans MonsterGame.py använder sig av klasserna och metoderna
för att kunna skapa olika monster. Programmet startar även i main() funktionen i MonsterGame.py.

MonsterGame.py sparar ens score i score.txt. MonsterGame.py använder sig av score.txt för att hämta
en topplista på de som har fått högst score eller när man har "förlorat" läggs det in värden i score.txt.

## Installation

För att man ska kunna köra pogramet måste man ha med alla filler som är under MonsterGame. Filerna kan
man sedan sätta in i en egen mapp men det är viktigt att allt är samlat. (Det är för att monsters.py och
MonsterGame.py måste kunna kominisera med varandra).

För att starta pogramet är det bra att köra MonsterGame.py

## To do

Lägga till en "How to play" funktion för att kunna göra det tydligt för användaren att förstå vad den ska göra.

Lägga till en "Setings" funktion och text fil (Setings.txt) för att kunna ändra API och på hastigheten som
programet vissar text.


