import unittest

from CsvReader.CsvReader import CSVReader, ClassFactory


class MyTestCase(unittest.TestCase):
    try:
        def setUp(self) -> None:
            self.csv_reader = CSVReader('StatData/Statistics_Values.csv')
    except OSError as e:
        print(e)

    try:
        def test_return_data_as_objects_values(self):
            test_data_values = self.csv_reader.return_data_as_objects('Values')
            self.assertIsInstance(test_data_values, list)
            test_class = ClassFactory('Values', self.csv_reader.data[0])
            for test_data in test_data_values:
                self.assertEqual(test_data.__name__, test_class.__name__)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    unittest.main()
