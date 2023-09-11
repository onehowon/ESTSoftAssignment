import json
import matplotlib

file_path = '230911\data.json'

with open(file_path) as f:
    data =json.load(f)
    
total_age = 0
for member in data:
    total_age += member['age']
average_total = total_age / len(data)
print(average_total)

rate_male = 0
rate_female = 0

for member in data:
    if member['gender'] == 'male':
        rate_male += 1
    else:
        rate_female += 1

gender_ratio = {
    'male' : rate_male / len(data),
    'female' : rate_female / len(data)
}

print(gender_ratio)

