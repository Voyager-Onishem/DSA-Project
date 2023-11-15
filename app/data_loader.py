import json
import os
global metro_data
def load_metro_network_data(data_file):
    #print(os.getcwd())
    try:
        with open(data_file, "r") as file:
            temp = json.load(file)
        return temp
    except FileNotFoundError:
        print(f"Error: File {data_file} not found.")
        return None

data_file = os.path.join(os.getcwd(), "Metro-Route-Planner/app/data/metro_data.json")
metro_data = load_metro_network_data(data_file)
    #if metro_data:
        # Process the loaded metro network data
        #print("Metro Network Data Loaded Successfully:")
        #print(metro_data)