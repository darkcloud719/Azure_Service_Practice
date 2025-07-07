# import yaml

# yaml1 = """
# name: Nick Chang
# trigger:
# - main
# """

# yaml2 = """
# name: Nick Chang
# trigger:
#   - main
# """

# data = yaml.safe_load(yaml1)
# print(data)

import yaml
import json

# yaml_str = """
# name: Nick Chang
# age: 30
# skills:
#   - Python
#   - YAML
#   - JSON
# """

yaml_str = """
parameters:
  name: ''
  testFile: ''

stages:

- stage: Test_${{ parameters.name }}
  jobs:
    - job: ${{ parameters.name }}_Windows
"""

# Yaml to Python dictionary
python_dict = yaml.safe_load(yaml_str)
print("YAML -> Python dict:")
print(python_dict)

# Python dictionary to JSON

json_str = json.dumps(python_dict, indent=4)
print("\nPython dict -> JSON:")
print(json_str)

# JSON to Python dictionary
python_dict_from_json = json.loads(json_str)
print("\nJSON -> Python dict:")
print(python_dict_from_json)

# Python dicrtionary to YAML

yaml_str_again = yaml.dump(python_dict_from_json)
print("\nPython dict -> YAML:")
print(yaml_str_again)


# yaml.safe_load & json.loads are used to convert strings to Python dictionaries.
# yaml.dump & json.dumps are used to convert Python dictionaries to strings.