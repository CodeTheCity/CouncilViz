import json

with open('datasource/council_committee_JSON.json') as f:
    data = json.load(f)

# print(data)
    
categories_dict = {}

for c in data:
    categories_dict[c["Category"]] = 1
categories = list(categories_dict.keys())

with open('datasource/council_committee_categories.json', 'w') as f:
    f.write(json.dumps(categories))
    
print("Categories: ", categories)
