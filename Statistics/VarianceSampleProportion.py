from Statistics.VariancePopulationProportion import variance_population_proportion
from Statistics.GetSample import getSample


def variance_sample_proportion(variance_sample_proportion_list):
    return variance_population_proportion(getSample(variance_sample_proportion_list, 5))
