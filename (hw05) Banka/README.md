# Bank Software

This project involves programming software for a bank. The implementation should use a binary search tree.

## Services Provided

Clients can create accounts, deposit money, make withdrawals, and close their accounts if they are not satisfied.

## Client Identification

Clients are identified by unique six-digit numbers that do not start with 0. In the `bank.in` file, each line represents transactions from one day of bank operations, separated by a semicolon (there is also a semicolon after the last operation on the line). The encoding of one transaction is as follows:

`ACCOUNT_NUMBER:CODE:AMOUNT;`

where:

- `ACCOUNT_NUMBER` is a six-digit number that uniquely identifies the client.
- `CODE` is a capital letter that determines the type of transaction. The options are:
  - `N` - create a new account (New)
  - `Q` - close an existing account (Quit)
  - `I` - increase the amount stored in the account (Increase)
  - `D` - decrease the amount stored in the account (Decrease)
- `AMOUNT` is a non-negative integer (for `N`, it's the initial deposit amount, for `I/D`, it's the increase/decrease amount, and for `Q`, the value doesn't matter).

## Program Functionality

The program should perform the specified transactions for all days (lines of the `bank.in` file). Then, it should write a report of the transactions and the current state of all accounts for each day to the `bank.out` file.

The report for each day starts with the line:

`=== DAY ===`

where `DAY` is the line number of the input file.

The report includes a line for each transaction. If the transaction is successful, the corresponding line should be in the format:

`TRANSACTION OK`

In case of an unsuccessful transaction, we want to know where the error occurred. The format of the line corresponding to an unsuccessful transaction is:

`TRANSACTION error: ERROR_DESCRIPTION`

`ERROR_DESCRIPTION` is a string:

- "account does not exist!" if we don't have any record for the given account number
- "account already exists!" if a new account is to be created with a number that is already in use
- "low account balance!" if someone wants to withdraw more than they have deposited in their account

`TRANSACTION` means the triplet: `ACCOUNT_NUMBER:CODE:AMOUNT` (without a semicolon)

After performing all transactions from the currently processed day, an separator line should be printed:

`======`

Then, the states of all accounts should be printed in the format:

`ACCOUNT_NUMBER:AMOUNT`

In the printout, the account numbers must be sorted in ascending order (this is where the implementation using a binary search tree can be conveniently used).

If you program the task using a binary search tree (and write in the comment that you used BST), I will award you double points (this will not happen automatically, I will do it manually after the deadline).

## Example

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