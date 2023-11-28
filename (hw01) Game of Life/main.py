# Game of life

def handle_input() -> tuple[int, int, int, list[str]]:
    """Function which handles inputs"""

    line_1 = input().split()
    width, height = int(line_1[0]), int((line_1[1]))

    number_of_cycles = int(input())

    grid = []   # a grid containing initial state of the game
    for x in range(height):
        grid.append(input())

    return width, height, number_of_cycles, grid

