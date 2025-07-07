import yaml
import json

ymal_str1 = """
person:
  name: Alick
  age: 25
  city: Taipei
"""

yaml_str2 = """
fruits:
  - Apple
  - Banana
  - Mongo
"""

yaml_str3 = """
users:
  - name: Tom
    role: admin
  - name: Jerry
    role: user
"""

python_dict1 = yaml.safe_load(ymal_str1)
print("YAML 1 -> Python dict:")
print(python_dict1)

json_str1 = json.dumps(python_dict1, indent=4)
print("\nPython dict 1 -> JSON:")
print(json_str1)

python_dict_from_json1 = json.loads(json_str1)
print("\nJSON -> Python dict 1:")
print(python_dict_from_json1)

yaml_str_again1 = yaml.dump(python_dict_from_json1)
print("\nPython dict 1 -> YAML again:")
print(yaml_str_again1)