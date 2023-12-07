
def implementation_1():
    """Implementation without using binary search tree"""

    def handle_input():

        dataset = open("bank.in", "r", encoding="utf-8").read()
        days = []
        for day in dataset.splitlines():
            days.append(day.split(";")[:-1])
        return days

    days = handle_input()

    def transaction_id(data) -> str:
        """Returns transaction id"""
        data = data.split(":")[1]
        return data

    def show_bank_database(bank_database, output_file):
        """Shows sorted bank database, each line represents a different account"""
        bank_database = dict(sorted(bank_database.items()))
        for key, value in bank_database.items():
            output_file.write(f"{key}:{value}\n")

    def create_account(data, bank_database, output_file):
        """Returns dict with a new account if the account is not in the database"""
        data_str = data[:]
        data = data.split(":")
        if int(data[0]) not in bank_database:
            bank_database[int(data[0])] = int(data[2])
            output_file.write(data_str + " OK\n")
        else:
            output_file.write(data_str + " chyba: ucet uz existuje!\n")

        return bank_database

    def quit_account(data, bank_database, output_file):
        """Removes an account from the bank database if it's in, else prints an error message"""
        data_str = data[:]
        data = data.split(":")
        if int(data[0]) in bank_database:
            del bank_database[int(data[0])]
            output_file.write(data_str + " OK\n")
        else:
            output_file.write(data_str + " chyba: ucet neexistuje!\n")

        return bank_database

    def increase(data, bank_database, output_file):
        """Increases savings in an account if the account exists, otherwise prints an error message."""
        data_str = data[:]
        data = data.split(":")
        if int(data[0]) in bank_database:
            bank_database[int(data[0])] = int(bank_database[int(data[0])]) + int(data[2])
            output_file.write(data_str + " OK\n")
        else:
            output_file.write(data_str + " chyba: ucet neexistuje!\n")

        return bank_database

    def decrease(data, bank_database, output_file):
        """Increases savings in an account if the account exists, otherwise prints an error message or if not enough money."""
        data_str = data[:]
        data = data.split(":")
        if int(data[0]) in bank_database:
            if int(bank_database[int(data[0])]) - int(data[2]) > 0:
                bank_database[int(data[0])] = int(bank_database[int(data[0])]) - int(data[2])
                output_file.write(data_str + " OK\n")
            else:
                output_file.write(data_str + " chyba: nizky stav uctu!\n")
        else:
            output_file.write(data_str + " chyba: ucet neexistuje!\n")

        return bank_database

    def bank_out(days):
        """Main function that handles all transactions and writes output to a file"""

        with open("bank.out", "w", encoding="utf-8") as output:
            bank_database = {}
            for day_count, day in enumerate(days):
                output.write(f"=== {day_count + 1} ===\n")

                for transaction in day:
                    if transaction != "":
                        if transaction_id(transaction) == "N":
                            bank_database = create_account(transaction, bank_database, output)
                        elif transaction_id(transaction) == "Q":
                            bank_database = quit_account(transaction, bank_database, output)
                        elif transaction_id(transaction) == "I":
                            bank_database = increase(transaction, bank_database, output)
                        elif transaction_id(transaction) == "D":
                            bank_database = decrease(transaction, bank_database, output)

                output.write("======\n")
                show_bank_database(bank_database, output)

    bank_out(days)

def implementaion_2():
    """Implementation using binary search tree"""
    def handle_input():

        dataset = open("bank.in", "r", encoding="utf-8").read()
        days = []
        for day in dataset.splitlines():
            days.append(day.split(";")[:-1])
        return days

    days = handle_input()

implementaion_2()