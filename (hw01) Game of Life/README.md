Game of life
Co je Game of life
Game of life je celulární automat, který v roce 1970 vymyslel John Conway. Program simuluje vývoj čtvercových buňěk ve dvourozměrné mřížce, podle předem daných pravidel. Vaším úkolem bude Game of life naprogramovat.

Program dostane zadané rozměry světa (šířku a výšku). Každá buňka je buď mrtvá (.), nebo žije (o). Jelikož svět tvoří čtvercová síť buněk, tak má každá buňka 8 sousedů.

Čili svět o rozměru 10x5 může vypadat třeba následovně:

..........<br />
..o.......<br />
...o......<br />
.ooo......<br />
..........<br />
Svět se vyvíjí v časových krocích. Při jednom kroku se pro každou buňku přepočítá, zda zemře, ožije a nebo zůstane tak jak je. To vše se odvíjí od jejích sousedů:

Každá živá buňka s méně než dvěma živými sousedy zemře.
Každá živá buňka se dvěma nebo třemi živými sousedy zůstává žít.
Každá živá buňka s více než třemi živými sousedy zemře.
Každá mrtvá buňka s právě třemi živými sousedy oživne.
Jelikož nemůžeme simulovat nekonečný svět, tak budeme simulovat cyklický svět. To znamená, že pokud počítám živé sousedy buňky na úplném spodku světa, tak zespoda sousedí s odpovídajícími buňkami na úplném vršku světa. Stejně tak je svět cyklický i zprava doleva.

Pro více informací se podívejte na stránku wikipedie.

Co budu programovat
Program dostane následující vstup:

10 5<br />
7<br />
..........<br />
..o.......<br />
...o......<br />
.ooo......<br />
..........<br />
První řádek obsahuje šířku a výšku světa. Druhý řádek je počet časových kroků, které máte odsimulovat. Další řádky obsahují počáteční stav světa o zadaných rozměrech.

Odpovídající výstup vašeho programu bude následující:

==========<br />
..........<br />
..........<br />
.o.o......<br />
..oo......<br />
..o.......<br />
==========<br />
..........<br />
..........<br />
...o......<br />
.o.o......<br />
..oo......<br />
==========<br />
..........<br />
..........<br />
..o.......<br />
...oo.....<br />
..oo......<br />
==========<br />
..........<br />
..........<br />
...o......<br />
....o.....<br />
..ooo.....<br />
==========<br />
...o......<br />
..........<br />
..........<br />
..o.o.....<br />
...oo.....<br />
==========<br />
...oo.....<br />
..........<br />
..........<br />
....o.....<br />
..o.o.....<br />
==========<br />
...oo.....<br />
..........<br />
..........<br />
...o......<br />
....oo....<br />

Tedy jedná se o sedm požadovaných časových kroků simulace, oddělených znaky =. Počet znaků = je právě takový, jaká je šířka světa. Pozor, dělící čára předchází každý svět, i ten první. Naopak za posledním není.

