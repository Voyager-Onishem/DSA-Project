import json
import os
metro_data=None
def load_metro_network_data(data_file):
    print(os.getcwd())
    global metro_data
    try:
        with open(data_file, "r") as file:
            metro_data = json.load(file)
        return metro_data
    except FileNotFoundError:
        print(f"Error: File {data_file} not found.")
        return None

if __name__ == "__main__":
    data_file=os.getcwd()
    data_file += "/Metro-Route-Planner/app/data/metro_data.json"
    metro_data = load_metro_network_data(data_file)

    if metro_data:
        # Process the loaded metro network data
        print("Metro Network Data Loaded Successfully:")
        print(metro_data)
