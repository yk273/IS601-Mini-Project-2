import unittest
from CsvReader.TestData import test_data_values
from CsvReader.TestDataResults import test_data_results
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CSVReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()
        self.test_data_values = CSVReader('StatData/Statistics_Values.csv').float_data
        self.test_data_results = CSVReader('StatData/Statistics_Results.csv').float_data

    def getUp(self) -> None:
        return self.test_data_values
        return self.test_data_results

    def test_instantiate_statistics_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_data_property(self):
        self.assertEqual(self.statistics.data, [])

    def test_population_mean(self):
        for row in test_data_values({}):
            result = test_data_results.float(row['Population_Mean'])
            self.assertEqual(self.statistics.population_mean((row['Values']), result))
            self.assertEqual(self.statistics.result, result)

    def test_median(self):
        for row in test_data_values({}):
            result = test_data_results.float(row['Median'])
            self.assertEqual(self.statistics.median((row['Values']), result))
            self.assertEqual(self.statistics.result, result)

    def test_mode(self):
        for row in test_data_values({}):
            result = test_data_results.float(row['Mode'])
            self.assertEqual(self.statistics.mode((row['Values']), result))
            self.assertEqual(self.statistics.result, result)

    def test_population_standard_deviance(self):
        for row in test_data_values({}):
            result = test_data_results.float(row['Population_Standard_Deviance'])
            self.assertAlmostEqual(self.statistics.population_standard_deviance((row['Values']), result))
            self.assertAlmostEqual(self.statistics.result, result)

    def test_variance_population_proportion(self):
        for row in test_data_values({}):
            result = test_data_results.float(row['Variance_Population_Proportion'])
            self.assertEqual(self.statistics.variance_population_proportion((row['Values']), result))
            self.assertEqual(self.statistics.result, result)

    def test_population_variance(self):
        for row in test_data_values({}):
            result = test_data_results.float(row['Variance'])
            self.assertAlmostEqual(self.statistics.population_variance((row['Values']), result))
            self.assertAlmostEqual(self.statistics.result, result)

    def test_zscore(self):
        for row in test_data_values({}):
            result = test_data_results.float(row['Zscore'])
            self.assertEqual(self.statistics.zscore((row['Values']), result))
            self.assertEqual(self.statistics.result, result)

    def test_population_correlation_coefficient(self):
        for row in test_data_values({}):
            result = test_data_results.float(row['Population_Correlation_Coefficient'])
            self.assertEqual(self.statistics.population_correlation_coefficient((row['Values']), result))
            self.assertEqual(self.statistics.result, result)

    def test_confidence_interval_ADD(self):
        for row in test_data_values({}):
            result = test_data_results.float(row['Confidence_Interval_ADD'])
            self.assertEqual(self.statistics.confidence_interval_ADD(row['Values'], result))
            self.assertEqual(self.statistics.result, result)

    def test_confidence_interval_SUB(self):
        for row in test_data_values({}):
            result = test_data_results.float(row['Confidence_Interval_SUB'])
            self.assertEqual(self.statistics.confidence_interval_SUB((row['Values']), result))
            self.assertEqual(self.statistics.result, result)

    def test_proportion(self):
        for row in test_data_values({}):
            result = test_data_results.float(row['Proportion'])
            self.assertEqual(self.statistics.proportion((row['Values']), result))
            self.assertEqual(self.statistics.result, result)

    def test_num_values(self):
        for row in test_data_values({}):
            result = test_data_results.float(row['Num_Values'])
            self.assertEqual(self.statistics.num_values((row['Values']), result))
            self.assertEqual(self.statistics.result, result)

    def test_get_sample(self):
        expected_range = range(5, 6)
        for row in test_data_values({}):
            result = float(row['Values']).getSample(test_data_values, sample_size=self.sample_size)
            self.assertIn(result, expected_range)

    def test_instantiate_statistical_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)


# sample mean, sample standard deviation, variance of sample proportion, and P-value cannot be tested
# all of these calculations require a sample population
#  this is due to the random package in the GetSample module


if __name__ == '__main__':
    unittest.main()
