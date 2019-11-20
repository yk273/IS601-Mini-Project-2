from CsvReader.CsvReader import CSVReader


def test_data_results(results_data):
    test_data = CSVReader('StatData/Statistics_Results.csv').float_data
    return test_data
