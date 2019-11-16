from Statistics.PopulationMean import population_mean
from Statistics.GetSample import getSample


def sample_mean(sample_mean_list):
    return population_mean(getSample(sample_mean_list, 5))
