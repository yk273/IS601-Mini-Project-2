import csv
import numpy as np


class CSVReader:
    data = []
    float_data = np.array(data, dtype=float)

    def __init__(self, filepath):
        self.data = []

        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass
