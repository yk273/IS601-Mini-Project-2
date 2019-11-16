from Calculator.Division import division
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Square_Root import square_root
from Statistics.PopulationMean import population_mean
from Statistics.SampleMean import sample_mean
from Statistics.PopulationStandardDeviation import population_standard_deviance
from Statistics.Num_Values import num_values


def P_value(P_value_list):
    return division(subtraction(sample_mean(P_value_list), population_mean(P_value_list)),
                    division(population_standard_deviance(P_value_list), square_root(num_values)))
