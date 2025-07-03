import json
import os

data = {
    "name": "Nick Chang",
    "age": 30,
    "skills": [
        "Python",
        "JSON",
        "YAML"
    ]
}

# json.dumps() converts a Python dictionary to a JSON string
json_str = json.dumps(data, indent=4)
print("json.dumps output (JSON string):")
print(json_str)
print()



# json.dump() writes a Python dictionary to a file in JSON format
# parent_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.pardir
parent_dir = os.path.dirname(os.getcwd())
print("Parent Directory (os.pardir()):", parent_dir)

data_dir = os.path.join(parent_dir,"data")
file_path = os.path.join(data_dir, "data.json")
if not os.path.exists(data_dir):
    print("Directory 'data' does not exist. Creating it...")
    os.makedirs(data_dir)
else:
    print("Directory 'data' already exists.")

with open(file_path,"w") as f:
    json.dump(data, f, indent=4)
print(f"Data has been written to {file_path}")
# json.loads() converts a JSON string back to a Python dictionary
parsed_data_from_json = json.loads(json_str)
print("json.loads output (Python dictionary from JSON string):")
print(parsed_data_from_json)
print()

# json.load() reads a JSON file and converts it to a Python dictionary
with open(file_path, "r") as f:
    parsed_data_from_file = json.load(f)
print("json.load output (Python dictionary from JSON file):")
print(parsed_data_from_file)
print()