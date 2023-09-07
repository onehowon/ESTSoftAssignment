l = [[1, 10, 'leehojun'], 
     [20, 30, 'hojun'], 
     [10, 20, 'weniv!'], 
     [1, 2, 'hello world'], 
     [55, 11, 'sun']]

# 1. 글자 수 대로 정렬해주세요.
def f(x):
    return len(x[2])

print(sorted(l, key=f, reverse=False))
print(sorted(l, key=lambda x:len(x[2]), reverse=False))

# 2. 맨 앞에 위치한 숫자대로 정렬해주세요.
def f2(x):
    return x[0]

print(sorted(l))
print(sorted(l, key=f2))
print(sorted(l, key=lambda x:x[0]))

# 3. 중앙에 위치한 값대로 정렬해주세요.

def f3(x):
    return x[1]

print(sorted(l))
print(sorted(l, key=f3))
print(sorted(l, key=lambda x:x[1]))