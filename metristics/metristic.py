from interfaces import IMetrics
from math import sqrt

class METRICSTICS(IMetrics):
    def __init__(self, data):
        self.data = sorted(data)
        self.session_data = {'data': self.data}

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        n = len(self.data)
        if n % 2 == 1:
            return self.data[n // 2]
        else:
            return (self.data[n // 2 - 1] + self.data[n // 2]) / 2

    def mode(self):
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

    def standard_deviation(self):
        mu = self.mean()
        variance = sum((x - mu) ** 2 for x in self.data) / len(self.data)
        return sqrt(variance)

    def mad(self):
        mu = self.mean()
        return sum(abs(x - mu) for x in self.data) / len(self.data)

    def min_max(self):
        return min(self.data), max(self.data)
