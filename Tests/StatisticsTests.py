import unittest
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CSVReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_statistics_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_data_property(self):
        self.assertEqual(self.statistics.data, [])

    def test_population_mean(self):
        test_data = CSVReader('StatData/Statistics_Values.csv').float_data
        result_data = CSVReader('StatData/Statistics_Results.csv').float_data
        for row in test_data:
            result = result_data(row['Population_Mean'])
            self.assertEqual(self.statistics.population_mean(row['Values'], result))
            self.assertEqual(self.statistics.result, row['Population_Mean'])

    def test_instantiate_statistical_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)


if __name__ == '__main__':
    unittest.main()
