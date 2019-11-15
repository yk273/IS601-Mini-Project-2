from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.Zscore import zscore

import math


def population_correlation_coefficient(population_correlation_coefficient_list):
    num_values = len(population_correlation_coefficient_list)
    total = 0
    for num in population_correlation_coefficient_list:
        total = addition(total, num)

    return division(math.fsum(zscore), num_values)
