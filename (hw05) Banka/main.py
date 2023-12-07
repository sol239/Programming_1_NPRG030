
def implementation_1():
    """Implementation without using binary search tree"""
    def handle_input():
        """Handle input"""
        days = []

        while True:
            day = input()
            if day == "":
                break
            days.append([day.split(";")])


        return days

    #days = handle_input()

    # testing input
    days = [[['222222:N:10', '111111:N:50', '333333:N:6000000', '']], [['111111:I:2000', '333333:N:6', '222222:D:20', '']], [['444444:N:42', '222222:Q:0', '']]]


implementation_1()