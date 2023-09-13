data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

result =[]

for row in data:
  for col in row:
    result.append(col + (col * 0.00014))

print(result)


