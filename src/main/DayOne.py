import os
import math

sum_fuel = 0


def file_path():
    script_dir = os.path.dirname(__file__)
    rel_path = "resources\\day_one.txt"
    return os.path.join(script_dir, rel_path)


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


def calc_fuel(mass):
    return round_down(mass / 3) - 2


def calc_total_fuel(mass):
    total_fuel = calc_fuel(mass)
    iteration_fuel = total_fuel
    while True:
        iteration_fuel = calc_fuel(iteration_fuel)
        if iteration_fuel >= 0:
            total_fuel += iteration_fuel
        else:
            return total_fuel


with open(file_path()) as fp:
    line = fp.readline()
    while line:
        sum_fuel += calc_fuel(int(line))
        line = fp.readline()
    print(sum_fuel)

with open(file_path()) as fp:
    sum_fuel = 0
    line = fp.readline()
    while line:
        sum_fuel += calc_total_fuel(int(line))
        line = fp.readline()
    print(sum_fuel)
