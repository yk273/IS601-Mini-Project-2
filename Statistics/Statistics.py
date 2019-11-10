from Calculator.Calculator import Calculator
from Statistics.PopulationMean import population_mean
from Statistics.Median import median
from Statistics.Mode import mode

class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def population_mean(self, pop_mean_list):
        self.data = population_mean(pop_mean_list)
        return self.data

    def median(self, median_list):
        self.data = median(median_list)
        return self.data

    def mode(self, mode_list):
        self.data = mode(mode_list)
        return self.data

