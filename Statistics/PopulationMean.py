from Calculator.Addition import addition
from Calculator.Division import division


def population_mean(mean_list):
    num_values = len(mean_list)
    total = 0
    for num in mean_list:
        total = addition(total, num)
    return division(total, num_values)


"""
import statistics


def population_mean(mean_list):
    solution = (statistics.mean(mean_list))
    return solution
"""