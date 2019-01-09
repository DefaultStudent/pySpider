import json

filename = 'starlight.json'
with open(filename) as f:
    pop_data = json.load(f)

for pop_dict in pop_data:
    index_num = pop_dict['index']
    title = pop_dict['index_title']
    print(index_num + ": " + title)