from Calculator.Calculator import Calculator
from Statistics.PopulationMean import population_mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.PopulationStandardDeviation import population_standard_deviance
from Statistics.PopulationVariance import population_variance
from Statistics.Zscore import zscore

from CsvReader.CsvReader import CSVReader


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def population_mean(self):
        self.result = population_mean(self.mean_list)
        return self.result

    def median(self):
        self.result = median(self.median_list)
        return self.result

    def mode(self):
        self.result = mode(self.mode_list)
        return self.result

    def population_standard_deviance(self):
        self.result = population_standard_deviance(self.pop_standard_deviation_list)
        return self.result

    def population_variance(self):
        self.result = population_variance(self.population_variance_list)
        return self.result
'''
    def zscore(self, zscore_list):
        self.data = zscore(zscore_list)
        return self.data
'''