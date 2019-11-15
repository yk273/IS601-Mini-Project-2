from Calculator.Square import square
from Statistics.PopulationStandardDeviation import population_standard_deviance


def population_variance(population_variance_list):
    return square(population_standard_deviance(population_variance_list))
