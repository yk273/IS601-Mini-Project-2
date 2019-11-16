from Statistics.PopulationStandardDeviation import population_standard_deviance
from Statistics.GetSample import getSample


def sample_standard_deviance(sample_standard_deviance_list):
    return population_standard_deviance(getSample(sample_standard_deviance_list, 5))
