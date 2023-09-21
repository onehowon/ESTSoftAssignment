def add(n):
  def decorator(function):
    def new_function(a,b):
      print(f'plus 함수가 {n}만큼 증가시키는 데코레이터가 시작됩니다.')
      result = function(a,b)
      print(result)
      print(f'plus 함수가 {n}만큼 증가시키는 데코레이터가 종료됩니다.')
      return result + n
    return new_function
  return decorator

@add(1000)
def plus(a,b):
  print('plus 함수가 호출되었습니다.')
  return a+b

result = plus(10,20)
print(f'result: {result}')