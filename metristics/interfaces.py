from abc import ABC, abstractmethod

# Interface for Metrics
class IMetrics(ABC):

    @abstractmethod
    def mean(self):
        pass

    @abstractmethod
    def median(self):
        pass

    @abstractmethod
    def mode(self):
        pass

    @abstractmethod
    def standard_deviation(self):
        pass

    @abstractmethod
    def mad(self):
        pass

    @abstractmethod
    def min_max(self):
        pass

# Interface for Random Number Generation
class IRandom(ABC):

    @abstractmethod
    def generate(self):
        pass
