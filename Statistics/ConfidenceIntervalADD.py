from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Square_Root import square_root
from Statistics.PopulationMean import population_mean
from Statistics.PopulationStandardDeviation import population_standard_deviance
from Statistics.Zscore import zscore


def confidence_interval_ADD(confidence_interval_ADD_list):
    num_values = len(confidence_interval_ADD_list)
    total = 0
    for num in confidence_interval_ADD_list:
        total = addition(total, num)

    solution = addition(population_mean(confidence_interval_ADD_list), (multiplication(zscore(confidence_interval_ADD_list)), division(population_standard_deviance(confidence_interval_ADD_list), square_root(num_values))))
    #solution_2 = subtraction(population_mean(confidence_interval_list), (multiplication(zscore(confidence_interval_list)), division(population_standard_deviance(confidence_interval_list), square_root(num_values))))
    return solution
