from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Statistics.PopulationMean import population_mean
from Statistics.PopulationStandardDeviation import population_standard_deviance


def zscore(zscore_list):
    return division((subtraction(zscore_list, population_mean(zscore_list))), population_standard_deviance(zscore_list))
