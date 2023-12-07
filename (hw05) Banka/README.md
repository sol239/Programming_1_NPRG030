Naprogramujte software pro banku.

Při implementaci použijte binární vyhledávací strom.

Poskytované služby

Klienti si v bance zakládají účty, ukládají na ně peníze a provádějí výběry. Když nejsou spokojeni, tak si účet zruší.

Co banka potřebuje?

Klienti jsou identifikováni pomocí unikátních šesticiferných čísel, která nezačínají 0. V souboru bank.in jsou na každém řádku transakce z jednoho dne provozu banky oddělené znakem středník (za poslední operací na řádku je středník taky). Kódování jedné transakce je následující:

CISLO_UCTU:KOD:CASTKA;
kde:

CISLO_UCTU je šestimístné číslo, které jednoznačně identifikuje klienta

KOD je velké písmeno, které určuje typ transakce. Možnosti jsou:

N .... založit nový účet (New)
Q....zrušit existující účet (Quit)
I .... zvýšit uloženou částku na daném účtu (Increase)
D....snížit uloženou částku na daném účtu (Decrease)
CASTKA je nezáporné celé číslo (v případě N jde o iniciální vloženou částku, v případě I/D jde o přírůstek/úbytek a v případě Q na hodnotě nezáleží)

Program má za úkol provést zadané transakce pro všechny dny (řádky souboru bank.in). Do souboru bank.out má potom vypsat pro každý den hlášení o průběhu transakcí a výpis aktuálního stavu všech účtů.

Výpis každého dne začíná řádkem:

=== DAY ===
kde DAY je číslo řádku vstupního souboru.

Hlášení o průběhu obsahuje řádek pro každou provedenou transakci. Pokud je transakce úspěšná, příslušný řádek má být ve formátu:

TRANSAKCE OK
V případě neúspěšné transakce chceme vědět kde se stala chyba. Formát řádku, který přísluší k neúspěšné transakci, je:

TRANSAKCE chyba: POPIS_CHYBY
POPIS_CHYBY je řetězec:

"ucet neexistuje!" v případě, že pro dané číslo účtu nemáme žádný záznam
"ucet uz existuje!" v případě, že má být založen nový účet s číslem, které už je použité
"nizky stav uctu!" pokud by někdo chtěl vybírat víc než na má na účtě uloženo
TRANSAKCE znamená trojici: CISLO_UCTU:KOD:CASTKA (bez středníku)

Po provedení všech transakcí z aktuálně zpracovávaného dne má být vypsán oddělovací řádek:

======
Poté bude následovat výpis stavů všech účtů ve formátu:

CISLO_UCTU:CASTKA
Ve výpisu musí být čísla účtů seřazena podle velikosti od nejmenšího (zde se dá vhodně využít implementace pomocí binárního vyhledávacího stromu).

Pokud úlohu naprogramujete s použitím binárního vyhledávacího stromu (a napíšete do komentáře, že jste použili BVS), přidělím vám dvojnásobek bodů (to se nestane automaticky, to udělám ručně po vypršení deadlinu).

Příklad:

bank.in:

222222:N:10;111111:N:50;333333:N:6000000;
111111:I:2000;333333:N:6;222222:D:20;
444444:N:42;222222:Q:0;
bank.out:

=== 1 ===
222222:N:10 OK
111111:N:50 OK
333333:N:6000000 OK
======
111111:50
222222:10
333333:6000000
=== 2 ===
111111:I:2000 OK
333333:N:6 chyba: ucet uz existuje!
222222:D:20 chyba: nizky stav uctu!
======
111111:2050
222222:10
333333:6000000
=== 3 ===
444444:N:42 OK
222222:Q:0 OK
======
111111:2050
333333:6000000
444444:42