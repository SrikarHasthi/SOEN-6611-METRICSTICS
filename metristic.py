import json

class METRICSTICS:

    
    def __init__(self, data):
        self.data = self._sort(data)
        self.session_data = {'data': self.data}

    def _sort(self, data):
        flag = False
        i = 1
        while i < len(data):
            if(data[i] < data[i - 1]):
                flag = True
            i += 1
            
        # printing result
        if (not flag) :
            return data
        else :
            if not data:
                return []
            pivot = data[0]
            less = [x for x in data[1:] if x <= pivot]
            greater = [x for x in data[1:] if x > pivot]
            return self._sort(less) + [pivot] + self._sort(greater)

    def _sum(self, data):
        total = 0
        for value in data:
            total += value
        return total

    def _length(self, data):
        count = 0
        for _ in data:
            count += 1
        return count
    
    def mean(self):
        return self._sum(self.data) / self._length(self.data)

    def median(self):
        n = self._length(self.data)
        if n % 2 == 1:
            return self.data[n // 2]
        else:
            return (self.data[n // 2 - 1] + self.data[n // 2]) / 2

    def mode(self):
        freq = {}
        max_count = 0
        modes = []
        for value in self.data:
            if value not in freq:
                freq[value] = 1
            else:
                freq[value] += 1
            if freq[value] > max_count:
                max_count = freq[value]
                modes = [value]
            elif freq[value] == max_count and value not in modes:
                modes.append(value)
        return modes

    def standard_deviation(self):
        mu = self.mean()
        variance = self._sum([(x - mu) ** 2 for x in self.data]) / self._length(self.data)
        return self._sqrt(variance)

    def _sqrt(self, num):
        return num ** 0.5

    def mad(self):
        mu = self.mean()
        return self._sum([self._abs(x - mu) for x in self.data]) / self._length(self.data)

    def _abs(self, num):
        return num if num >= 0 else -num

    def min_max(self):
        return self.data[0], self.data[-1]
    
    def save_session(self, filename="session_data.json"):
        with open(filename, "w") as file:
            json.dump(self.session_data, file)
        print(f"Session data saved to {filename}")

    def load_session(filename="session_data.json"):
        try:
            with open(filename, "r") as file:
                session_data = json.load(file)
            data = session_data
            # metrics = METRICSTICS(data)
            print(f"Session data loaded from {filename}")
            return data
        except FileNotFoundError:
            print("Session data file not found. Starting a new session.")
            return None
        
    def menu():
        print("Select an Operation")
        print("1. Calculate Mean")
        print("2. Calculate Median:")
        print("3. Calculate Mode:")
        print("4. Calculate Standard Deviation:")
        print("5. Calculate MAD:")
        print("6. Calculate Min & Max:")
        print("7. Calculate All")
        opt_type = int(input())
        match opt_type:
            case 1:
                mean_value = metrics.mean()
                metrics.session_data['mean'] = mean_value
                print("Mean:", mean_value)

            case 2:
                print("Median:", metrics.median())

            case 3:
                print("Mode:", metrics.mode())
            
            case 4:
                print("Standard Deviation:", metrics.standard_deviation())

            case 5:
                print("MAD:", metrics.mad())

            case 6:
                print("Min & Max:", metrics.min_max())

            case 7:
                print("Mean:", metrics.mean())
                print("Median:", metrics.median())
                print("Mode:", metrics.mode())
                print("Standard Deviation:", metrics.standard_deviation())
                print("MAD:", metrics.mad())
                print("Min & Max:", metrics.min_max())

            case _:
                print("Wrong Input.")


def random():
    a = 1664525
    c = 1013904223
    m = 2**32
    random.seed_value = (a * random.seed_value + c) % m
    return random.seed_value / m

random.seed_value = 12345678  # Initial seed

def generate_test_data(n=100, low=0, high=100):
    return [int(random() * (high - low) + low) for _ in range(n)]

if __name__ == "__main__":

    print("Do you want to load previous session data? (yes/no)")
    load_session_choice = input().lower()
    if load_session_choice == "yes":
        metrics_data = METRICSTICS.load_session()
        metrics_data1 = metrics_data["data"]
        print(metrics_data)
        metrics = METRICSTICS(metrics_data1)
        METRICSTICS.menu()
        
    else:
        print("Please select how you want to input the data")
        print("1. Auto generate 10000 values")
        print("2. Input comma seperated data using command line")
        input_type = int(input())
        if(input_type == 1):
            test_data = generate_test_data()
            print(test_data)
            metrics = METRICSTICS(test_data)
        elif(input_type == 2):
            input_list = [int(x) for x in input().split(',')]
            metrics = METRICSTICS(input_list)

        METRICSTICS.menu()

        print("Do you want to save this session data? (yes/no)")
        save_session_choice = input().lower()
        if save_session_choice == "yes":
            metrics.save_session()
