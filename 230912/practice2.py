숫자 = [1,2,3,4,5]
승수 = [2,2,2,3,3]

list(zip(숫자, 승수))

list(map(lambda x : x[0] ** x[1], zip(숫자, 승수)))

list(filter(lambda x: x>100, list(map(lambda x:x[0] ** x[1], zip(숫자, 승수)))))

sum(map(lambda x:x[0] ** x[1], zip(숫자, 승수)))