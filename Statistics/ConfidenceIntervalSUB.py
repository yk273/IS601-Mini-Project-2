from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Square_Root import square_root
from Statistics.PopulationMean import population_mean
from Statistics.PopulationStandardDeviation import population_standard_deviance
from Statistics.Zscore import zscore
from Statistics.Num_Values import num_values


def confidence_interval_SUB(confidence_interval_SUB_list):
    return subtraction(population_mean(confidence_interval_SUB_list), (multiplication(zscore(confidence_interval_SUB_list)), division(population_standard_deviance(confidence_interval_SUB_list), square_root(num_values))))
