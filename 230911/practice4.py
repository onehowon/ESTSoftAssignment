import json

with open('data.json') as f:
    data = json.load(f)

total_age = 0
for member in data:
    total_age += member['age']
average_age = total_age / len(data)
print(f"회원들의 age 평균: {average_age}")