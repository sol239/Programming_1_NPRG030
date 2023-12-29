Write a program that evaluates an arithmetic expression in reverse-polish (prefix) notation (or write that the expression is wrong). Program reads one line with a given expression. Expression consists of operators +, -, * and / and of integer numbers (not necessarily single digits). All numbers and operators are (mutually) separated by single spaces.

All the numbers (including partial results) fit into 32bit integer. Operator / denotes the integral division. If the expression is wrong (including dividing by zero), write "ERROR".

Output is (one) integer, i.e., the value of the expression or the word "ERROR".

Example:
Input:
/ + 1 2 2

Output:
1