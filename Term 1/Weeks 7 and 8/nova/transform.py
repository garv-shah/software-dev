import json

# Opening JSON file
f = open('input.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list

symbol_to_name = {}

for i in data['data']:
    symbol_to_name[i['symbol']] = i['id']

print(symbol_to_name)

# Closing file
f.close()

