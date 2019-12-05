import os


def get_input_csv():
    script_dir = os.path.dirname(__file__)
    rel_path = "resources\\day_five.txt"
    path = os.path.join(script_dir, rel_path)
    f = open(path, 'r')
    lines = f.read().split("\n")

    for line in lines:
        if line != "":  # add other needed checks to skip titles
            cols = [int(x) for x in line.split(",")]

    return cols


def opt1_2(input_arr, start_index, param1_mode, param2_mode, op_code):
    x = input_arr[1 + start_index]
    y = input_arr[2 + start_index]
    if param1_mode == 0:
        x = input_arr[x]
    if param2_mode == 0:
        y = input_arr[y]
    if op_code == 1:
        return x + y
    if op_code == 2:
        return x * y


def convert_int_to_string(i):
    s = str(i)
    while s.__len__() < 4:
        s = str(0) + s
    return s


def run_program(data, input):
    i = 0
    y = data.__len__()
    inc = 0
    while data[i] != 99:
        s = convert_int_to_string(data[i])
        if data[i] == 1 or data[i] == 2:
            data[data[i + 3]] = opt1_2(data, i, s[0], s[1], data[i])
            inc = 4
        elif data[i] == 3:
            data[data[i + 1]] = input
            inc = 2
        elif data[i] == 4:
            print(data[i + 1])
            inc = 2
        if (i + inc) <= y:
            i += inc
        else:
            break
    return data[0]


data = get_input_csv()

run_program(data, 1)

# iter_noun = 0
# iter_verb = 0
#
# while data[0] != 19690720:
#     data = get_input_csv()
#     run_program(data, iter_noun, iter_verb)
#     if data[0] == 19690720:
#         break
#     if iter_noun < 99:
#         iter_noun += 1
#     elif iter_verb < 99:
#         iter_noun = 0
#         iter_verb += 1
#     else:
#         break
#
# print(100 * iter_noun + iter_verb)
