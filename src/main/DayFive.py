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


def opt3(input_arr, start_index, param1_mode, input):
    if param1_mode == 0:
        input_arr[input_arr[start_index + 1]] = input
    if param1_mode == 1:
        input_arr[start_index + 1] = input


def opt4(input_arr, start_index, param1_mode):
    if param1_mode == 0:
        print(input_arr[input_arr[start_index + 1]])
    if param1_mode == 1:
        print(input_arr[start_index + 1])


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
        param1_mode = int(s[1])
        param2_mode = int(s[0])
        op_code = int(s[3])
        if op_code == 1 or op_code == 2:
            data[data[i + 3]] = opt1_2(data, i, param1_mode, param2_mode, op_code)
            inc = 4
        elif op_code == 3:
            opt3(data, i, param1_mode, input)
            inc = 2
        elif op_code == 4:
            opt4(data, i, param1_mode)
            inc = 2
        if (i + inc) < y:
            i += inc
        else:
            break
    return data[0]


data = get_input_csv()

run_program(data, 1)
