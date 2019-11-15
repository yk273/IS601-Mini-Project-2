from Calculator.Addition import addition
from Calculator.Division import division


def proportion(proportion_list):
    num_values = len(proportion_list)
    total = 0
    for num in proportion_list:
        total = addition(total, num)

    return division(proportion_list, num_values)
