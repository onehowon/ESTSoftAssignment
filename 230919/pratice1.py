num_list = [1,2,3,4,5,6,7,8,9]
target_sum = 10

result_list = []
for i in range(len(num_list)):
  for j in range(i+1, len(num_list)):
    if num_list[i] + num_list[j] == target_sum:
      result_list.append((num_list[i], num_list[j]))
print(target_sum)
for result in result_list:
  print(result)