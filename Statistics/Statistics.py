from Calculator.Calculator import Calculator
from Statistics.PopulationMean import population_mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.PopulationStandardDeviation import population_standard_deviance
from Statistics.Variance import variance
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

    def mode(self, mode_list):
        self.data = mode(mode_list)
        return self.data

    def population_standard_deviance(self, pop_standard_deviation_list):
        self.data = population_standard_deviance(pop_standard_deviation_list)
        return self.data

    def variance(self, variance_list):
        self.data = variance(variance_list)
        return self.data

    def zscore(self, zscore_list):
        self.data = zscore(zscore_list)
        return self.data
