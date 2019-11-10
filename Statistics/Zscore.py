import scipy


def zscore(zscore_list):
    solution = scipy.stats.zscore(zscore_list)
    return solution
