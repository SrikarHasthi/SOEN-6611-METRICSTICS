import json
import os
from datetime import datetime
import uuid
from metristic import METRICSTICS
import hashlib


class SimpleRandom:
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

def save_session(metrics, session_file="sessions.json"):
    session_name = input("Please enter a session name: ")
    
    # Create a short hash of a new UUID
    short_session_id = hashlib.sha256(str(uuid.uuid4()).encode('utf-8')).hexdigest()[:8]  # Using just first 8 characters
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"session_{short_session_id}.json"

    # Save dataset to a file
    with open(filename, "w") as file:
        json.dump(metrics.session_data, file)

    # Save session information
    session_info = {
        'session_id': short_session_id,
        'session_name': session_name,
        'timestamp': timestamp,
        'file_location': filename
    }

    # Load existing sessions
    if os.path.exists(session_file):
        with open(session_file, "r") as file:
            sessions = json.load(file)
    else:
        sessions = []

    # Append new session and save
    sessions.append(session_info)
    with open(session_file, "w") as file:
        json.dump(sessions, file)
    
    # Inform the user about the saved session
    print(f"Session saved! Your session ID is: {short_session_id}")

def load_session(session_file="sessions.json"):
    try:
        session_id = input("Please enter the session ID: ")
        with open(session_file, "r") as file:
            sessions = json.load(file)
        
        # Search for the session info using the provided session ID
        session_info = next((session for session in sessions if session['session_id'] == session_id), None)
        
        if session_info is None:
            print("No session found with the given ID.")
            return None

        # Load the data from the file specified in the session info
        with open(session_info['file_location'], "r") as file:
            session_data = json.load(file)
            # Assuming METRICSTICS class is expecting a list of numbers
            metrics = METRICSTICS(session_data['data'])  
            return metrics

    except FileNotFoundError:
        print("Session file not found.")
        return None
    except json.JSONDecodeError:
        print("Error reading the session file. The file might be corrupted.")
        return None
    except Exception as e:
        print(f"Error occurred while loading session data: {e}")
        return None


def menu(metrics):
    
    try:
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
    except Exception as e:
        print(f"Error occurred: {e}")

    try:
        print("Do you want to save this session data? (yes/no)")
        save_session_choice = input().lower()
        if save_session_choice == "yes":
            save_session(metrics)
    except Exception as e:
        print(f"Error occurred while saving session data: {e}")

def main():
    try:
        load_session_choice = input("Do you want to load previous session data? (yes/no) ").lower()
        if load_session_choice == "yes":
            metrics = load_session()
            if metrics:
                menu(metrics)
        else:
            print("Please select how you want to input the data")
            print("1. Auto generate values")
            print("2. Input comma separated data using command line")
            input_type = int(input())
            if input_type == 1:
                random_generator = SimpleRandom()
                n = int(input("Enter the number of data values: "))
                test_data = generate_test_data(random_generator, n)
                print(test_data)
                metrics = METRICSTICS(test_data)
            elif input_type == 2:
                input_list = [int(x) for x in input("Enter the data points separated by commas: ").split(',')]
                metrics = METRICSTICS(input_list)
            else:
                print("Invalid input type.")
                return

            menu(metrics)

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
