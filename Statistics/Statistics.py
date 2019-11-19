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
from Statistics.SampleMean import sample_mean
from Statistics.SampleStandardDeviation import sample_standard_deviance
from Statistics.VarianceSampleProportion import variance_sample_proportion
from Statistics.P_Value import P_value
from Statistics.Proportion import proportion
from Statistics.Num_Values import num_values
from Statistics.GetSample import getSample
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

    def sample_mean(self):
        self.result = sample_mean(self.sample_mean_list)
        return self.result

    def sample_standard_deviance(self):
        self.result = sample_standard_deviance(self.sample_standard_deviance_list)
        return self.result

    def variance_sample_proportion(self):
        self.result = variance_sample_proportion(self.variance_sample_proportion_list)
        return self.result

    def P_value(self):
        self.result = P_value(self.P_value_list)
        return self.result

    def proportion(self):
        self.result = proportion(self.proportion_list)
        return self.result

    def num_values(self):
        self.result = num_values(self.proportion_list)
        return self.result

    def get_sample(self):
        self.result = getSample(self.data, self.sample_size)
        return self.result
