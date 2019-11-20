from CsvReader.CsvReader import CSVReader
from CsvReader.TestData import test_data_values
from CsvReader.TestDataResults import test_data_results


class CSVFiles(CSVReader):

    def __init__(self):
        super().__init__()

    def test_data_value(self, test_data):
        self.result = test_data_values(self.test_data)
        return self.result

    def test_data_results(self, results_data):
        self.result = test_data_results(self.results_data)
        return self.result
