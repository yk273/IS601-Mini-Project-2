from CsvReader.CsvReader import CSVReader


def test_data_values(test_data):
    test_data = CSVReader('StatData/Statistics_Values.csv').float_data
    return test_data
