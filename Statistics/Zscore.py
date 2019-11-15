from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Statistics.PopulationMean import population_mean
from Statistics.PopulationStandardDeviation import population_standard_deviance


def zscore(zscore_list):
    num_values = len(zscore_list)
    total = 0
    for num in zscore_list:
        total = addition(total, num)
    return division((subtraction(zscore_list, num_values)), population_standard_deviance(zscore_list))
