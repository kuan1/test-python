import json
from os import path

# Changing JSON to Dictionary
person_json = '''{
    "name": "kuan",
    "country": "China",
    "city": "ShangHai",
    "skills": ["JavaScrip", "React", "Python"]
}'''

person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# Changing Dictionary to JSON
person = {
    "name": "kuan",
    "country": "China",
    "city": "ShangHai",
    "skills": ["JavaScrip", "React", "Python"]
}

person_json = json.dumps(person, indent=2)
print(person_json)
print(type(person_json))

# Saving as JSON File
temp3_path = path.join(path.dirname(__file__), 'temp3.txt')
with open(temp3_path, 'w', encoding='utf-8') as f:
  json.dump(person, f, ensure_ascii=False, indent=2)