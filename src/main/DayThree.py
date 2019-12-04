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


current_pos = [0, 0]
grid = DayThreeMaze(10, current_pos)

grid.move_down(5)
grid.move_right(5)

data = get_input_csv()
# print(grid.grid)
pprint.pprint(grid.grid)
