student_score = {
		'hong': 97,
		'원희': 60,
		'동해': 77,
		'변수': 79,
		'창현': 89,
}

total_sum = sum(student_score.values())
print(total_sum)

total_avg = sum(student_score.values()) / len(student_score)
print(total_avg)

total_max = max(student_score.values())
target = total_max
total_max_person = [key for key, value in student_score.items() if value == target]
print(str(total_max_person), total_max)

total_min = min(student_score.values())
target = total_min
total_min_person = [key for key, value in student_score.items() if value == target]
print(str(total_min_person), total_min)

