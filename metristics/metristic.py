from interfaces import IMetrics
from math import sqrt

class METRICSTICS(IMetrics):
    def __init__(self, data):
        try:
            self.data = sorted(data)
            self.session_data = {'data': self.data}
        except Exception as e:
            raise Exception(f"Error occurred while initializing METRICSTICS: {e}")

    def mean(self):
        try:
            return sum(self.data) / len(self.data)
        except ZeroDivisionError:
            raise Exception("Error: Cannot calculate mean for an empty dataset.")

    def median(self):
        try:
            n = len(self.data)
            if n % 2 == 1:
                return self.data[n // 2]
            else:
                return (self.data[n // 2 - 1] + self.data[n // 2]) / 2
        except Exception as e:
            raise Exception(f"Error occurred while calculating median: {e}")

    def mode(self):
        try:
            freq = {}
            max_count = 0
            modes = []
            for value in self.data:
                freq[value] = freq.get(value, 0) + 1
                if freq[value] > max_count:
                    max_count = freq[value]
                    modes = [value]
                elif freq[value] == max_count:
                    modes.append(value)
            return modes
        except Exception as e:
            raise Exception(f"Error occurred while calculating mode: {e}")

    def standard_deviation(self):
        try:
            mu = self.mean()
            variance = sum((x - mu) ** 2 for x in self.data) / len(self.data)
            return sqrt(variance)
        except Exception as e:
            raise Exception(f"Error occurred while calculating standard deviation: {e}")

    def mad(self):
        try:
            mu = self.mean()
            return sum(abs(x - mu) for x in self.data) / len(self.data)
        except Exception as e:
            raise Exception(f"Error occurred while calculating MAD: {e}")

    def min_max(self):
        try:
            return min(self.data), max(self.data)
        except Exception as e:
            raise Exception(f"Error occurred while calculating Min & Max: {e}")
