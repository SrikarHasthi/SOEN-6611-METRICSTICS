from metristic import METRICSTICS
from interfaces import IRandom
import json

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

def save_session(metrics, filename="session_data.json"):
        with open(filename, "w") as file:
            json.dump(metrics.session_data, file)
        print(f"Session data saved to {filename}")

def load_session(filename="session_data.json"):
    try:
        with open(filename, "r") as file:
            session_data = json.load(file)
            data = session_data
            print(data)
            # metrics = METRICSTICS(data)
            print(f"Session data loaded from {filename}")
            return data
    except FileNotFoundError:
        print("Session data file not found.")
        return None
        
def menu(metrics):
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
            median_value = metrics.median()
            metrics.session_data['median'] = median_value
            print("Median:", median_value)

        case 3:
            mode_value = metrics.mode()
            metrics.session_data['mode'] = mode_value
            print("Mode:", mode_value)

        case 4:
            std_deviation_value = metrics.standard_deviation()
            metrics.session_data['std_deviation'] = std_deviation_value
            print("Standard Deviation:", std_deviation_value)

        case 5:
            mad_value = metrics.mad()
            metrics.session_data['mad'] = mad_value
            print("MAD:", mad_value)

        case 6:
            min_max_values = metrics.min_max()
            metrics.session_data['min_max'] = min_max_values
            print("Min & Max:", min_max_values)

        case 7:
            mean_value = metrics.mean()
            median_value = metrics.median()
            mode_value = metrics.mode()
            std_deviation_value = metrics.standard_deviation()
            mad_value = metrics.mad()
            min_max_values = metrics.min_max()

            metrics.session_data['mean'] = mean_value
            metrics.session_data['median'] = median_value
            metrics.session_data['mode'] = mode_value
            metrics.session_data['std_deviation'] = std_deviation_value
            metrics.session_data['mad'] = mad_value
            metrics.session_data['min_max'] = min_max_values

            print("Mean:", mean_value)
            print("Median:", median_value)
            print("Mode:", mode_value)
            print("Standard Deviation:", std_deviation_value)
            print("MAD:", mad_value)
            print("Min & Max:", min_max_values)

        case _:
            print("Wrong Input.")

    print("Do you want to save this session data? (yes/no)")
    save_session_choice = input().lower()
    if save_session_choice == "yes":
        save_session(metrics)

def main():


    print("Do you want to load previous session data? (yes/no)")
    load_session_choice = input().lower()
    if load_session_choice == "yes":
        metrics_data = load_session()
        if(metrics_data == None):
            return
        metrics_data1 = metrics_data["data"]
        print(metrics_data)
        metrics = METRICSTICS(metrics_data1)
        menu(metrics)
        
    else:
        print("Please select how you want to input the data")
        print("1. Auto generate values")
        print("2. Input comma seperated data using command line")
        input_type = int(input())
        if(input_type == 1):
            random_generator = SimpleRandom()
            n = int(input("Enter the number of data values: "))
            test_data = generate_test_data(random_generator, n)
            print(test_data)
            metrics = METRICSTICS(test_data)
        elif(input_type == 2):
            input_list = [int(x) for x in input().split(',')]
            metrics = METRICSTICS(input_list)

        menu(metrics)

       


if __name__ == "__main__":
    main()
