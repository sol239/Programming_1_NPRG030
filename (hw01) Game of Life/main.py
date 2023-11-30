# Game of life

def handle_input() -> tuple[int, int, int, list[str]]:
    """Function which handles inputs"""

    line_1 = input().split()
    width, height = int(line_1[0]), int((line_1[1]))

    number_of_cycles = int(input())

    grid = []   # a grid containing initial state of the game
    for x in range(height):
        grid.append(list(input()))  # append each row of the grid as a list

    return width, height, number_of_cycles, grid

def cycle(width, height, number_of_cycles, grid):
    """Function which creates new grid with new state of cells."""
    def state_of_cell(grid):
        """Function which determine state of cell and creates new grid."""

        # Creating new grid with dimensions of initial grid.
        new_grid = []

        for y in range(len(grid)):

            grid_line = []
            for x in range(len(grid[y])):
                neigbours_of_cell = calculate_neighbours(x, y, len(grid[0]), len(grid))
                state = neighbours_analysis(neigbours_of_cell, grid)
                if (grid[y][x]) == "o":
                    if state < 2:
                        new_cell = "."
                    elif state == 2 or state == 3:
                        new_cell = "o"
                    else:
                        new_cell = "."

                else:
                    if state == 3:
                        new_cell = "o"
                    else:
                        new_cell = "."
                grid_line.append(new_cell)
            new_grid.append(grid_line)
        return new_grid


    def calculate_neighbours(x, y, width, height):
        """Function returns 8 neighbours of given cell as list of lists."""
        neighbours = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if [x, y] != [x + i, y + j]:
                    neighbours.append([x + i, y + j])

        for x in range(0, len(neighbours)):

            neigbour = neighbours[x]
            new_neigbour_x = neigbour[0]
            new_neigbour_y = neigbour[1]

            if new_neigbour_x >= width:
                new_neigbour_x = 0
            if new_neigbour_x < 0:
                new_neigbour_x = width - 1
            if new_neigbour_y >= height:
                new_neigbour_y = 0
            if new_neigbour_y < 0:
                new_neigbour_y = height - 1

            neighbours[x] =  [new_neigbour_x, new_neigbour_y]   # [x, y]

        return neighbours   # list of lists

    def neighbours_analysis(neighbours_of_cell, grid):
        """Returns number of living neighbours of given cell"""
        neigbours = []
        for neigbour in neighbours_of_cell:
            x = neigbour[0]
            y = neigbour[1]
            neigbours.append(grid[y][x])

        return neigbours.count("o")


    return state_of_cell(grid)

def main(width, height, number_of_cycles, grid):
    """Main function, which prints new grid with new state of cells."""

    for iteration in range(number_of_cycles):
        new_grid = (cycle(width, height, number_of_cycles, grid))
        print(width * "=")

        for x in new_grid:
            for letter in x:
                print(letter, sep="", end="")
            print()
            grid = new_grid   # new grid becomes initial grid for next iteration

if __name__ == "__main__":

    width, height, number_of_cycles, grid = handle_input()
    main(width, height, number_of_cycles, grid)