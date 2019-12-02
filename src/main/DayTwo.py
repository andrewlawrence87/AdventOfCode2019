import csv
import os


def get_input_csv():
    script_dir = os.path.dirname(__file__)
    rel_path = "resources\\day_two.txt"
    path = os.path.join(script_dir, rel_path)
    f = open(path, 'r')
    lines = f.read().split("\n")

    for line in lines:
        if line != "":  # add other needed checks to skip titles
            cols = [int(x) for x in line.split(",")]

    return cols


def opt1(input_arr, start_index):
    return input_arr[input_arr[1 + start_index]] + input_arr[input_arr[2 + start_index]]


def opt2(input_arr, start_index):
    return input_arr[input_arr[1 + start_index]] * input_arr[input_arr[2 + start_index]]


data = get_input_csv()
i = 0
data[1] = 12
data[2] = 2

y = data.__len__()
while data[i] != 99:
    if data[i] == 1:
        data[data[i + 3]] = opt1(data, i)
    elif data[i] == 2:
        data[data[i + 3]] = opt2(data, i)
    if (i + 4) <= y:
        i += 4
    else:
        break

print(data[0])
