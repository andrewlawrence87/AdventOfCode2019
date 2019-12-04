import os
import pprint
from src.main.classes.DayThreeMaze import DayThreeMaze


def get_input_csv():
    script_dir = os.path.dirname(__file__)
    rel_path = "resources\\day_three.txt"
    path = os.path.join(script_dir, rel_path)
    f = open(path, 'r')
    lines = f.read().split("\n")

    for line in lines:
        if line != "":  # add other needed checks to skip titles
            cols = [x for x in line.split(",")]
    return cols



starting_pos = [500, 500]
grid = DayThreeMaze(1000, starting_pos)

grid.move_up(7)
grid.move_right(6)
data = get_input_csv()
# print(grid.grid)
pprint.pprint(grid.crossover_points)

grid.calculate_closest_crossover()
