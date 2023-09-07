l = [[1, 10, 32], 
     [20, 30, 11], 
     [10, 20, 22], 
     [1, 2, 13], 
     [55, 11, 44]]


# 4. 3개의 전체 합이 작은 순서대로 출력해주세요.

def f4(x):
    return x[0] + x[1] + x[2]

def f5(x):
    return sum(x)

print(sorted(l, key=f4))
print(sorted(l, key=f5))
print(sorted(l, key=lambda x: sum(x)))
print(sorted(l, key=sum))