import json

fp = 'details.txt'
data = []

with open(fp, 'r') as f:
    for line in f:
        values = line.strip()
        columns= {
            'word': values.lower(),
            'word_length': len(line)
        }
        data.append(columns)
list_of_dicts = [obj for obj in data]

json_data= json.dumps(list_of_dicts, indent=4, ensure_ascii=False)

with open('output.json', 'w') as f:
    f.write(json_data)