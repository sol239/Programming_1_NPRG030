
def handle_input():
    """Function to handle input according to the problem statement
    returns list of numbers from 1 to n inclusive"""
    try:
        n = int(input())
        if n < 0:
            print("ERROR")
            exit()
    except ValueError:
        print("ERROR")
        exit()
    return n

def killer(n):
    """Function to solve the problem"""

    soldiers = [i for i in range(1, n + 1)]   # list of soldiers from 1 to n
    delka = n   # length of the list
    kill_list = [0] * n   # list of killed soldiers, 0 - alive, 1 - dead

    aim = 1
    kill_list[aim] = 1
    counter = 0   # counter for checking alive soldiers
    counter_2 = 0   # exiting loop after only one soldier is alive

    while True:
        aim += 1
        if aim > delka - 1:
            aim = delka - aim
        if kill_list[aim] == 0:
            counter += 1

        if counter == 2:
            kill_list[aim] = 1
            counter = 0
            counter_2 += 1

        if counter_2 == delka - 2:
            break

    # printing the result
    for x in range(0, delka):
        if kill_list[x] == 0:
            print(soldiers[x])


killer(handle_input())