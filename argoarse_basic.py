import yaml

filepath = '../complex_python_task/synonyms.yaml'

with open(filepath, "r") as f:
    data = yaml.safe_load(f)

# def key_value(key='',value=''):
#     with open(filepath, "r") as f:
#         data = yaml.safe_load(f)
#     if key in data and value in data['synonym_value']:
#         print(key,value)
#     elif key in data and value not in data['synonym_value']:
#         print(data[key]['synonym_name'])
#     elif key not in data and value in data['synonym_value']:
#         print(data[value])
#     else:
#         print('hello')
print(data['google']['synonym_value'])