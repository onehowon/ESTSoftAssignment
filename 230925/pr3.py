# 문제2: (class 쓰레드) 하나의 숫자에 제곱근을 구하는 함수 sqrt_number(num)이 있었을 때 자체 예외 NegativeNumberError를 정의하세요. 이 예외는 음수가 입력될 때 발생하도록 합니다. 사용자로부터 숫자를 입력 받아 그 숫자의 제곱근을 반환하는 함수를 작성하세요. 입력된 숫자가 음수이면 NegativeNumberError를 발생시키고 "음수의 제곱근은 계산할 수 없습니다."라는 메시지를 출력하세요.

class NegativeNumberError(Exception):
  def __init__(self):
    super().__init__('음수의 제곱근은 계산할 수 없습니다.')

def sqrt_number(num):

  if num < 0:
    raise NegativeNumberError()
  print(num**(1/2))

sqrt_number(456)