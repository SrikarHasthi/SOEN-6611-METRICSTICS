from metristic import METRICSTICS
from interfaces import IRandom

class SimpleRandom(IRandom):
    def __init__(self):
        self.seed_value = 12345678

    def generate(self):
        a = 1664525
        c = 1013904223
        m = 2**32
        self.seed_value = (a * self.seed_value + c) % m
        return self.seed_value / m

def generate_test_data(random_generator, n=1000, low=0, high=1000):
    return [int(random_generator.generate() * (high - low) + low) for _ in range(n)]

def main():
    random_generator = SimpleRandom()
    n = int(input("Enter the number of data values: "))
    test_data = generate_test_data(random_generator, n)
    
    metrics = METRICSTICS(test_data)
    print("\nResults with User Input Data:")
    print("Mean:", metrics.mean())
    print("Median:", metrics.median())
    print("Mode:", metrics.mode())
    print("Standard Deviation:", metrics.standard_deviation())
    print("MAD:", metrics.mad())
    print("Min & Max:", metrics.min_max())

if __name__ == "__main__":
    main()
