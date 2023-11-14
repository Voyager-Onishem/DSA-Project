import json
import os
metro_data=None
def load_metro_network_data(data_file):
    global metro_data
    #print(os.getcwd())
    try:
        with open(data_file, "r") as file:
            metro_data = json.load(file)
            print(metro_data)
        return metro_data
    except FileNotFoundError:
        print(f"Error: File {data_file} not found.")
        return None

if __name__ == "__main__":
    data_file = os.path.join(os.getcwd(), "app/data/metro_data.json")
    print(data_file)
    metro_data = load_metro_network_data(data_file)

    #if metro_data:
        # Process the loaded metro network data
        #print("Metro Network Data Loaded Successfully:")
        #print(metro_data)