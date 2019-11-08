from Calculator.Calculator import Calculator
from Statistics.PopulationMean import population_mean


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def population_mean(self, pop_mean_list):
        self.data = population_mean(pop_mean_list)
        return self.data
