from Calculator.Square_Root import square_root
from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Multiplication import multiplication
from Calculator.Subtraction import subtraction
from Statistics.PopulationMean import population_mean
from Statistics.Num_Values import num_values


def variance_population_proportion(variance_population_proportion_list):
    return square_root(division(multiplication(subtraction(population_mean(variance_population_proportion_list), 1)), population_mean(variance_population_proportion_list), num_values))
