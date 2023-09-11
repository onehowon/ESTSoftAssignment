import json
from matplotlib import pyplot as plt

file_path = '230911\data.json'

with open(file_path) as f:
    data = json.load(f)

total_age = 0
for member in data:
    total_age += member['age']
average_age = total_age / len(data)
print(f"회원들의 age 평균: {average_age}")

num_male = 0
num_female = 0
for member in data:
    if member['gender'] == 'male':
        num_male += 1
    else:
        num_female += 1

gender_ratio = {
    'male' : num_male / len(data),
    'female' : num_female / len(data)
}

print('회원들의 남녀 성비:')
for gender, ratio in gender_ratio.items():
    print(f"{gender}: {ratio}")
    

labels = ['Male', 'Female']
sizes = [num_male, num_female]
colors = ['blue', 'pink']
plt.pie(sizes, labels=labels, colors = colors, autopct = '%1.1f%%')
plt.axis('equal')
plt.show()