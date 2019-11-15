from Calculator.Calculator import Calculator
from Statistics.PopulationMean import population_mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.PopulationStandardDeviation import population_standard_deviance
from Statistics.PopulationVariance import population_variance
from Statistics.Zscore import zscore
from Statistics.VariancePopulationProportion import variance_population_proportion
from Statistics.PopulationCorrelationCoefficient import population_correlation_coefficient
from Statistics.ConfidenceIntervalADD import confidence_interval_ADD
from Statistics.ConfidenceIntervalSUB import confidence_interval_SUB

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

    def variance_population_proportion(self):
        self.result = variance_population_proportion(self.variance_population_proportion_list)
        return self.result

    def population_variance(self):
        self.result = population_variance(self.population_variance_list)
        return self.result

    def zscore(self):
        self.result = zscore(self.zscore_list)
        return self.result

    def population_correlation_coefficient(self):
        self.result = population_correlation_coefficient(self.population_correlation_coefficient_list)
        return self.result

    def confidence_interval_ADD(self):
        self.result = confidence_interval_ADD(self.confidence_interval_ADD_list)
        return self.result

    def confidence_interval_SUB(self):
        self.result = confidence_interval_SUB(self.confidence_interval_SUB_list)
        return self.result

