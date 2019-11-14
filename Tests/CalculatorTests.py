import unittest
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CSVReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CSVReader('CalcData/Unit_Test_Addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtraction(self):
        test_data = CSVReader('CalcData/Unit_Test_Subtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiplication(self):
        test_data = CSVReader('CalcData/Unit_Test_Multiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_division(self):
        test_data = CSVReader('CalcData/Unit_Test_Division.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.divide(row['Value 2'], row['Value 1']), result)
            self.assertAlmostEqual(self.calculator.result, result)

    def test_square(self):
        test_data = CSVReader('CalcData/Unit_Test_Square.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(float(row['Value 1'])), result)
            self.assertEqual(self.calculator.result, result)

    def test_square_root(self):
        test_data = CSVReader('CalcData/Unit_Test_Square_Root.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.square_root(float(row['Value 1'])), result)
            self.assertAlmostEqual(self.calculator.result, result)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
