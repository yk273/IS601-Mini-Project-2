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
        for row in test_data:
            result = float(row['Population_Mean'])
            self.assertEqual(self.statistics.population_mean(float(row['Values'])), result)
            self.assertEqual(self.statistics.result, result)

    def test_median(self):
        test_data = CSVReader('StatData/Statistics_Values.csv').float_data
        # result_data = CSVReader('StatData/Statistics_Results.csv').data
        for row in test_data:
            result = float(row['Median'])
            self.assertEqual(self.statistics.median(float(row['Values'])), result)
            self.assertEqual(self.statistics.result, result)

    def test_mode(self):
        test_data = CSVReader('StatData/Statistics_Values.csv').float_data
        # result_data = CSVReader('StatData/Statistics_Results.csv').float_data
        for row in test_data:
            result = float(row['Mode'])
            self.assertEqual(self.statistics.mode(row['Values'], result))
            self.assertEqual(self.statistics.result, result)

    def test_population_standard_deviance(self):
        test_data = CSVReader('StatData/Statistics_Values.csv').float_data
        # result_data = CSVReader('StatData/Statistics_Results.csv').float_data
        for row in test_data:
            result = float(row['Population_Standard_Deviance'])
            self.assertAlmostEqual(self.statistics.population_standard_deviance(row['Values'], result))
            self.assertAlmostEqual(self.statistics.result, result)

    def test_variance_population_proportion(self):
        test_data = CSVReader('StatData/Statistics_Values.csv').float_data
        # result_data = CSVReader('StatData/Statistics_Results.csv').float_data
        for row in test_data:
            result = float(row['Variance_Population_Proportion'])
            self.assertEqual(self.statistics.variance_population_proportion(row['Values'], result))
            self.assertEqual(self.statistics.result, result)

    def test_population_variance(self):
        test_data = CSVReader('StatData/Statistics_Values.csv').float_data
        # result_data = CSVReader('StatData/Statistics_Results.csv').float_data
        for row in test_data:
            result = float(row['Variance'])
            self.assertAlmostEqual(self.statistics.population_variance(row['Values'], result))
            self.assertAlmostEqual(self.statistics.result, result)

    def test_zscore(self):
        test_data = CSVReader('StatData/Statistics_Values.csv').float_data
        # result_data = CSVReader('StatData/Statistics_Results.csv').float_data
        for row in test_data:
            result = float(row['Zscore'])
            self.assertEqual(self.statistics.zscore(row['Values'], result))
            self.assertEqual(self.statistics.result, result)

    def test_population_correlation_coefficient(self):
        test_data = CSVReader('StatData/Statistics_Values.csv').float_data
        # result_data = CSVReader('StatData/Statistics_Results.csv').float_data
        for row in test_data:
            result = float(row['Population_Correlation_Coefficient'])
            self.assertEqual(self.statistics.population_correlation_coefficient(row['Values'], result))
            self.assertEqual(self.statistics.result, result)

    def test_confidence_interval_ADD(self):
        test_data = CSVReader('StatData/Statistics_Values.csv').float_data
        # result_data = CSVReader('StatData/Statistics_Results.csv').float_data
        for row in test_data:
            result = float(row['Confidence_Interval_ADD'])
            self.assertEqual(self.statistics.confidence_interval_ADD(row['Values'], result))
            self.assertEqual(self.statistics.result, result)

    def test_confidence_interval_SUB(self):
        test_data = CSVReader('StatData/Statistics_Values.csv').float_data
        # result_data = CSVReader('StatData/Statistics_Results.csv').float_data
        for row in test_data:
            result = float(row['Confidence_Interval_SUB'])
            self.assertEqual(self.statistics.confidence_interval_SUB(row['Values'], result))
            self.assertEqual(self.statistics.result, result)

    def test_instantiate_statistical_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)


if __name__ == '__main__':
    unittest.main()
