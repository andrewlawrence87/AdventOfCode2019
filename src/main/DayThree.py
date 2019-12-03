import os
import pprint
from classes import DayThreeMaze


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


def move_right(input_arr, current_pos, no_moves):
    for k in range(0, no_moves):
        current_pos[1] += 1
        input_arr[current_pos[0]][current_pos[1]] += 1


def move_down(input_arr, current_pos, no_moves):
    for k in range(0, no_moves):
        current_pos[0] += 1
        input_arr[current_pos[0]][current_pos[1]] += 1


grid = DayThreeMaze


# def initialise_grid():
#     x = []
#     for row in range(10):
#         x.append([])
#
#     for row in x:
#         for col in range(10):
#             row.append(0)
#     return x


data = get_input_csv()
current_pos = [0, 0]
grid = initialise_grid()

move_right(grid, current_pos, 2)

move_down(grid, current_pos, 2)

pprint.pprint(grid)
