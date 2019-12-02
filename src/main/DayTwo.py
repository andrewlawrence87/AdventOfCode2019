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


def run_program(data, noun, verb):
    i = 0
    data[1] = noun
    data[2] = verb
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
    return data[0]


data = get_input_csv()
print(run_program(data, 12, 2))

iter_noun = 0
iter_verb = 0

while data[0] != 19690720:
    data = get_input_csv()
    run_program(data, iter_noun, iter_verb)
    if data[0] == 19690720:
        break
    if iter_noun < 99:
        iter_noun += 1
    elif iter_verb < 99:
        iter_noun = 0
        iter_verb += 1
    else:
        break

print(100 * iter_noun + iter_verb)
