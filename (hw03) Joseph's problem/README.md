EN:
While conquering Troy, some of defenders were cornered in a half-ruined temple. To avoid ignominious defeat, they decided to commit a collective suicide. They got arranged around the circle, they assigned numbers and they started lying onto their swords always skipping one in each step (i.e., first was soldier number 2, second number 4,...). One among them, Josephus, did not agree on this algorithm and he wanted to give up. It would be hardly possible that he would refuse to lie onto a sword (he would be murdered by the others). Advise him what number around the circle he should pick to survive as the last one.

Standard input consists of one integer N representable by 32bit integer. This is a number of Trojan soldiers. Output an integer J(N) - position around the circle that Josephus should take. For an incorrect input write 'ERROR'.

For N = 5 we proceed like this:

1 2 3 4 5 => 1 3 4 5 (soldier 2 is out)
1 3 4 5 => 1 3 5 (soldier 4 is out)
1 3 5 => 3 5 (soldier 1 is out)
3 5 => 3 (soldier 5 is out)
J(N) = 3
Example 1:

Input:
37
Output:
11

Example 2:

Input:
-5
Output:
ERROR

CZ:
Při dobývání Tróje byla hrstka obránců zahnána řeckými válečníky do polorozbořené budovy chrámu a obklíčena. Aby unikli ponižující porážce, rozhodli se Trójané spáchat sebevraždu. Stoupli si do kruhu, přiřadili si čísla a ob jednoho postupně nalehli na svůj meč. Začali vynecháním vojáka s číslem 1 a pokračovali v kruhu tak dlouho, dokud nebyli všichni mrtví. Jeden z Trójanů, říkejme mu Josef, ale s tímto postupem nesouhlasil a mnohem radši by se vzdal Řekům a zachránil si život. Poraďte Josefovi, na jaké místo v kruhu si má stoupnout, aby při rozpočítávání zůstal jako poslední a nikdo z Trójanů se tak nedozvěděl o jeho potupě.

Na standardním vstupu dostanete jedno celé číslo N v rozsahu typu longint - počet trójských vojáků. Vypište na standardní výstup celé číslo J(N) - místo v kruhu, na které si má Josef stoupnout. Při nekorektním vstupu vypište pouze řetězec 'ERROR'.

Pro N = 5 probíhá tedy vyřazování takto:

1 2 3 4 5 => 1 3 4 5 (vypadl voják 2)
1 3 4 5 => 1 3 5 (vypadl voják 4)
1 3 5 => 3 5 (vypadl voják 1)
3 5 => 3 (vypadl voják 5)
J(N) = 3
Příklad 1:

Vstup:
37

Odpovídající výstup:
11
Příklad 2:

Vstup:
-5

Odpovídající výstup:
ERROR

